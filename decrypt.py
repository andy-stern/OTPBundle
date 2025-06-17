import sys
import base64
import binascii

def convertciphertext(ciphertext: str) -> bytes:
    if all(c in "0123456789abcdefABCDEF" for c in ciphertext) and len(ciphertext) % 2 == 0:
        try:
            return bytes.fromhex(ciphertext)
        except ValueError:
            pass

    try:
        return base64.b64decode(ciphertext, validate=True)
    except (binascii.Error, ValueError):
        pass

    return None


def randomdecrypt(ciphertextbytes: bytes, key: bytes) -> str:
    plaintextbytes = bytes([c ^ k for c, k in zip(ciphertextbytes, key)])
    return plaintextbytes.decode("utf-8")

def keydecrypt(ciphertextbytes: bytes, key: str) -> str:
    keybytes = key.encode("utf-8")
    plaintextbytes = bytes([b ^ keybytes[i % len(keybytes)] for i, b in enumerate(ciphertextbytes)])
    return plaintextbytes.decode("utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Pass arguments in the format of python xxx.py \"Ciphertext\" israndom \"key\" ")
        sys.exit(1)

    ciphertext = convertciphertext(sys.argv[1])
    if ciphertext is None:
        print("Invalid ciphertext format.")
        sys.exit(1)

    israndom = sys.argv[2].lower()

    key_str = sys.argv[3]

    if israndom == "true":
        try:
            key = bytes.fromhex(key_str)
        except ValueError:
            print("Invalid key format.")
            sys.exit(1)

        decrypted = randomdecrypt(ciphertext, key)
        print(decrypted)
    elif israndom == "false":
        decrypted = keydecrypt(ciphertext, key_str)
        print(decrypted)
    else:
        print("Random status must be a boolean.")
        sys.exit(1)