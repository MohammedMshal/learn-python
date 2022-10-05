

#كتابة فانكشن لحساب حجم الكرة
def vol(r):
    pi = 13.14
    return 4/3 * pi * r**3

#كتابة فانكش تتحق من العدد المدخل ضمن الرينج أم لا
def check_rang(num,low,high):
    return num in range(low,high+1 )

#حساب عدد الاحرف الكابتل والسمول
st = 'Hello Mr. Faris, hope you are good at this fine Friday.'
upper = 0
lower = 0
all_char = 0
for char in st:
    all_char += 1
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

#فلترة الليست من الأرقام المكررة وإرجاعها كليست

list_num = [1,1,1,1,2,2,2,3,3,3,3]
def uniqe_list(alist):
    return list(set(alist))

#ضرب الأرقام التى بداخل الليست وطباعتها
numlst = [2,3,5,-10]
def mul_num(lst):
    res_num = 1
    for num in lst:
        res_num *= num
    return res_num
print(mul_num(numlst))