import base64

def decode(string):
    string_into_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(string_into_bytes)
    base64_decoded = base64_bytes.decode('ascii')

    return base64_decoded

def encode(string):
    result = base64.b64decode(string).decode('ascii')
    return result

print("Zaszyforwany:", decode("Hej"))

print("Odszyfrowany:", encode("SGVq"))




