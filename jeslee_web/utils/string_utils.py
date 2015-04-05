import base64


def encode(key, string):
    """
    return: an encode string using 'Vigenere cipher'.
    The returned string can be decoded using string_utils.decode(key, string) function.
    """
    encoded_chars = []
    for i, c in enumerate(string):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(c) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)


def decode(key, string):
    """
    return: the decoded string using 'Vigenere cipher'
    The string must be encoded with string_utils.encode(key, string) with the exact same key.
    """
    ori_str = base64.urlsafe_b64decode(string)
    decoded_chars = []
    for i, c in enumerate(ori_str):
        key_c = key[i % len(key)]
        decoded_c = chr(ord(c) - ord(key_c) % 256)
        decoded_chars.append(decoded_c)
    return "".join(decoded_chars)
    """

    """
