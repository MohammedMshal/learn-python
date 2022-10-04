#اللوب مع المتغيرات

name ='Mohammed Mshal'
for names in name:
    print(names)

#اللوب مع الليست
nameList = ['Mohammed','Mahmoud','Ahmed','Mshal']
for nameLists in nameList:
    print(nameLists)

#اللوب مع الدكشنرى
nameDic = {
    'name':'Mohammed Mahmoud Ahmed Mshal',
    'age':22,
    'barthDay':'9/9/1999'
}

for nameDics in nameDic.values():
    print(nameDics)

#for (var) in (List-Value-Dectionaries,other...)
#for (var) in rang(start,end,step)

#تكرار الامر
for x in range(5):
    print('test print range method')
    #لإضافة امر بعد إنتهاء اللوب من تنفيذ الكود الذى بالأعلى
else :
    print('end for loop')

#عندما يتحقق الشرط سوف يوقف اللوب
numList = [1,2,3,4,5]
for num in numList:
   if num > 3:
    break
   print(num)


# يوقف اللوب بإعادة اللوب للعمل من البداية
numList = [1,2,3,4,5]
for num in numList:
   if num > 3:
    continue
   print(num)

#عندما نريد كتابة اللوب ولكن نريد تركه فارغاً وتأجيله لاحقا

for num in numList:
    pass

#while loop
#var
num = 1
while num <= 10:
    num +=1
    if(num == 3):
        continue
    print( f'num = {num}')

#lists
myList = [1,2,3,4,5]
myList2 = []
index = 0
while index < len(myList):
    print(myList[index])
    index += 1

print('========================================================')
while myList:
    #عندما نريد حفظ العناصر من بداية  الليست نضع بين الأقواس (0)
    item = myList.pop(0)
    print(item)

print('============================================')
num2 = 1
while num2 <= 20:
    if(num2 == 10):
        break
    num2 += 1
    print(num2)