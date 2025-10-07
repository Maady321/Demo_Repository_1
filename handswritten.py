#find the greatest on from the three number from users
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#c = int(input("Enter third number: "))

#if a > b and a > c:
  #  print("The greatest number is:", a)
#elif b > a and b > c:
 #   print("The greatest number is:", b)
#else:
  #  print("The greatest number is:", c)


#a = int(input("enter the number: "))

#x = (a/100)*10
#y = (a/100)*5


#if a >= 1000:
 #  print (a-x)

#elif a >= 500  and a < 1000:
 #  print(a-y)

#elif a < 500 :
 #  print ('No discount')

#x = int(input("enter the x: "))
#y = int(input("enter the y: "))
#if x > 0 and y > 0:
#    print("1st Quadrant ")
#elif x < 0 and y > 0:
 #   print("2nd Quadrant ")
#elif x < 0 and y < 0:
#    print("3rd  Quadrant ")
#elif x > 0 and y < 0 :
# print("4th Quadrant ")
 
#else:
 #    print( "centre")
month = int(input(' enter the number'))

match month:
    case 1:
      print("january")

    case 2:
      print('February')  
    
    case 3:
      print('march')
    
    case 4:
      print('april')

    case 5:
      print('may')

    case 6:
      print('june')

    case 7:
      print('july')

    case 8:
      print('august')

    case 9:
      print('september')

    case 10:
      print('october')

    case 11:
      print('november')

    case 12:
      print('december')

  case _:
    print('Invalid month number')
      