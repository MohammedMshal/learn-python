from functools import reduce
myList = [1,2,3,4,5,6,7,8,9,10]
myList_name = ['Mohammed','ahmed','fady','sarah','shimaa','abdo']
def squre(num):
    return num ** 2

result_num1 = []

for num in myList:
    result_num1.append(squre(num))
print(result_num1)

result_num2 = []
for item in map(squre,myList):
    result_num2.append(item)
print(result_num2)

result_num3 = list(map(squre,myList))
print(result_num3)
#هنا قمنا بإستخدام الماب ولامبادا لاختصار الكود
result_num4 = list(map(lambda num: num ** 2,myList))
print(result_num4)

def check_even(num):
    return num % 2 == 0

for item in myList:
    print(check_even(item))

#سنقوم بإستخدام الفلتر
#المثال الأول سنقوم بفلترة الارقام الزوحية
print(list(filter(lambda num: num % 2 == 0,myList)))
#المثال الثانى سنقوم بفلترة الاسماء التى تحتوى على خمسة أحرف فقط
print(list(filter(lambda name: len(name) <= 5, myList_name)))

#reduce
#هذه بالطريقة العادية
total=0
for num in myList:
    total += num
print(total)
#هنا سنستخدم الريديوس
print(reduce (lambda total,num:total +  num ,myList,0))
#مثال أخر اولاً سنستخدم ا لطريقة العادية
mul = 1
for num in  myList:
    mul *= num
print(mul)
#هنا سنستخدم الريديوس\
print(reduce(lambda total,num:total * num,myList,1))