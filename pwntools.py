#!/usr/bin/env python3

from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


while True:
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    encoding = received["type"]
    value = received["encoded"]
    decoded = null

    if encoding == "base64":
        decoded = base64.b64decode(value).decode() #
    elif encoding == "hex":
        decoded = codecs.decode(value, "hex").decode()
    elif encoding == "rot13":
        decoded = codecs.encode(value, 'rot_13') # works!
    elif encoding == "bigint":
        decoded = codecs.decode(value[2:], "hex").decode()
    elif encoding == "utf-8":
        decoded = ''.join([chr(b) for b in value]) #

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)
