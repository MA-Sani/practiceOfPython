
                         #FOR LOOPs

for i in range(10) :
    print("Dum")
    i=i+1
# Printing sets
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in a :
    print(item)

# break starement
for i in range(5) :
    i = int(input("Enter a number : "))
    if i==0 :
        break
    else:
        print("you enter : " , i)


# Continue statement
for i in range(5) :
    if i==0 :
        continue
    print(i+1)





                       #While LOOPs
i = 0
while i < 10 :
    print(i)
    i+=1

while True :
    num = int(input("Entert a number : "))
    if num == 0 :
        break


print("program Ends!!!")
