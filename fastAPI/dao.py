from datetime import datetime, date
from utility.querybuilder import QueryBuilder
from pymongo import MongoClient
import os
from dotenv import load_dotenv


class Dao:

    def __init__(self, query=None, url=None, auth_id=None, auth_key=None):
        load_dotenv()
        self.query = query or QueryBuilder()
        self.url = url or os.getenv('DB_URL')
        self.auth_id = auth_id or os.getenv('AUTH_ID')
        self.auth_key = auth_key or os.getenv('AUTH_KEY')

    def db_connection(self, auth_id, auth_key):

        try:
            
            url = self.url.replace("<auth_id>", auth_id).replace("<auth_key>", auth_key)

            connection = MongoClient(url)
            
            return connection
        
        except Exception as er:
            
            raise er

    def db_create(self, collections, request):
        
        try:
            
            connection = self.db_connection(self.auth_id, self.auth_key)

            db = connection['Employee']

            request_dict = request.dict()

            for field, value in request_dict.items():
                
                if isinstance(value, date):  # Correct usage
                    
                    request_dict[field] = datetime.combine(value, datetime.min.time())

            for collection_name, fields in collections.items():

                collection = db[collection_name]

                record = {field: request_dict[field] for field in fields}

                collection.insert_one(record)

            connection.close()

            return '{"message": "Record Successfully Inserted!!!"}'
        
        except Exception as er:
            
            raise er

    def db_retrieve(self, collections, request):
        
        try:
            records = {}

            connection = self.db_connection(self.auth_id, self.auth_key)

            db = connection['Employee']

            for collection_name in collections.items():

                collection = db[collection_name[0]]

                result = collection.find_one({'Emp_Id': request.Emp_Id})

                result.pop('_id', None)

                records[f'{collection_name[0]}'] = result

                # records.append(result)

            connection.close()

            return records
        
        except Exception as er:

            raise er

    def db_update(self, collections, request):

        try:
            
            record = self.db_retrieve(collections, request)
            
            collections_for_update = self.query.query_for_update(request, record)

            for list_collection in collections_for_update:

                for collection_name, collection_value in list_collection.items():

                        connection = self.db_connection(self.auth_id, self.auth_key)

                        db = connection['Employee']
                        
                        collection = db[collection_name]
                        
                        query = {"Emp_Id": request.Emp_Id}
                        
                        collection.update_one(query, collection_value)

                        connection.close()

            return '{"message": "Record Successfully Updated!!!"}'
        
        except Exception as er:

            raise er

    def db_delete(self, collections, request):

        try:

            connection = self.db_connection(self.auth_id, self.auth_key)

            db = connection['Employee']

            for collection_name in collections.items():

                collection = db[collection_name[0]]

                collection.find_one_and_delete({'Emp_Id': request.Emp_Id})

            connection.close()

            return '{"message": "Record Deleted Successfully!!!"}'
        
        except Exception as er:

            raise er
