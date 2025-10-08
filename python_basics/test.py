#find the sum of all even number upto n using a while loop
n=int(input("Enter a number: "))
a = 1
sum = 0
while a <= n:
    if a % 2 == 0:
        sum = sum + a
    a = a + 1
print(sum)
