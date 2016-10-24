from paste import deploy
from paste import httpserver

#def server_factory(global_conf, host, port):
#    def serve(app):
#        s = Server(app, host=host, port=port)
#        s.serve_forever()
#    return serve

app = deploy.loadapp('config:/root/demo/paste.ini')
httpserver.serve(app, '192.168.10.159','8080')
