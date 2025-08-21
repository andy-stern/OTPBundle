import os
import base64
import sys
from typing import Tuple

def formatresult(data: str, mode: str):
    if mode == "base64":
        return base64.b64encode(data).decode()
    elif mode == "hex":
        return data.hex()
    else:
        return "Invalid resultformat."

def randomencrypt(plaintext: str) -> Tuple[bytes, bytes]:
    key = os.urandom(len(plaintext))
    plaintextbytes = plaintext.encode()
    ciphertextbytes = bytes([c ^ k for c, k in zip(plaintextbytes, key)])
    return ciphertextbytes, key

def keyencrypt(plaintext: str, key: str) -> bytes:
    plaintextbytes = plaintext.encode(()
    keybytes = key.encode()
    ciphertextbytes = bytes([c ^ keybytes[i % len(keybytes)] for i, c in enumerate(plaintextbytes)])
    return ciphertextbytes

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Pass arguments in the format of python xxx.py \"Text\" israndom \"key(if not random)\" resultformat(base64, hex)")

    text = sys.argv[1]

    israndom = sys.argv[2].lower()
    if israndom == "true":
        israndom = True
    elif israndom == "false":
        israndom = False
    else:
        print("Random status must be a boolean.")
        sys.exit(1)
    
    if not israndom:
        key = sys.argv[3]
        ciphertext = keyencrypt(text, key)
        resultformat = sys.argv[4]
        formatted = formatresult(ciphertext, resultformat)
        print(formatted)
    else:
        ciphertext, key = randomencrypt(text)
        resultformat = sys.argv[3]
        formatted = formatresult(ciphertext, resultformat)
        print("\x1B[3mEncrypted text:\x1B[0m " + formatted)
        print("\x1B[3mKey:\x1B[0m " + key.hex())
