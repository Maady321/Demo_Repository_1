#Problem Statement:
#Find the Grades from the user input for the marks.
#Let "X" be marks obtained through input.
#Write a program to check if the mark falls in the below mentioned range.
#A -> 100 to 80
#B -> 60 to 79
#C -> 50 to 59
#D -> 40 to 49
#lesser than 40 - Fail
#Sample Input:
#77
#Sample output:
#B
marks = int(input("Enter your marks: "))
if marks >= 80 and marks <= 100:
    print("A")
elif marks >= 60 and marks <= 79:
    print("B")
elif marks >= 50 and marks <= 59:
    print("C")
elif marks >= 40 and marks <= 49:
    print("D")
else:
    print("Fail")