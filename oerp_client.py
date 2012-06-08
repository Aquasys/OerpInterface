import xmlrpclib

from oerp_model import OerpModel
from oerp_query import OerpQueryManager


class OerpClient:
    """
    Creates the connection to OpenERP and handles queries
    """


    def __init__(self, username, password, db, url):
        self.username = username
        self.password = password
        self.db = db
        self.url = url

        self.get_uid()
        self.get_proxy()


    def get_uid(self):
        """
        UID is needed for queries
        """

        proxy = xmlrpclib.ServerProxy(self.url + "common")
        uid = proxy.login(self.db, self.username, self.password)
        self.uid = uid


    def get_proxy(self):
        """
        Gets the proxy used for queries
        """
        proxy = xmlrpclib.ServerProxy(self.url + "object", allow_none=True)
        self.proxy = proxy


username = 'admin'
password = 'pass'
db = 'dev'
url = 'http://localhost:8069/xmlrpc/'   

client = OerpClient(username, password, db, url)
query_manager = OerpQueryManager(client)
#partners = query_manager.filter(name="Machin", _module="res.partner")
#partner = query_manager.get(2, _module="res.partner")
partner = {
   'name': 'Vincent Prouillet'
}
model = OerpModel('res.partner', partner)
model2 = OerpModel('res.partner', partner)
testing = [model, model2]

#test = query_manager.delete(testing)
#print test
