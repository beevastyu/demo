import falcon
import json

class Resource:
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
        ('/', Resource())
        ]

def app_factory(global_conf, **local_conf):
    print 'Creating WSGI app...'
    # Create the REST API
    api = falcon.API()
    # Register the URIs
    for route, resource in endpoints:
        api.add_route(route, resource)
    return api
