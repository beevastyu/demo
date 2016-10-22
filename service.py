import falcon
import json

class HelloResource:
    def on_get(self, req, resp):
        res = {
                'text': 'Hello World!!',
                'method': req.method
        }
        resp.body = json.dumps(res)

    def on_post(self, req, resp):
        res = {
                'text': 'Hello World!!',
                'method': req.method
        }
        resp.body = json.dumps(res)

endpoints = [
#        ('/', Resource()),
        ('/hello', HelloResource())
        ]

# Create the REST API
api = falcon.API()

# Register the URIs
for route, resource in endpoints:
    api.add_route(route, resource)
