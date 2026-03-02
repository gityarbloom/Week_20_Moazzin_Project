from gridfs import GridFS
from pymongo import MongoClient
from grid_fs_config import GridFSConfig



class GridFSStorage:
    def __init__(self):
        self.environment = GridFSConfig()
        self.mongo_uri = self.environment.mongo_uri
        self.mongo_db_name = self.environment.mongo_db_name
        self.mongo_coll_name = self.environment.mongo_coll_name
        self.fs = self.get_grid_fs()

    def get_grid_fs(self):
        client = MongoClient(self.mongo_uri)
        db = client[self.mongo_db_name]
        fs = GridFS(db)
        return fs

    def save_in_mongo(self, bin_file):
        file_id = self.fs.put(bin_file)
        return f"\nfile_id of the uploaded File: {file_id} \n"
