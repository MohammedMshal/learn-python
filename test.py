
#list comprehension
#هى تقوم بوضع المتغير داخل ليست بطريقة مبسطه
#var
names = 'Mohammed Mshal'
resultName = [name for name in names]
print(f'nameString = {resultName}')

#numbers(int)

resultNum = [num for num in range(10)]
print(f'numList = {resultNum}')

#طباعة ارقام زوجية وإستخدام الدالة الشرطية داخل الليست

resultNum2 = [num for num in range(20) if num%2 == 0]
print(f'reslutNumTwo: {resultNum2}')

#استخدام الدالة الشرطية كاملة داخل الليست

resultNum3 = ['Even' if num%2 ==0 else 'ODD' for num in range(10)]
print(f'reslutNumThree: {resultNum3}')

#طرب عناصر الليست الأولى فى الثانية او عملية اخرى بطريقة مختصرة

myList1 = [1,2,3,]
myList2 = [100,200,300,]
reslutListNum = []
for x in myList1:
    for x2 in myList2:
        reslutListNum.append (x * x2)

print (f'reslutListNum{reslutListNum}')

#الطريقة
reslutListNum2 = [x * y for x in myList1 for y in myList2]
print(f'reslutListNum: {reslutListNum}')
