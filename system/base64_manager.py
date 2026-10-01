# QJR Base64 Utility
import base64

def base64_encode(text: str) -> str:
    # encode a text in to Base64
    text_bytes = text.encode("utf-8")
    encoded_bytes = base64.b64encode(text_bytes)

    return encoded_bytes.decode("utf-8")


def base64_decode(encoded_text: str) -> str:
    # decode text from Base64 to the regular text
    encoded_bytes = encoded_text.encode("utf-8")
    decoded_bytes = base64.b64decode(encoded_bytes)

    return decoded_bytes.decode("utf-8")


# additional API-functions for bytes

def base64_encode_bytes(data: bytes) -> bytes:
    # encode bytes in to Base64 bytes
    return base64.b64encode(data)


def base64_decode_bytes(data: bytes) -> bytes:
    # decode Base64 bytes
    return base64.b64decode(data)


# usage example
if __name__ == "__main__":
    text = "QJRdesktop 5.5"

    encoded = base64_encode(text)
    print("Encoded ->", encoded)

    decoded = base64_decode(encoded)
    print("Decoded ->", decoded)
