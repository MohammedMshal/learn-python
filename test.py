#يمكن التعامل مع الملفات من خلال هذه الدالة ويتم إنشاء الملف بشكل اتوماتيكى فى موق ع الملف
myFile = open('C:\\Users\\moham\\Desktop\\learn python\\test.txt','rt')
#لقراءة الملف
print(myFile.read())
#لإعادة بدء الملف الأول
myFile.seek(0)
#لقراءة جزء من الملف
print(myFile.read(4))
myFile.seek(0)
#لقراءة الملف كسطر واحد فقد
print(myFile.readline())
myFile.seek(0)
#لقراءة الملف كأسطر
print(myFile.readlines())
myFile.seek(0)
#للحصول على الملف كليست والتعديل عليه
myLits= []
for line in myFile:
    myLits.append(line.strip())

print( f'my list is {myLits}')
myFile.close()

with open('test.txt') as myFile2:
    data = myFile2.read()

print(f'my file 2 is \n {data}')



#get path (pwd)
#open location path (ls)