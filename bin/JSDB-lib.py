import json



class dataset:
    def __init__(self,dict1):
        self.__dict__.update(dict1)
    
    
dbfile = "default.jsdb"


def Connect(dbfilename,mode = "r"):
        file = open(dbfilename,mode)
        return file


def Disconnect(fileObj):
        fileObj.close()

                
def Select(fobj):
        dat = fobj.read()
        datfmt = str(dat[:-2]) #remove last 2 character
        mdb = json.loads("["+datfmt+"]")
        return mdb #string                


def Insert(fobj,dic):
        json_object = json.dumps(dic,indent = 2)
        fobj.write(json_object + ",\n")

                
def GetAll(JSDBdbfile):
        fobj = open(JSDBdbfile,"r") 
        dat = fobj.read()
        datfmt = str(dat[:-2]) #remove last 2 character
        mdb = json.loads("["+datfmt+"]")
        fobj.close()
        return json.loads(json.dumps(mdb),object_hook=dataset) #convert mdb to object

def Get(JSDBdbfile):
        fobj = open(JSDBdbfile,"r") 
        dat = fobj.read()
        datfmt = str(dat[:-2]) #remove last 2 character
        mdb = json.loads("["+datfmt+"]")
        #print(mdb)
        fobj.close()
        return mdb #string

def Set(JSDBdbfile,dic):
        fobj = open(JSDBdbfile,"a+")
        json_object = json.dumps(dic,indent = 2)
        fobj.write(json_object + ",\n")
        fobj.close()

def ToObject(dic1):
        return json.loads(json.dumps(dic1),object_hook=dataset)

def loadRaw(self,rawdata):
        output = f"[{rawdata}]"
        return output 

def CRYPT(key, string, act='e'):
    '''vigenere cipher function, use (key,text) for encoding and (key,text, 'd') for decoding'''
    
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        if act=='e':
            encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        else:
            encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string


def Secure(dic):
    for k in dic:
        val = str(dic[k])
        enval = CRYPT(k,val)
        dic[k] = enval

        print(f"{k} = {val} = {enval}")
        print(dic[k])

    return dic

def UnSecure(dic):
    for k in dic:
        val = str(dic[k])
        deval = CRYPT(k,val,"d")
        dic[k] = deval

        print(f"{k} = {val} = {deval}")
        print(dic[k])

    return dic
