import array
val = array.array('i', [0,1,2,3,4,5,6,7,8,9])
print(val)
for i in range(0,6):
  print(val[i] , end = ' ') 

for j in val:
  print(j , end = ', ')

print(val.typecode)

# val.reverse()
# print(val)
# for i in range(len(val)-1 , -1 , -1):
#   print(val[i])

# print(val)
# val.insert(0 , 00)
# print(val)

# print(val)
# val.append(10000)
# print(val)

# print(val)
# #  overwrite data
# val[0] = 2000
# print(val)

copyarray = array.array(val.typecode , (x*2 for x in val))
# print(copyarray)
# copyarray.pop(0)
# print(copyarray)

# print(copyarray)
# copyarray.remove(8)
# print(copyarray)]]

a = array.array('i' , (x*1 for x in val))
print(a[0:5])
print(a[-1:])
print(a[-1])
print(a[0:-3])
print(a[::-1])

# arr1 = array.array('i' , [])
# n = int(input())
# for i in range(0,n):
#   x = int(input())
#   arr1.append(x)

# print(arr1)

print(a)
print(a.index(6))