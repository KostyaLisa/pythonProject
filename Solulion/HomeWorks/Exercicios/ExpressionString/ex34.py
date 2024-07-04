# for i in range(2, 10, 2):
#     print(i)

count=0
sum=0

for i in range(10):
    num = int(input(f"Enter integer number {i + 1}: "))
    if num%2==0:
        count+=1
        sum+=num
print(count,sum)