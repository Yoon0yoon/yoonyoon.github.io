import http.server
import ssl
 
portnum = 4443
ipaddress = '0.0.0.0'
server_address = (ipaddress, portnum)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile='cert.pem', ssl_version=ssl.PROTOCOL_TLS)
 
print("starting https with port %d" % portnum)
 
httpd.serve_forever()
