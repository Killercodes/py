# writing string matching 
```py

a = """
Heck is here optional, provides a 4-10x speedup in String Matching, though may result in differing
It uses Levenshtein Distance to calculate the differences between
"""
b = "FThis is sample It uses Levenshtein Distance to calculate the differences between sequences in a simple-to-use package."

class StringMatching:
    def __init__(self,destinationString):
        self.String = destinationString

    
        
    def Compare(self,source):
        Rank = 0
        Matching = 0
        source_split = source.split()
        destination_split = self.String.split()

        for ss in source_split:
            for ds in destination_split:
                if ss.lower() == ds.lower():
                    Rank += 1

    
        MatchingPercentage = Rank /len(source_split) * 100
        #Rank_Destination = len(destination_split)
        #print("source.length = {},  b = {}".format(len(source_split),len(destination_split)))
        #print(" {} = {}".format(Rank_Source,Rank_Destination))
        #print("Matching % = {}, Matches = {}".format(Matching,Rank))
        return MatchingPercentage


    
#in_d = input("Enter the sentence : ")

file = open("abcd.txt","r")
for l in file:
    if len(l) > 0:
        sm = StringMatching("http://website:5555/AppWebServices/ImportJob.asmx")
        percent = sm.Compare(l)
        print("{} {}".format(percent,l))

```
