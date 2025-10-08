
#a = int(input("Enter the starting number: "))
#b = int(input("Enter the ending number: "))
#for i in range(a, b + 1):
 #   print(i)


#a = int(input("Enter the starting number: "))
#b = int(input("Enter the ending number: "))
#n = int(input("Enter the divisor: "))
#count= 0
#while a<=b:
 #   if a % n == 0:
  #     count = count + 1
   # a = a + 1
#print("The count = ", count)


#For  A smartwatch , you need to write a function to calculate the total stars points for a given walking steps

 # for every 1000 steps = 5 stars  
 # for every 5000th steps, bonus 20 points

def star_points(steps):
    for_1000 = steps // 1000 * 5
    for_1000 = steps // 5000 * 20
    total_points = for_1000 + for_5000
    print("total star is ", total_points)
star_points = (10000)