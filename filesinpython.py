fp = open("cobra.txt","r")
wr = open("cobra.txt","a")

#print(fp.read()) #will read whole
#print(fp.readline())will read 1 lnie
#print(fp.readlines()) output bbc\n bbc \n
#print(fp.read(5)) #this will read 5 bytes from file space is a byte remembe !!!
#print(wr.write("Ihaten yoggerrs")) #prints the number inside 
#wr.write("python is mid \n")
#print(fp.readline(500))
# wr.close()
#print(fp.readlines())
#wr.write("python is mid \n") if i run this withouth opening this will give an error  since the file is already closed

print("Pointer position beofre reading is:",
fp.tell())
print(fp.read())
fp.seek(6)
print("Pointer position beofre reading is:",
fp.tell())