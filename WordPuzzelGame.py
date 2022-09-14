from random import shuffle

words=["father", "break", "crypto", "green", "aeroplane"]
shuffle(words)
temp=[]
count=0
for i in words:
    for j in i:
        temp.append(j)

    shuffle(temp)
    print("Arrange the letters to form a valid word: ","\n",''.join(temp))
    temp.clear()
    if i==str(input("Guess the word : ")) :
        print("\n","Correct","\n")
        count+=1
    else :
        print("\n","Wrong","\n")
        count-=1

print("Net Score is ",count)