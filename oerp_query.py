
from oerp_utils import OerpUtils
from oerp_model import OerpModel

class OerpQueryManager:
    """
    Simplifies all the queries to and from OpenERP
    """


    def __init__(self, client):
        self.client = client


    def filter(self, _module=None, **kwargs):
        """
        Can return several objects
        Search criteria are in the kwargs 
        """
        search_criteria = OerpUtils.translate_to_search_domain(kwargs)

        ids = self.client.proxy.execute(
            self.client.db, self.client.uid, self.client.password, 
            _module, 'search', search_criteria)


        objects = self.client.proxy.execute(
            self.client.db, self.client.uid, self.client.password, 
            _module, 'read', ids)

        result = []

        for item in objects:
            result.append(OerpModel(_module, item))

        if len(result) > 0:
            return result
        else:
            return None


    def get(self, pk=None, _module=None):
        """
        Returns only the first object
        Look by id
        """

        if isinstance(pk, (int, long)):
            objects = self.client.proxy.execute(
            self.client.db, self.client.uid, self.client.password, 
            _module, 'read', pk)

            if not isinstance(objects, (list)):
                result = OerpModel(_module, objects)
                return result
            else
                return None

        else:
            return None


    def create(self, oerp_object)):
        """
        Basic create
        """
        print 'create'


    def update(self):
        """
        Update an object
        """
        print 'update'


    def delete(self):
        """
        Delete the record
        """
        print 'delete'
