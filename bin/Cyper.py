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

def Secure(dic):
    for k in dic:
        val = str(dic[k])
        encoded_data = val #base64.b64encode(val.encode())
        enval = CRYPT(k,encoded_data)
        dic[k] = enval

        #print(f"{k} = {val} = {enval}")
        #print(dic[k])

    return dic

def UnSecure(dic):
    for k in dic:
        val = str(dic[k])
        decoded_data = val #base64.b64decode(val.decode())
        deval = CRYPT(k,decoded_data,encrypt=False)
        dic[k] = deval

        #print(f"{k} = {val} = {deval}")
        #print(dic[k])

    return dic

def Test():
    d = {"name":"Vinod Srivastav","Address":"bangalore india","Age":123}

    print("ENCODE")
    for i in range(0,10):
        d = Secure(d)
        print(f"EL {i} = ",d)
    print("ENCODED ",d)

    print("DECODE")
    for i in range(0,10):
        d = UnSecure(d)
        print(f"EL {i} = ",d)
    print("DECODED ",d)

#print(d1)
#d2 = Secure(d1)
#print(d2)
