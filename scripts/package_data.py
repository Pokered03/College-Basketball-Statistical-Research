"""Pack in the background worker; unpack before updating a hosted checkout."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from research.store import DB_PATH
from research.package import pack_database,ensure_database
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('operation',choices=['pack','unpack']);args=p.parse_args()
    print(json.dumps(pack_database(DB_PATH) if args.operation=='pack' else {'restored':ensure_database(DB_PATH)}))
