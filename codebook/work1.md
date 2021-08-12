

# Print Your code here
```py
from random import randint

a = """Lorem ipsum dolor sit amet\n
consectetur adipiscing elit

sed do eiusmod #tempor incididunt
ut labore et dolore magna aliqua."""

dictionary = "and Sed do this is word magna"
dictionary = dictionary.lower()
words= a.split();
print(type(words))

rank = []

for l in words:
    if dictionary.find(l) > 0:
    	rank.insert(1,l)
        
##print(words[randint(0, len(words))])    
print(rank)
```

## second example
```py
thisdict =	{
  "brand": "Ford;Maruti;nissan",
  "model": "Mustang",
  "year": "1964"
}


def getQuote(word):
	
    wrd = thisdict[word]
    if len(wrd) > 1:
        return wrd
    else:
        return wrd 
    
for q in getQuote("brand").split(";"):
    print(q)
```    
