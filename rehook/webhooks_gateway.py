import requests

from .webhook import WebhookCollection, Webhook


class WebhooksGateway:
    def __init__(self, gateway):
        self.gateway = gateway

    def list(self):
        req = requests.Request(method='GET',
                               url=self.gateway.get_url('webhooks/'))
        resp = self.gateway.send(req)
        data = resp.json()
        webhooks = WebhookCollection()
        for item in data:
            webhooks.append(Webhook(item))
        return webhooks

    def retrieve(self, id):
        req = requests.Request(method='GET',
                               url=self.gateway.get_url(f'webhooks/{id}/'))
        resp = self.gateway.send(req)
        data = resp.json()
        webhook = Webhook(data)
        return webhook

    def delete(self, id):
        req = requests.Request(method='DELETE',
                               url=self.gateway.get_url(f'webhooks/{id}/'))
        resp = self.gateway.send(req)
        return resp.status_code in [200, 202, 204]
