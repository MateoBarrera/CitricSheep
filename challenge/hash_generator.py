"""Citric Sheep Challenge for Python Software Developer

  Hash generator 

  Summary:
  - Start with the string "CitricSheep". 
  - Use the ASCII values of each character in the string and generate a list of these values.
  - Multiply each value in the list by the number of characters in the string.
  - Find the sum of all numbers in the resulting list.
  - Use this sum to generate a SHA256 hash.
  - Convert this hash to a hexadecimal string.
"""

import hashlib


def string_to_list_ascii(text):
    """
    The string_to_list_ascii function takes a string as input and returns a list of the ASCII values for each character in the string.

    :param text: Get the string that will be converted to a list of ascii values
    :return: The list of the ascii values of each character in a string
    :doc-author: Trelent
    """
    list_text = list(text)
    list_text_ascii = [ord(x) for x in list_text]
    return list_text_ascii


def hash_generator(list_ascii):
    """
    The hash_generator function takes a list of ASCII values as input and returns the SHA256 hash of the sum
    of each ASCII value multiplied by the length of the list. This is done to ensure that if two lists have different
    lengths, they will not produce identical hashes.

    :param list_ascii: Pass the list of ascii values to the function
    :return: A hash of the sum of the ascii values multiplied by their position in the string
    :doc-author: Trelent
    """
    n_characters = len(list_ascii)
    list_multiplied = [x * n_characters for x in list_ascii]
    sum_to_hash = str(sum(list_multiplied))
    h = hashlib.sha256(str.encode(sum_to_hash))
    return h.hexdigest()


def encrypt_password(text):
    """
    The encrypt_password function takes a string as input and returns the hash value of that string.
    The function first converts the string to a list of ASCII values, then uses those values to generate
    a hash value using the SHA256 algorithm.

    :param text: Pass the string that is going to be encrypted
    :return: The hash value of the text
    :doc-author: Trelent
    """
    list_ascii = string_to_list_ascii(text)
    hash_value = hash_generator(list_ascii)
    return hash_value


if __name__ == "__main__":
    print(encrypt_password("CitricSheep"))
