#طريقة تعريف الفنكشن
def printName(name):
    print(f'Hello {name}')

printName('Mohammed Mshal')

#إرجاع قيمة من الفنكشن
def sum_num(num1,num2):
    reslutNum =num1 + num2
    return reslutNum

print(sum_num(2,5))

#مثال اخر التحقق من ان العدد زوجى
def evenNumber(num):
    resultNum = num % 2 == 0
    print(resultNum)

evenNumber(9)
#مثال اخر للتحقق من ان الارقام يوجد بها رقم زوجى أو لا
def isNumsEven(numList):
    for num in numList:
        if num % 2 == 0:
            return True
    return False

print(isNumsEven([1,3,5,7,6]))

#مثال اخر لوضع قيمة التحقق داخل متغير
eventResult=[]
def getEven(event):
    for eventL in event:
       if(eventL % 2 == 0):
        eventResult.append(eventL)
getEven([1,3,2,5,7,6,8,12,14,15,15])
print(eventResult)
