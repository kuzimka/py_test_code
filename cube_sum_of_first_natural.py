def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i*i
         
    return sum
 
 
# Driver Function
n = 5
print(sumOfSeries(n))
