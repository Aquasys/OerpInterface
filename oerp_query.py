
from oerp_utils import OerpUtils
from oerp_model import OerpModel

class OerpQueryManager:
    """
    Simplifies all the queries to and from OpenERP
    """


    def __init__(self, client):
        self.client = client


    def filter(self, _module, **kwargs):
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


    def get(self, pk, _module):
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
            else:
                return None

        else:
            return None


    def create(self, oerp_objects):
        """
        Basic create enhanced, you can create several at the same time
        Name of the module is store on the __name__ of the object
        Returns the id of the newly created objects
        """
        id_list = []

        if len(oerp_objects) == 0:
            return None

        for oerp_object in oerp_objects:
            new_id = self.client.proxy.execute(self.client.db, self.client.uid, self.client.password, 
            oerp_object.object.__name__, 'create', oerp_object.to_dict())

            id_list.append(new_id)

        return id_list


    def update(self, oerp_objects):
        """
        Update an object
        Works the same as create
        Returns True if updated, False otherwise
        """
        success_list = []

        if len(oerp_objects) == 0:
            return None

        for oerp_object in oerp_objects:
            result = self.client.proxy.execute(self.client.db, self.client.uid, self.client.password, 
            oerp_object.object.__name__, 'write', oerp_object.object.id, oerp_object.to_dict())

            success_list.append(result)

        return success_list


    def delete(self, oerp_objects):
        """
        Delete the record
        Works the same as create/update
        Returns true if it worked (returns true if the object doesn't exist too)
        """
        success_list = []

        if len(oerp_objects) == 0:
            return None

        id_list = []
        for oerp_object in oerp_objects:
            id_list.append(oerp_object.object.id)
            
        result = self.client.proxy.execute(self.client.db, self.client.uid, self.client.password, 
        oerp_object.object.__name__, 'unlink', id_list)

        return result
