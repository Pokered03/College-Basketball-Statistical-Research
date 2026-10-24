"""Publish a compressed SQLite asset; restore with bounded memory and atomic replacement."""
import fcntl
import gzip
import hashlib
import json
import os
from pathlib import Path
import tempfile

MAX_DATABASE_BYTES=256*1024*1024
CHUNK_BYTES=1024*1024

def pack_database(database):
    database=Path(database)
    archive=database.with_suffix(database.suffix+'.gz')
    manifest=database.with_suffix(database.suffix+'.manifest.json')
    digest=hashlib.sha256();size=0
    fd,temp=tempfile.mkstemp(prefix='database-package-',dir=database.parent)
    try:
        with os.fdopen(fd,'wb') as output:
            with gzip.GzipFile(filename='',mode='wb',fileobj=output,mtime=0,compresslevel=6) as packed, database.open('rb') as source:
                while chunk:=source.read(CHUNK_BYTES):
                    size+=len(chunk)
                    if size>MAX_DATABASE_BYTES:raise ValueError('Database exceeds publication size limit')
                    digest.update(chunk);packed.write(chunk)
        os.replace(temp,archive)
        data={'format':1,'sha256':digest.hexdigest(),'database_bytes':size,'compressed_bytes':archive.stat().st_size}
        manifest.write_text(json.dumps(data,indent=2)+'\n')
        return data
    finally:
        if os.path.exists(temp):os.unlink(temp)

def ensure_database(database):
    """No-op on unchanged package. Never replaces the last good store on failure."""
    database=Path(database)
    archive=database.with_suffix(database.suffix+'.gz')
    manifest=database.with_suffix(database.suffix+'.manifest.json')
    if not archive.exists() or not manifest.exists():return False
    metadata=json.loads(manifest.read_text())
    expected=metadata['sha256'];size=int(metadata['database_bytes'])
    if not 0<size<=MAX_DATABASE_BYTES:raise ValueError('Invalid packaged database size')
    state=database.parent/'package-state.json'
    database.parent.mkdir(parents=True,exist_ok=True)
    with database.with_suffix('.package.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        if database.exists() and state.exists():
            try:
                cached=json.loads(state.read_text());stat=database.stat()
                if cached=={'sha256':expected,'mtime_ns':stat.st_mtime_ns,'bytes':stat.st_size} and stat.st_size==size:return False
            except (ValueError,OSError):pass
        fd,temp=tempfile.mkstemp(prefix='database-restore-',dir=database.parent)
        try:
            digest=hashlib.sha256();observed=0
            with os.fdopen(fd,'wb') as output,gzip.open(archive,'rb') as source:
                while chunk:=source.read(CHUNK_BYTES):
                    observed+=len(chunk)
                    if observed>size:raise ValueError('Packaged database exceeds declared size')
                    digest.update(chunk);output.write(chunk)
            if observed!=size or digest.hexdigest()!=expected:raise ValueError('Packaged database checksum mismatch')
            os.replace(temp,database)
            state.write_text(json.dumps({'sha256':expected,'mtime_ns':database.stat().st_mtime_ns,'bytes':observed}))
            return True
        finally:
            if os.path.exists(temp):os.unlink(temp)
