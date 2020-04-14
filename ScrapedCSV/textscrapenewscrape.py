import socket
import ssl
import sys


def shift(b, c):
 for i in range(len(b) - 1):
  b[i] = b[i + 1]

 b[-1] = c[0]

def scrape(relative):
 domain = "www.sec.gov"

 with socket.create_connection((domain, 443)) as old_sock:
  with ssl.create_default_context().wrap_socket(old_sock, server_hostname =
   domain) as sock:
   sock.send((
"GET /Archives/%s HTTP/1.0\r\n" % relative +
"Host: %s\r\n\r\n" % domain
 ).encode())
   output = b""
   target = b"\r\n\r\n"
   buffer = bytearray(b"\0" * len(target))

   while buffer != target:
    shift(buffer, sock.recv(1))

   while True:
    target = b"<FILENAME>"
    buffer = bytearray(b"\0" * len(target))
    broken = False

    while buffer != target:
     c = sock.recv(1)

     if not c:
      broken = True
      break

     shift(buffer, c)

     if c == b"<":
      while c != b">":
       c = sock.recv(1)
       shift(buffer, c)
     else:
      output += c

    if broken:
     break

    c = sock.recv(1)
    output += c
    filename = b""

    while c != b"\n":
     filename += c
     c = sock.recv(1)
     output += c

    target = b"<TEXT>\n"
    buffer = bytearray(b"\0" * len(target))

    while buffer != target:
     c = sock.recv(1)
     shift(buffer, c)

     if c == b"<":
      while c != b">":
       c = sock.recv(1)
       shift(buffer, c)
     else:
      output += c

    target = b"</TEXT>"
    buffer = bytearray(b"\0" * len(target))

    if filename[-4 :] in (b".txt", b".htm"):
     while buffer != target:
      c = sock.recv(1)
      shift(buffer, c)

      if c == b"<":
       while c != b">":
        c = sock.recv(1)
        shift(buffer, c)
      elif c == b"&":
       while c != b";":
        c = sock.recv(1)
        shift(buffer, c)
      else:
       output += c
    else:
     while buffer != target:
      c = sock.recv(1)
      shift(buffer, c)

   return output

#print(scrape("edgar/data/1124198/0001104659-13-037604.txt").decode())

# import socket
# import ssl
# import sys

# def scrape(relative):
#  domain = "www.sec.gov"

#  with socket.create_connection((domain, 443)) as old_sock:
#   with ssl.create_default_context().wrap_socket(old_sock, server_hostname =
#    domain) as sock:
#    sock.send((
# "GET /Archives/%s HTTP/1.0\r\n" % relative +
# "Host: %s\r\n\r\n" % domain
#  ).encode())
#    output = ""
#    target = "\r\n\r\n"
#    buffer = "\0" * len(target)

#    while buffer != target:
#     buffer = buffer[1 :] + sock.recv(1).decode()

#    while True:
#     target = "<FILENAME>"
#     buffer = "\0" * len(target)
#     broken = False

#     while buffer != target:
#      c = sock.recv(1).decode()

#      if not c:
#       broken = True
#       break

#      buffer = buffer[1 :] + c

#      if c == "<":
#       while c != ">":
#        c = sock.recv(1).decode()
#        buffer = buffer[1 :] + c
#      else:
#       output += c

#     if broken:
#      break

#     c = sock.recv(1).decode()
#     output += c
#     filename = ""

#     while c != "\n":
#      filename += c
#      c = sock.recv(1).decode()
#      output += c

#     target = "<TEXT>\n"
#     buffer = "\0" * len(target)

#     while buffer != target:
#      c = sock.recv(1).decode()
#      buffer = buffer[1 :] + c

#      if c == "<":
#       while c != ">":
#        c = sock.recv(1).decode()
#        buffer = buffer[1 :] + c
#      else:
#       output += c

#     target = "</TEXT>"
#     buffer = "\0" * len(target)

#     if filename[-3 :] in ("txt", "htm"):
#      while buffer != target:
#       c = sock.recv(1).decode()
#       buffer = buffer[1 :] + c

#       if c == "<":
#        while c != ">":
#         c = sock.recv(1).decode()
#         buffer = buffer[1 :] + c
#       else:
#        output += c
#     else:
#      while buffer != target:
#       c = sock.recv(1).decode()
#       buffer = buffer[1 :] + c

#    return output
   
# #print(scrape('edgar/data/1124198/0001104659-13-037604.txt'))