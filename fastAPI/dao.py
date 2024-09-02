from datetime import datetime, date

from pymongo import MongoClient
from fastAPI.utility import constants as const
import os


# "mongodb+srv://boobeish123:R9C6K8QBwIKOmYg0@cluster0.1loch.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# "mongodb+srv://<auth_id>:<auth_key>@cluster0.1loch.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# auth_id
# auth_key
# db
# collection
# DB_URL="mongodb+srv://<auth_id>:<auth_key>@cluster0.1loch.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";AUTH_ID=boobeish123;AUTH_KEY=R9C6K8QBwIKOmYg0

class Dao:

    def __init__(self, url=None, auth_id=None, auth_key=None):
        # self.query = query or QueryBuilder()
        self.url = url or os.getenv('DB_URL')
        self.auth_id = auth_id or os.getenv('AUTH_ID')
        self.auth_key = auth_key or os.getenv('AUTH_KEY')

    def db_activity(self, request, operation):
        try:

            connection = self.db_connection(self.auth_id, self.auth_key)

            collections = const.collection_mappings

            if operation == 'C':
                create_response = self.db_create(connection, collections, request)
                return create_response
            elif operation == 'R':
                retrieve_response = self.db_retrieve(connection, collections, request)
                return retrieve_response
            elif operation == 'U':
                update_response = self.db_update(connection, collections, request)
                return update_response
            elif operation == 'D':
                delete_response = self.db_delete(connection, collections, request)
                return delete_response
            else:
                raise "Invalid operation code"
        except Exception as er:
            raise er

    def db_connection(self, auth_id, auth_key):
        try:
            url = self.url.replace("<auth_id>", auth_id).replace("<auth_key>", auth_key)
            print(url)
            connection = MongoClient(url)
            print("inside db_connection")
            # db = connection['Employee']
            return connection
        except Exception as er:
            raise er

    def db_create(self, connection, collections, request):
        try:
            db = connection['Employee']
            print("inside db_create")
            request_dict = request.dict()

            for field, value in request_dict.items():
                if isinstance(value, date):  # Correct usage
                    request_dict[field] = datetime.combine(value, datetime.min.time())

            for collection_name, fields in collections.items():
                print(collection_name)
                # print(fields)
                collection = db[collection_name]
                # print(collection)
                record = {field: request_dict[field] for field in fields}
                print(record)
                collection.insert_one(record)
            connection.close()
            return '{"message": "Record Successfully Inserted"}'
        except Exception as er:
            raise er

    def db_retrieve(self, connection, collections, request):
        try:
            # db = connection['Employee']
            # for collection_name, fields in collections.items():
            #     collection = db[collection_name]
            #     record = {field: request[field] for field in fields}
            #     collection.insert_one(record)
            connection.close()
            return True
        except Exception as er:
            raise er

    def db_update(self, connection, collections, request):
        try:
            # db = connection['Employee']
            # for collection_name, fields in collections.items():
            #     collection = db[collection_name]
            #     record = {field: request[field] for field in fields}
            #     collection.insert_one(record)
            connection.close()
            return True
        except Exception as er:
            raise er

    def db_delete(self, connection, collections, request):
        try:
            # db = connection['Employee']
            # for collection_name, fields in collections.items():
            #     collection = db[collection_name]
            #     record = {field: request[field] for field in fields}
            #     collection.insert_one(record)
            connection.close()
            return True
        except Exception as er:
            raise er
