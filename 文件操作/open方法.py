f = open('./test',"r+")
f.seek(2)
a = '2\n'
f.write(a)
f.close()

f = open('./test')
#for i in f.readlines():
    #print i
print f.read()
f.close()