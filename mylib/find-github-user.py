
import os
#import subprocess
import itertools


def Execute(uname):
    commd = f"https://api.github.com/users/{uname}"
    github = f"{uname}.github.io"
    commd = 'curl -s -o /dev/null -w "%{response_code}" -I ' + commd
    #print(commd)
    pro = os.popen(commd)
    lines = pro.readlines()
    pro.close()
    if(int(lines[0]) != 200):
        print(f"{github} [AVAILABLE]")
        with open("gituser.txt","a") as gfile:
            gfile.write(github+"\n")
    
    #return lines
    
    
    
def Getunique():
    s1="opqrstuvwxyzabcdefghijklmn"
    res = itertools.permutations(s1,4)
    count = 0
    for r in res:
        count+=1
        word = "".join(r)
        #print(word)
        Execute(word)

#Execute("datbz")
Execute("datbz2")
Getunique()


