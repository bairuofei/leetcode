import bisect

a=[1,2,4]
b=bisect.bisect_left(a,1.2)
bisect.insort(a,3)
print(a)
print(b)