from .resource import Resource


class Webhook(Resource):
    """
    {
        "id": "wh_abc123",
        "scheme": "http",
        "path": "/test",
        "method": "GET",
        "query_params": "",
        "remote_address": "1.2.3.4",
        "remote_host": "",
        "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Cookie": "",
            "Pragma": "no-cache",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.5",
            "X-Forwarded-For": "1.2.3.4",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https",
        },
        "encoding": null,
        "post_data": {},
        "date": "2019-11-12T17:37:56.010680Z"
    },
    """
    pass


class WebhookCollection(list):
    pass
