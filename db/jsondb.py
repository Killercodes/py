import json



class dataset:
    def __init__(self,dict1):
        self.__dict__.update(dict1)
    

class JSDB:
    'JSON DATABASE'
    
    dbfile = "default.jsdb"
    

    def __init__(self,filename):
       JSDB.dbfile = filename + ".jsdb"

            
    def getall(self):
        fobj = open(JSDB.dbfile,"r") 
        dat = fobj.read()
        datfmt = str(dat[:-2]) #remove last 2 character
        mdb = json.loads("["+datfmt+"]")
        fobj.close()
        return json.loads(json.dumps(mdb),object_hook=dataset) #convert mdb to object

    def get(self):
        fobj = open(JSDB.dbfile,"r") 
        dat = fobj.read()
        datfmt = str(dat[:-2]) #remove last 2 character
        mdb = json.loads("["+datfmt+"]")
        #print(mdb)
        fobj.close()
        return mdb #string

    def insert(self,dic):
        fobj = open(JSDB.dbfile,"a+")
        json_object = json.dumps(dic,indent = 2)
        fobj.write(json_object + ",\n")
        fobj.close()

    def asObject(self,dic1):
        return json.loads(json.dumps(dic1),object_hook=dataset)

    def loadRaw(self,rawdata):
        output = f"[{rawdata}]"
        return output 

