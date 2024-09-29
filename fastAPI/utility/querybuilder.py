class QueryBuilder:

    def query_for_update(self, request, record):

        request = request.dict()

        filtered_request = {key: val for key, val in request.items() if val is not None
                            and not (key == 'Emp_Marital_Status' and val == 'N')}

        list_collection = []

        for key, value in record.items():
            
            for dict_key, dict_value in value.items():

                for key1, value1 in filtered_request.items():

                    if dict_key == key1 and key1 != 'Emp_Id':

                        if key1 == 'Emp_Phone' or key1 == 'Emp_Personal_Phone':

                            collection_data = {'$set': {f'{key1}': int(value1)}}

                        elif key1 == 'Emp_Skills':

                            collection_data = {'$set': {f'{key1}': value1}}

                        else:

                            collection_data = {'$set': {f'{key1}': f'{value1}'}}
                        
                        list_collection.append({key: collection_data})

        return list_collection
