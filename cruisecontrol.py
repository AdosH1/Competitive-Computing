#Google Code Jam Round 1B 2017 Q(A)
# Available @ https://code.google.com/codejam/contest/8294486/dashboard
# By Aden Huen

#Small solution only

f = open("A-large.in","r")
g = open("ans.txt", "w")

maxCase = int(f.readline().strip('\n'))
Case = 1


while Case <= maxCase:
    line = f.readline()
    line = line.rstrip("\n")
    tDistance = int(line.split(" ")[0])
    nHorses = int(line.split(" ")[1])
    fastest = 0
    index = 0
    
    hDist = []
    hSpd = []
    for i in range(int(nHorses)):
        a = f.readline().strip('\n')
        a = a.split(" ")
        #Horse spawn dist : horse speed
        if a != ['']:
            hDist.append(a[0])
            hSpd.append(a[1])
        
    for i in range(int(nHorses)):
        tmp = tDistance - int(hDist[i])
        tmp /= float(hSpd[i])
        if tmp > fastest:
            fastest = tmp
            index = i
        
    val = round(tDistance / fastest, 6)

    g.write("Case #"+ str(Case) + ": " + str(val) + "\n")
    Case += 1
        
f.close()
g.close()
    