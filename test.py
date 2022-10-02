from operator import ne


listName = [1, 'two', 3]
listNum2 = [4, 'five, 6']
#يمكن دمج متفيرين من نوع ليست 
newNumList = listName + listNum2
print(newNumList)
#يمكن الحصول على او طباعة جزء من الليست
print(listName[:2:])
#طريقة إضافة عنصر الى الليست
newNumList.append('Siven')
print(newNumList)
# إضافة عنصر معين الى الليست من خلال الانديكس
newNumList.insert(0,'Zero')
print(newNumList)
#حذغ عنصر معين من الليست من خلال اسم العنصر
newNumList.remove('Siven')
#حذغ عنصر معين من الليست والحصول عليه داخل متغير
resultList = newNumList.pop(2)
print(resultList)
#حذف عنصر معين من الليست من خلال الانديكس
del newNumList[0]
print(newNumList)
#حذف الليست بالمتفير 😂
#del newNumList
#حذف العناصر التى بداخل الليست بالكامل
newNumList.clear()
print(newNumList)
num = [3,6,1,5,2]
#ترتيب العناصر التى جاخل الليست من الاصغر الى الاكبر
num.sort()
print(num)
#عكس عناصر الليست
num.reverse()
print(num)

