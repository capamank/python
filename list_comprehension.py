squares=[]
for i in range(6):
    print(i*i)

sq=[i*i for i in range(6)]    
print(sq)
list=[i*i for i in range(6) if i%2!=0]
print(list)