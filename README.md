# Introduction
Python bindings for the rehook service. Lets you retrieve webhooks that have been recently run (e.g. Braintree sandbox notifications).

# Installation
python setup.py install

# Usage
List most recent webhooks: `RehookGateway().webhooks.list()`
Retrieve a specific webhook: `RehookGateway().webhooks.retrieve('wh_abc123')`

```
>>> from rehook.gateway import RehookGateway
>>> RehookGateway().webhooks.list()
[<Webhook id: 'wh_k9tbplxnv6gb', scheme: 'http', path: '/test', method: 'GET', query_pa... 4334369744, <Webhook id: 'wh_i8w4ng6lyx9m', scheme: 'http', path: '/test', method: 'GET', query_pa... 4334369808, <Webhook id: 'wh_1c81lnixylmra', scheme: 'http', path: '/webhook/test', method: 'POST'... 4334369872, <Webhook id: 'wh_3u14r9s17mjak', scheme: 'https', path: '/braintree/notification/', me... 4334369936, <Webhook id: 'wh_2nnbz85ahlqpp', scheme: 'https', path: '/braintree/notification/', me... 4334370000, <Webhook id: 'wh_51gwfdq4qpld', scheme: 'https', path: '/braintree/notification/', met... 4334370128, <Webhook id: 'wh_2w48cqb0vxdp', scheme: 'https', path: '/braintree/notification/', met... 4334370192, <Webhook id: 'wh_1rj6853u90ha7', scheme: 'https', path: '/braintree/notification/', me... 4334370256, <Webhook id: 'wh_fv6l15l7txm6', scheme: 'https', path: '/braintree/notification/', met... 4334370320, <Webhook id: 'wh_3lwu7kog1095l', scheme: 'https', path: '/braintree/notification/', me... 4334370064, <Webhook id: 'wh_g66nlc910con', scheme: 'https', path: '/braintree/notification/', met... 4334370384, <Webhook id: 'wh_2atjwsm16yrfd', scheme: 'https', path: '/braintree/notification/', me... 4334370448, <Webhook id: 'wh_3bbh0v3n6we8w', scheme: 'https', path: '/braintree/notification/', me... 4334370512, <Webhook id: 'wh_29mz2odw6ffnk', scheme: 'https', path: '/braintree/notification/', me... 4334370576, <Webhook id: 'wh_eyurehopyg7c', scheme: 'https', path: '/braintree/notification/', met... 4334370640, <Webhook id: 'wh_nwx5v865esaw', scheme: 'https', path: '/braintree/notification/', met... 4334370704, <Webhook id: 'wh_38l3gfz2rbhjf', scheme: 'https', path: '/braintree/notification/', me... 4334370768, <Webhook id: 'wh_cz3xr6nihi6d', scheme: 'https', path: '/braintree/notification/', met... 4334374992, <Webhook id: 'wh_1qwk73nlyoziy', scheme: 'https', path: '/braintree/notification/', me... 4334375056, <Webhook id: 'wh_3glat48lcnq07', scheme: 'https', path: '/braintree/notification/', me... 4334375120, <Webhook id: 'wh_lg4kwbs3bdv0', scheme: 'https', path: '/braintree/notification/', met... 4334375184, <Webhook id: 'wh_11qm73s1e2rgc', scheme: 'https', path: '/braintree/notification/', me... 4334375248, <Webhook id: 'wh_2sgsn156lpv27', scheme: 'https', path: '/braintree/notification/', me... 4334375312, <Webhook id: 'wh_j0zybh8b7s1g', scheme: 'https', path: '/braintree/notification/', met... 4334375376, <Webhook id: 'wh_3176tk2t6lz1c', scheme: 'https', path: '/braintree/notification/', me... 4334375440, <Webhook id: 'wh_1o0ebf8deuwsg', scheme: 'https', path: '/braintree/notification/', me... 4334375504]
>>> RehookGateway().webhooks.retrieve('wh_k9tbplxnv6gb')
<Webhook id: 'wh_k9tbplxnv6gb', scheme: 'http', path: '/test', method: 'GET', query_pa... 4334385168
```

1. You can query the webhooks headers
```
>>> webhook.headers
{'Host': 'django-env.vhkawew7qf.us-west-2.elasticbeanstalk.com', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Cookie': 'csrftoken=uUMwTjUOjTRhGXzcbKengMx2mvyjvnSCY8gQXn3heJBm0Ci64o8HXdKU1TIGkA2K; sessionid=8iwufndsd3zga0a92pro2phiddj1fqk9', 'Pragma': 'no-cache', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0', 'Cache-Control': 'no-cache', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.5', 'X-Forwarded-For': '208.185.211.138', 'X-Forwarded-Port': '80', 'X-Forwarded-Proto': 'http', 'Upgrade-Insecure-Requests': '1'}
```
2. You can query the webhooks metadata such has ip address, method, scheme.
```
>>> webhook.method
'GET'
>>> webhook.path
'/test'
>>> webhook.remote_address
'208.185.211.138'
>>> webhook.scheme
'http'
>>> webhook.date
'2019-11-12T17:37:56.010680Z'
```
3. Query the webhook data (returns a dict).
```
>>> webhook.post_data
{'param1': ['foo'], 'param2': ['bar', 'baz']}
```

