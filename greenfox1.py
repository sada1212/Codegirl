def average(numList):
    sumofodds=0
    count=0
    for i in numList:
        if i % 2> 0:
            sumofodds=sumofodds+i
            count=count+1
    return sumofodds/count

print (average([1,2,3,4,5]))
print (average([3,5,9,2]))
print (average([-2,3,-9]))
print (average([100,200,300,101]))
