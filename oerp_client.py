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


    def search(self, module, args):
        """
        Returns list of ids satisfying the args
        """
        return self.proxy.execute(self.db, self.uid, self.password, module, 'search', args)


    def create(self):
        partner = {
           'name': 'Fabien Pinckaers'
        }
        class Partner:
            def __init__(self):
                self.name = "oulalala"
        partner = Partner()
        partner_id = self.proxy.execute(self.db, self.uid, self.password, 'res.partner', 'create', partner)
        print partner_id


    def select(self):
        fields = ['name'] #fields to read
        ids = [4, 5]
        data = self.proxy.execute(self.db, self.uid, self.password, 'res.partner', 'read', ids, fields)
        machin = OerpModel('res.partner', data[0])

        print machin.object


username = 'admin'
password = 'pass'
db = 'dev'
url = 'http://localhost:8069/xmlrpc/'   

client = OerpClient(username, password, db, url)
query_manager = OerpQueryManager(client)
#partners = query_manager.filter(name="Machin", _module="res.partner")
partner = query_manager.get(2, _module="res.partner")
print partner.object.name