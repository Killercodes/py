import json


class dataset:
    def __init__(self,dict1):
        self.__dict__.update(dict1)

    
    

class JSDB:
    'JSON DATABASE'
    #db = ""
    dbfile = "default.jsdb"
    #fileobj = ""

    def __init__(self,filename):
       JSDB.dbfile = filename 

    #def Open(self):
    #    JSDB.fileobj = open(JSDB.dbfile,"a")
            
    def getall(self):
        fobj = open(JSDB.dbfile,"r") 
        dat = fobj.read()
        datfmt = str(dat[:-2]) #remove last 2 character
        mdb = json.loads("["+datfmt+"]")
        #print(mdb)
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



v = JSDB("a4.txt")
#v.Open()
'''
for i in range(1,1024):
    nm = f"vinod {str(i)}"
    data = {'name':nm,'age':i, 'details':{'adress':'address '+str(i), 'street':'st 1','zip': '560037' }}
    print(type(data))
    v.insert(data)

'''
db = v.get()
#print(db)

for d in db:
    #print(d)
    o = v.asObject(d)
    #print(o.name)
    if(o.age <= 24 and o.age >20):
        print(f"Name={o.name} | Age = {o.age} ",end="\n" )


#oo = v.asObject(db)
#print(oo[0].name)
