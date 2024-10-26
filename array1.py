arr = []
n = int(input("Enter size of array :"))
for i in range(0,n):
    ele = int(input())
    arr.append(ele)

print(arr)
sum =0
for i in range(0, len(arr)):
    sum = sum + arr[i]

print(sum)

max =0
for i in range(0, len(arr)):
    if arr[i] > max:
        max=arr[i]

print(max)
        
