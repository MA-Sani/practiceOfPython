               # Writing file
# Method 1
s = "Sani is good guy"
with open("text.txt", "w") as f:
    f.write(s)

# Method 2
fp = open("text.txt", "w")
fp.write(s)
fp.close()



               # Reading file

# Method 1
with open("text.txt", "w") as f:
    s = f.read()
    print(s)

# Method 2
f = open("text.txt" , "w")
s = f.read()
print(s)
f.close()


                # Appending File

with open("text.txt", "a") as f:
    s = f.write("Moazzam Ali Sani is my full name")