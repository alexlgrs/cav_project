import http.server

PORT = 80
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
max([2,3])
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
httpd.serve_forever()