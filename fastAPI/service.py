from fastAPI.dao import Dao


class Service:

    def __init__(self):
        self.dao = Dao()

    def service_call(self, request):
        return self.dao.db_activity(request)
