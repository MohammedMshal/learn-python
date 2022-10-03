#السيت يمكن تخزين بها عدة قيم ولكن لا تدعم التسلسل 
#ايضا السيت لا يمكن ان يحتوى على قيم مكرره
mySet = {
    1,
    'two',
    3,
    'four'
}

print(mySet)
#يمكن تحويل السيت الى ليست كالآتى
myList = [1,3,'three']
newSet = set(myList)
print(newSet)
#يمكن إضافة عنصر  إلى السيت من كالآتى
mySet.add('six')
print(mySet)