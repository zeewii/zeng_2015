f = open('/home/zeng/test',"r+")
f.seek(2)
a = '5\n'
f.write(a)
f.close()
f = open('/home/zeng/test')
for i in f.readlines():
    print i
f.close()