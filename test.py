#نستعملها عندما نريد وضع عدد لانهائى من البراميترات
def sumNum(*args):
    return(sum((args)))

result_num = sumNum(3,6,2,7,8)
print(result_num)

#مثال عندما نريد وضع عدد لا نهائى من الراميترات على شكل {مفتاح  , قيمة}
def myfunc(**kwargs):
    print(kwargs)
    for item in kwargs:
        print(f'{item} is {kwargs[item]}')

myfunc(name='mohammed',age=22,brath_day='sptamper')

