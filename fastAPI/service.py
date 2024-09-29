from dao import Dao
from utility import constants as const


class Service:

    def __init__(self):
        self.dao = Dao()

    def service_call(self, request):

        try:

            collections = const.collection_mappings

            if request.Operation_Cd == 'C':

                response_from_dao = self.dao.db_create(collections, request)

            elif request.Operation_Cd == 'R':
                
                response_from_dao = self.dao.db_retrieve(collections, request)

            elif request.Operation_Cd == 'U':
                
                response_from_dao = self.dao.db_update(collections, request)

            elif request.Operation_Cd == 'D':
                
                response_from_dao = self.dao.db_delete(collections, request)

            else:
                
                raise "Invalid operation code"
            
            return response_from_dao
        
        except Exception as er:
            
            raise er
