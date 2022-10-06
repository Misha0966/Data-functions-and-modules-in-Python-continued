N = int(input('Введите натуральное число N: '))
lst = []
for i in range(2,N + 1):
    if N % i == 0:
        count = 1
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
            lst.append(i)
print(lst)