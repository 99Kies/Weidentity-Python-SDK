import requests
import logging
class Base(object):
    def __init__(self, host, port, version):

        self.HOST = host
        self.PORT = port
        self.version = version
        if "://" in host:
            if host[-1] == "/":
                host = host[:-1]
            entity = host.split("/")[2].split(":")
            host = entity[0]
            self.HOST = host
            port = int(entity[1])
            self.PORT = port
        if not isinstance(port, int):
            raise TypeError("port must be an instance of int")
        self.BASEURL = "http://{host}:{port}".format(host=host, port=port)

    def get(self, url, params=""):

        response = requests.get("{BASEURL}{url}".format(BASEURL=self.BASEURL, url=url), params=params)
        if response.status_code >= 400:
            LOG.warning('create charging_rule error: %s:%s', response.status_code, response.text)
            return None
        return response.json()

    def post(self, url, data):

        response = requests.post("{BASEURL}{url}".format(BASEURL=self.BASEURL, url=url), json=data)
        if response.status_code >= 400:
            LOG.warning('create charging_rule error: %s:%s', response.status_code, response.text)
            return None
        return response.json()