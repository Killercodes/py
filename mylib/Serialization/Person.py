class Person:
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def show(self,greet):
        print(f"{greet}, {self.fname} {self.lname}")

