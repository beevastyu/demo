import socket
from paste import deploy
from paste import httpserver

cfg = 'paste.ini'
host = socket.gethostbyname(socket.gethostname())
port = 8080

app = deploy.loadapp('config:' + cfg, relative_to = '.')
httpserver.serve(app, host, port)
