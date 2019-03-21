from tinydb import TinyDB
from tinydb.storages import MemoryStorage
from pa.config import Config

def get_db(config=Config):
    return TinyDB(storage=MemoryStorage) if config.DB == 'memory' else TinyDB(config.DB)
