import jsondb




v = JSDB.JSDB("a5")

#v.Open()

'''
 #Insert
for i in range(1,100):
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
    #if(o.age <= 24 and o.age >20):
    print(f"Name={o.name} | Age = {o.age} ",end="\n" )


#oo = v.asObject(db)
#print(oo[0].name)
