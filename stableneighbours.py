#Google Code Jam Round 1B 2017 Q(B)
# Available @ https://code.google.com/codejam/contest/8294486/dashboard#s=p1
# By Aden Huen

#For small input

import operator

f = open("B-small-attempt4.in","r")
g = open("ans.txt", "w")

maxCase = int(f.readline().strip('\n'))
Case = 1


while Case <= maxCase:
    line = f.readline()
    line = line.rstrip("\n")
    line = line.split(" ")
    dict = {}
    val = ""
    l = []
    prev = ""
    N, R, O, Y, G, B, V = int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6]) 
    colors = [ [R, "R"], [O,"O"], [Y,"Y"], [G,"G"], [B,"B"], [V,"V"] ]
    
    colors = sorted(colors, reverse=True)
    
    
    if max(colors)[0] > (N/2)+1:
        val = "IMPOSSIBLE"
    
    if val != "IMPOSSIBLE":
        n = N
        while n != 0:
            if prev != colors[0][1] and colors[0][0] > 0:
                l.append(colors[0][1])
                colors[0][0] -= 1
                prev = colors[0][1]
            elif prev != colors[1][1] and colors[1][0] > 0:
                l.append(colors[1][1])
                colors[1][0] -= 1
                prev = colors[2][0]
            elif prev != colors[2][1] and colors[2][0] > 0:
                l.append(colors[2][1])
                colors[2][0] -= 1
                prev = colors[2][1]
            elif prev != colors[3][1] and colors[3][0] > 0:
                l.append(colors[3][1])
                colors[3][0] -= 1
                prev = colors[3][1]
            elif prev != colors[4][1] and colors[4][0] > 0:
                l.append(colors[4][1])
                colors[4][0] -= 1
                prev = colors[4][1]
            elif prev != colors[5][1] and colors[5][0] > 0:
                l.append(colors[5][1])
                colors[5][0] -= 1
                prev = colors[5][1]
                
            n -= 1
        if val != "IMPOSSIBLE":
            for i in range(len(l)):
                val+=str(l[i])
        

    g.write("Case #"+ str(Case) + ": " + str(val) + "\n")
    Case += 1
f.close()
g.close()
    