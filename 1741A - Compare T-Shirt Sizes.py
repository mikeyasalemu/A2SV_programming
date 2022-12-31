itr = int(input())
for i in range(itr):
    words = input().split()
    ch1 = words[0][len(words[0])-1]
    ch2 = words[1][len(words[1])-1]
    if ch1 =="S" and ch2 =="S":
        if len(words[0]) > len(words[1]):
            print ('<')
        elif len(words[0]) < len(words[1]):
            print (">")
        else:
            print ("=")
    elif ch1 =="L" and ch2 =="L":
        if len(words[0]) > len(words[1]):
            print (">")
        elif len(words[0]) < len(words[1]):
            print ("<")
        else:
            print ("=")
    elif ch1 =="L" and ch2 =="M":
        print(">")
    elif ch1 =="M" and ch2 =="L":
        print("<")
    elif ch1 =="S" and ch2 =="L":
        print("<")
    elif ch1 =="L" and ch2 =="S":
        print(">")
    elif ch1 =="M" and ch2 =="S":
        print(">")
    elif ch1 =="S" and ch2 =="M":
        print("<")
    elif ch1 =="M" and ch2 =="M":
        print("=")
    

   
   
