"""Last-good-store preservation and cache invalidation for compressed publication."""
import gzip,json
import pytest
from research.package import pack_database,ensure_database

def test_package_restore_cache_and_revised_data(tmp_path):
    db=tmp_path/'research.sqlite';first=b'SQLite format 3\0'+b'a'*3000000
    db.write_bytes(first);pack_database(db);db.unlink()
    assert ensure_database(db) is True and db.read_bytes()==first
    assert ensure_database(db) is False
    second=b'SQLite format 3\0'+b'b'*2000000
    db.write_bytes(second);pack_database(db)
    assert ensure_database(db) is True and db.read_bytes()==second

@pytest.mark.parametrize('damage',['checksum','oversize','truncated'])
def test_bad_package_preserves_last_good_database(tmp_path,damage):
    db=tmp_path/'research.sqlite';db.write_bytes(b'last known good')
    pack_database(db)
    archive=tmp_path/'research.sqlite.gz'
    if damage=='checksum':
        m=tmp_path/'research.sqlite.manifest.json';d=json.loads(m.read_text());d['sha256']='0'*64;m.write_text(json.dumps(d))
    elif damage=='oversize':
        with gzip.open(archive,'wb') as f:f.write(b'bad oversized data'*100)
    else:archive.write_bytes(archive.read_bytes()[:8])
    with pytest.raises((ValueError,OSError,EOFError)):ensure_database(db)
    assert db.read_bytes()==b'last known good'
    assert not list(tmp_path.glob('database-restore-*'))
