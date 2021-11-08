#! /usr/bin/env python3
import os
import math
from haesh.util import HaeshKeyGenerator
from haesh.haesh import Haesh
from pyaes.aes import AESModeOfOperationCBC

import argparse

BLOCK_SIZE = 16

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file_path", help="File path whose hash we want to generate", type=str)
parser.add_argument("-t", "--text", help="Text to hash. Use this instead of std input. File path will take precedence if specified", type=str)
parser.add_argument("-p", "--password", help="Extra passwrod/ salt to add for extra protection", type=str)

args = parser.parse_args()

file_path = args.file_path
text = args.text

data = file_path or text

if not file_path and not text:
    raise ValueError("Either a file path or some text needs to be provided.")

# for file path, validate that the file exists..
if file_path and not text:
    if not os.path.isfile(file_path):
        raise ValueError("File path provided does not exist.")

salt = args.password or "haesh-haesh-haes"

file_byte_array = None

# initialize objects
haesh_key_generator = HaeshKeyGenerator(file_path=file_path, text=text)
haesh = Haesh()

key = None
if file_path:
    key = haesh_key_generator.get_file_signature_key()
    hex_content = b''
    with open(file_path, 'rb') as file:
        file_byte_array = file.read()

elif text:
    key = haesh_key_generator.get_text_signature_key()

# make sure salt is 16 bytes long, cut it if it's too long and
# pad it if it's too short
if len(salt) < BLOCK_SIZE:
    required = BLOCK_SIZE - len(salt)
    salt += b'0'*required
elif len(salt) > BLOCK_SIZE:
    salt = salt[0:BLOCK_SIZE]

aes_cbc = AESModeOfOperationCBC(key, salt)

byte_data = file_byte_array or text
no_of_blocks = math.ceil(len(byte_data)/BLOCK_SIZE)

for block_index in range(no_of_blocks):
    block = byte_data[block_index*BLOCK_SIZE:BLOCK_SIZE+(block_index*BLOCK_SIZE)]
    # pad the last block that may not be 16 butes long
    if len(block) < BLOCK_SIZE:
        required = BLOCK_SIZE - len(block)
        block += b'0'*required
    aes_cbc.encrypt(block)
    haesh.calculate_digest(aes_cbc._last_cipherblock)

print(haesh.get_hex_digest())
