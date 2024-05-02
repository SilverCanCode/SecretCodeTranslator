
import random
def Code():
    w = input("Enter your word: ")
    if len(w) > 2:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        a = w[0]
        a2 = w[len(w) - 1]
        a3 = w[1:len(w)-1]
        a4 = a2 + a3 + a
        # print(a3)
        # print(a4)
        for i in range(1):            
            r1 = (random.choice(alphabet))
            r2 = (random.choice(alphabet))
            r3 = (random.choice(alphabet))
            con = (r1+r2+r3)
        for i in range(1):
            r4 = random.choice(alphabet)
            r5 = random.choice(alphabet)
            r6 = random.choice(alphabet)
            con2 = (r4+r5+r6)
            print(con + a4 + con2, end="")
    elif(len(w) <= 2):
        print(w[::-1])
    else:
        raise ValueError ("Enter a word containing more than 1 charecter")
    
def Decode():
    w = input("Enter the word to decode: ")
    if len(w) <= 2:
        print(w[::-1])
    elif(len(w) > 2):
        a = w[0]
        a2 = w[1]
        a3 = w[2]
        a4 = w[3]
        a5 = w[len(w) - 2]
        a6 = w[len(w) - 3: len(w)]
        con = a + a2 + a3
        print(con)
        print(a6)
        s = w.strip(a6)
        s2 = s.strip(con)
        f = s2[-1] + s2[1:-1] + s2[0]
        print(f)
    else:
        raise ValueError ("Please enter a coded word, if you don't know what is a coded word first please read the readme file.")
i = input("Do you want to code or decode: ")
if i.lower() == "code":
    Code()
elif i.lower() == "decode":
    Decode()
else:
    raise TypeError ("INVALID INPUT!")



