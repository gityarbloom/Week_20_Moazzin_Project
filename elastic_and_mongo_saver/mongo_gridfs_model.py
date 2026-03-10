from gridfs import GridFS
from pymongo import MongoClient
from bson.objectid import ObjectId
from service_configs import ServiceConfigurations


class GridFSStorage:
    def __init__(self, mongo_uri: str, mongo_db_name: str):
        self.mongo_uri = mongo_uri
        self.mongo_db_name = mongo_db_name
        self.mongo_gridfs = None
        self.get_grid_fs()

    def get_grid_fs(self):
        client = MongoClient(self.mongo_uri)
        db = client[self.mongo_db_name]
        grid_fs = GridFS(db)
        return grid_fs

    def save_in_gridfs(self, bin_file: bytes, id: str):
        if self.mongo_gridfs is None:
            self.mongo_gridfs = self.get_grid_fs()
        self.mongo_gridfs.put(bin_file, _id=id)
        return f"\nfile_id of the uploaded File: {id} \n"