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
#للقراءة على الملف وإغلاقة تلقائياً
#وضع الريت يتم كتابة النص مع مسح القديم وانشاء الملف ان لم يكن موجود ولا يسمح بالقراءة
with open('test.txt', 'w') as write1:
    write1.write('this is test write my file w mode')
#فى هذا الوضع يتم الكتابة على الملف بدون حذف الاسطر القديمة 
#وإذا لم يكن الملف موجود فسينم انشاءه تلقائيا
with open('test.txt' , 'a') as write2:
    write2.write('\nthis is write mode 2')

#تسمح لنا بكتابة على الملف ولكن ليس بنفس الإسم وإن كان موجود سيحدث خطأ
with open('test.txt','x') as xMode:
    xMode.write('this is x mode rite')

#تسمح لنا بالقراءة والكتابة على الملف فى نفس الوقت ولكن اذا لم يكن الملف موجود سيجدث خطأ
#يمسح المحتوى القديم ويضيف الجديد
with open('test', 'r+') as rPlusMode:
    rPlusMode.write('this is x mode rite')
    rPlusMode.seek(0)
    rPlusMode.read()
#rPlusMode عكس
#يمسح الحتوى القديم ويضيف جديد
with open('test.txt','w+') as wPlus:




#get path (pwd)
#open location path (ls)