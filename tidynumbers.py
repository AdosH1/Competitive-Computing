# Google Code Jam Qualification Round 2017 Q(B)
# Available @ https://code.google.com/codejam/contest/3264486/dashboard#s=p1
# By Aden Huen

def tidyN(num):
    #We want number to be a string so we can iterate through character by character (list works too)
    N = str(num)
    tidy = False
    val=""
    
    #if length is 1, number is trivially tidy
    if len(N) == 1:
        val=N[0]
        tidy = True
        
    if tidy == False:
        val+=str(N[0])
        #checks that the numbers are in ascending order
        for i in range(0,len(N)-1):
            if int(N[i]) <= int(N[i+1]):
                val+=str(N[i+1])
                tidy = True
            else:
                #here is a greedy solution, we take the last tidy number in string and subtract 1
                # replacing the rest of the values with 9 eg. 1230432 -> 1229999
                val+=str(N[i+1])
                val=str(int(val)-1)
                for j in range(i+2, len(N)):
                    val+="9"
                tidy = False
                break
    #The greedy solution breaks on edge cases eg. 1232945 -> 1231999 is not tidy, thus we will call the function again
    # after each greedy operation to check validity
    if tidy == False:
        return tidyN(val)
    else:
        return val

#Input / Output files
f = open("B-large.in","r")
g = open("ans.txt", "w")

maxCase = f.readline()
Case = 1

for line in f:
    N = line.rstrip("\n")
    
    val = tidyN(N)

    g.write("Case #"+ str(Case) + ": " + val + "\n")
    Case += 1
        
f.close()
g.close()
    