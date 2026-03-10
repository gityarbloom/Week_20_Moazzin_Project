from elasticsearch import Elasticsearch, NotFoundError
from elasticsearch.helpers import bulk

class Elastic_MTD_Stor:
    def __init__(self, es_uri: str, index: str, es_properties: dict[str, dict[str, str]]):
        self.es = Elasticsearch(es_uri)
        self.index = index
        self.mapping = {'mappings': {'properties': es_properties}}

    def create_es_index(self):
        try:
            response = self.es.indices.create(index=self.index, body= self.mapping)
            return f"Response: {response}"
        except Exception as e:
            raise Exception(f"ElasticSearch Failed. \n{e}")
        

    def is_index_exists(self):
        try:
            response = self.es.indices.exists(index=self.index)
            return f"Response: {response}"
        except Exception as e:
            raise Exception(f"ElasticSearch Failed. \n{e}")
        

    def delete_es_index(self):
        try:
            response = self.es.indices.delete(index=self.index, body= self.mapping)
            return f"Response: {response}"
        except Exception as e:
            raise Exception(f"ElasticSearch Failed. \n{e}")


    def save_es_document(self, doc: dict):
        doc_id = doc["id"]
        response = self.es.index(index=self.index, id= doc_id, document= doc)
        return f"\nDocument is {response['result']}\n"