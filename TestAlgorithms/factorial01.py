def interative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
        return fact
print( interative_factorial(5))

def restive_factorial (n):
    if n == 1:
        return n
    else:
        temp = restive_factorial(n - 1)
        temp = temp*n
        return temp
print(restive_factorial(4))


def permute(string, pocker = ""):
    if len(string) == 0:
        print(pocker)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front+back
            permute(together,letter+pocker)
print(permute("abc",""))
