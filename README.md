## Files
- `encrypt.py`: Encrypts plaintext with an XOR cipher (random or provided).
- `decrypt.py`: Decrypts ciphertext using an XOR cipher (random or provided).
## Usage
- `encrypt.py`: python encrypt.py "plaintext" israndom "key(if not random) resultformat(base64, hex)" (e.g. python encrypt.py "Hello" true hex, python encrypt.py "Hello" false "Test" base64)
- `decrypt.py`: python decrypt.py "ciphertext" israndom "key" (e.g. python decrypt.py "784f4d387e" true "302a215411", python decrypt.py "HAAfGDs=" false "Test")
- Random keys are always returned in a hexidecimal format
