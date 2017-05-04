#UWA PCS Practice Tournament
# By Aden Huen

#Check if string s1 is an anagram of string s2

import sys

broken = False

x = sys.stdin.readline()
s1 = x.strip('\n')

x = sys.stdin.readline()
s2 = x.strip('\n')

while(True):
  if len(s1) != len(s2):
    print("NO")
    break
      
  if len( set(s1) - set(s2) ) != 0:
    print("NO")
    break
  
  for i in set(s1):
    broken = False
    if s1.count(i) != s2.count(i):
      print("NO")
      broken = True
      break
  if broken == True:
      break
  print("YES")
  break