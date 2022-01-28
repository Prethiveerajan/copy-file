#devolped by : Prethiveerajan P
#reg no:21500340
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
    for line in firstfile:
             secondfile.write(line)