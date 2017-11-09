
import six.moves.urllib.request as request

class OrcClient(object):

    def __init__(self, api_root):
        self._api_root = api_root

    @property
    def api_root(self):
        return self._api_root

    @property
    def http_client(self):
        return self._http_client

    def discovery(self, instance, port):
       request.urlopen("http://10.71.84.90:3000/api/discover/127.0.0.1/3306")




