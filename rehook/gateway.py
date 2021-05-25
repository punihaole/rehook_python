import requests

from .webhooks_gateway import WebhooksGateway


class RehookGateway:
    def __init__(self, host='dev-webhooks.rocketreach.co', port=443):
        if port == 443:
            self.schema = 'https'
        else:
            self.schema = 'http'
        self.host = host
        self.port = port
        self.session = requests.Session()
        self.webhooks = WebhooksGateway(self)

    def send(self, req: requests.Request):
        preq = req.prepare()
        res = self.session.send(preq)
        return res

    def get_url(self, path):
        return f'{self.schema}://{self.host}:{self.port}/{path}'
