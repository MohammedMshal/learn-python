#إختبار طباعة الكلمة التى أولها حرف الأس
st1 = 'print only the words that starts with s in this sentence like Sam'
for word in st1.split():
    if(word[0].lower() == "s"):
        print(word)
#طباعة الارقام الزوجية بإستخدام رانج
print(list(range(0,11,2)))
#طباعة الأرقام من واحد إلى خمسين التى تقبل القسمة على ثلاثة
reslutNum = [num for num in range(51) if num % 3 == 0]
print(reslutNum)
#طباعة الكلمات التى عدد أحرفها زوجية
st2 = 'print every word in this sentence that has an even number of letters'
for word in st2.split():
    if(len(word) % 2 == 0):
        print(f'{word} is Even')

#عمل ليست تحتوى على اول حرف من كلمة
st3 = 'create a list of the first letters of every word in this sentence'

resultList = [word[0] for word in st3.split()]
print(resultList)