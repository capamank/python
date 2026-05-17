# import os
f=open("data.txt","w")
# data=f.read()
# readlie=f.readline()
# # print(data)
# print(readlie)
writes=f.write("this is a overwritten text in the write mode")
# print(type(data))
print(writes)
f.close()
with open ("data.txt","a") as f:
    f.write("\nthis is a text for appending the new text")
# os.remove("del_sample.txt")   
o=open("newfile.txt","x") 
    