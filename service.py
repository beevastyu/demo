import socket
from paste import deploy
from paste import httpserver

cfg = 'paste.ini'
host = socket.gethostbyname(socket.gethostname())
port = 8080

#def server_factory(global_conf, host, port):
#    def serve(app):
#        s = Server(app, host=host, port=port)
#        s.serve_forever()
#    return serve

app = deploy.loadapp('config:' + cfg, relative_to = '.')
httpserver.serve(app, host, port)
