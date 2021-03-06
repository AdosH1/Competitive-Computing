#Google Code Jam Qualification Round 2017 Q(A)
# Available @ https://code.google.com/codejam/contest/3264486/dashboard#s=p0
# By Aden Huen

f = open("A-large.in","r")
g = open("ans.txt", "w")

maxCase = f.readline()
Case = 1

for line in f:
    input = line.rstrip('\n')
    lstr = input.split(" ")
        
    cake = lstr[0]
    
    #Get pancakes in list form ['-', '+', '+'] etc
    pcakes = []
    for i in range(0,len(cake)):
        if cake[i] == '-':
            pcakes.append(0)
        if cake[i] == '+':
            pcakes.append(1)
        #pcakes.append(cake[i])
    
    #Number of minimum pancakes to flip
    K = int(lstr[1])
    
    #set no. flips to 0
    flips = 0
    

    #check each element of pcakes
    for i in range(0,len(pcakes)):
        #This is our greedy solution, we can flip pancakes in a sliding window as needed
        #if we find a zero, flip next K
        if pcakes[i] == 0:
            #makes sure j loop doesn't go out of range
            if (i+K) <= len(pcakes):
                #flip K elements
                for j in range(i,i+K):
                    if pcakes[j] == 0:
                        pcakes[j] = 1
                    elif pcakes[j] == 1:
                        pcakes[j] = 0
                flips+=1
    
    if 0 in pcakes:
        g.write("Case #"+ str(Case) + ": " + "IMPOSSIBLE" + "\n")
        Case += 1
    else:
        g.write("Case #"+ str(Case) + ": " + str(flips) + "\n")
        Case += 1
        
f.close()
g.close()
    
            