char = ["","!","*","#","$","%","&","'","(",")","\"","+",",",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<",">","=","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\","]","^","_","-","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","}","|","~"]
#num = int(input("How long is the longest password variation: "))
print("It will create all the combinations up to 8 character long passwords B-)")
word2 = ""
##    while a < num:
##        word = ""
##        a+=1
##        for i in char:
##            b = 0
##            while b < a:
##                word = word + i
##                f.write(word+"\n")
##                b+=1

##    for a in char:
##        word = ""
##        word+=a
##        for b in char:
##            word+=b
##            for d in char:
##                word+=d
##                for c in char:
##                    word+=c
##                    f.write(word+"\n")
##                    break
##                for i in char:
##                    word+=i
##                    for i in char:
##                        word+=i
##                        for i in char:
##                            word+=i
##                            for i in char:
##                                word+=i
##                                for i in char:
##                                    word+=i
##                                    for i in char:
##                                        word+=i
##                                        for i in char:
##                                            word+=i
file = open("./comb.txt", "w")
word = ["","","","","","","",""]
for a in range(len(word)):
    for b in char:
        word[0] = b
        for c in char:
            word[1] = c
            for d in char:
                word[2] = d
                for e in char:
                    word[3] = e
                    for f in char:
                        word[4] = f
                        for g in char:
                            word[5] = g
                            for h in char:
                                word[6] = h
                                for j in char:
                                    word[7] = j
                                    for i in word:
                                        word2 = word2+i
                                        file.write(word2+"\n")
file.close()
print("Now it's waiting just for you ;)")
