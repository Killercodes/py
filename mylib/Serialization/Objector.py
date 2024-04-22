import pickle


class Objector:

    def __init__(self,filename ) -> None:
        self.filename = filename

    def toBin(self,obj):
        with open(self.filename,"wb") as f:
            pickle.dump(obj,f)

    def toObj(self):
        # Open the file in read-binary mode
        with open(self.filename, "rb") as f:
            # Load the object from the file
            obj = pickle.load(f)
            
        return obj 
    
