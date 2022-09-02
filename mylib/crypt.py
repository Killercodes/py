# cyper
import base64

def CRYPT(key, string, encrypt=True):
    '''vigenere cipher function, use (key,text) for encoding and (key,text, 'd') for decoding'''
    
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        if encrypt == True:
            encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
            res = ord(string[i]) + ord(key_c) % 256
            print(f"{ord(string[i])} + {ord(key_c)} % 256 = {res}")
        else:
            encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string
