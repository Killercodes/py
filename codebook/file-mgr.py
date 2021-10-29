
#class FILE:
READ = "r"
APPEND = "a"
WRITE = "w"
CREATE = "x"
TEXT = "t"
BINARY = "b"
    

#def FILE(name,fileattrib):
#    return open(name,fileattrib)





class TextFile:
    def __init__(self,file,atttrib="r"):
        self.FileName = file
        self.FileAttribute = atttrib
        self.Data = open(self.FileName,"r")

    def ForRead(self):
        self.Data = open(self.FileName,"r")
    def ForAppend(self):
        self.Data = open(self.FileName,"a")
    def ForWrite(self):
        self.Data = open(self.FileName,"w")
    def CreateNew(self):
        self.Data = open(self.FileName,"a")
    def Close(self):
        self.Data.close()

    def ReadLine(self):
        self.Data.readline()
    def ReadLines(self):
        self.Data.readlines()
        
""""
    def ReadFile(self):
        self.Data.read()

    def ReadFile(self,numChars):
        self.Data.read(numChars)

    

    
"""





