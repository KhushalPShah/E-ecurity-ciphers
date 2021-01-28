ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL_CHARS = " ,.-;:_?!="

# def encrypt(plain_text, key):
#     """
#     Encrypts plaintext using a caesar.

#     :param plain_text:  The plaintext
#     :param key: The key (Integer)
#     :return: The cipher-text
#     """
#     cipher_text = ""
#     for letter in plain_text:
#         if letter in SPECIAL_CHARS:
#             cipher_text += letter
#             continue
#         index = ALPHABET.find(letter.upper())
#         new_index = flatten(index + key)
#         cipher_text += ALPHABET[new_index]
#     return cipher_text

def decrypt(cipher_text, key=None):
    """
    This function decrypts plaintext. If no key is specified, it 
    will be found using distribution analysis.
    :param cipher_text: The cipher-text
    :param key: The key
    :return: the plain-text
    """
    if key is None:
        keys = find_key_from_cipher(cipher_text)
        print(keys)
    texts = []
    for key in range(0,26):
        plain_text = ""
        for letter in cipher_text:
            #Skipping special characters (incomplete solution)
            if letter in SPECIAL_CHARS:
                plain_text += letter
                continue
            index = ALPHABET.find(letter.upper())
            new_index = flatten(index - key)
            plain_text += ALPHABET[new_index]
        texts.append(plain_text)
    return texts

def flatten(number) :
    """
    Flattens the key back to be in range(1,26)
    :param number: 
    :return: 
    """
    return number - (26*(number//26))


def find_key_from_cipher(cipher_text):
    index_of_most_common_letter = 19 #Index of 'e'

    #Calculate distribution
    distribution_dict = analyse_letter_distribution(cipher_text)
    #Get common letters
    common_letters = sorted(distribution_dict, key=distribution_dict.get, reverse=True)
    #Use most common letter to get key
    keys = []
    for i in range(0,26):
        keys.append(ALPHABET.find(common_letters[0].upper()) - i)
    return keys

def analyse_letter_distribution(cipher_text):
    distribution_dict = {}
    for letter in cipher_text:
        if letter in SPECIAL_CHARS:
            continue
        if letter not in distribution_dict:
            distribution_dict[letter] = 1
        else:
            distribution_dict[letter] += 1
    if len(distribution_dict.values()) != len(distribution_dict.values()):
        print("Multiple letters appear the same amount of times! Uh oh.")
    return distribution_dict


if __name__ == "__main__":
    texts = decrypt("VGFLX GJYWL LGTMQ LZWLA UCWLK LGLZW UGFUW JL")
    i = 0
    for text in texts:
        print(i, text)
        i = i + 1