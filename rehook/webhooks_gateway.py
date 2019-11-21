from collections import defaultdict

import requests

from .webhook import WebhookCollection, Webhook


class WebhookCursor:
    def __init__(self, gateway, query_params={}):
        self.gateway = gateway
        self.query_params = query_params
        self.start_page = 1
        self.size = 10

    def __iter__(self):
        self.page = self.start_page
        while True:
            items = self.gateway.list(self.page, self.size, self.query_params)
            if items is None:
                break
            for item in items:
                yield item
            self.page += 1

    def __getitem__(self, key):
        items = self.gateway.list(self.start_page, self.size, self.query_params)
        return items[key]


class WebhooksGateway:
    def __init__(self, gateway):
        self.gateway = gateway

    def iterator(self):
        return WebhookCursor(self)

    def list(self, page=1, page_size=10, query_params={}):
        params = {'page': page, 'page_size': page_size}
        params.update(query_params)
        req = requests.Request(method='GET',
                               url=self.gateway.get_url('webhooks/'),
                               params=params)
        resp = self.gateway.send(req)
        if resp.status_code == 200:
            data = resp.json()
            webhooks = WebhookCollection()
            for item in data['results']:
                webhooks.append(Webhook(item))
            return webhooks
        elif resp.status_code == 404:
            return None

    def search(self):
        s = WebhookSearch(self)
        return s

    def execute_search(self, s):
        return WebhookCursor(self, s.query)

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


class WebhookSearch:
    def __init__(self, webhook_gateway):
        self.gateway = webhook_gateway
        self._facets = defaultdict(list)

    @property
    def query(self):
        return dict(self._facets)

    def __copy__(self):
        return self._clone()

    def _clone(self):
        s = self.__class__(self.gateway)
        s._facets = self._facets.copy()
        return s

    def filter(self, **kwargs):
        s = self._clone()
        for k, v in kwargs.items():
            s._facets[k].append(v)
        return s

    def execute(self):
        return self.gateway.execute_search(self)
