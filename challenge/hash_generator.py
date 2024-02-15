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

from hashlib import sha256


def _string_tolist(text):
    list_text = list(text)
    list_text_ascii = [ord(x) for x in list_text]
    return list_text_ascii


def _hast256(list_ascii):
    n_characters = len(list_ascii)
    list_multiplied = [x * n_characters for x in list_ascii]
    sum_to_hash = sum(list_multiplied)

    hast_result = sha256(str(sum_to_hash))

    return hast_result


def create_password(text):
    list_ascii = _string_tolist(text)
    hash_value = _hast256(list_ascii)
    return hash_value


if __name__ == "__main__":
    print(create_password("CitricSheep"))
