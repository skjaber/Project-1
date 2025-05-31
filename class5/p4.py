try:
 x = int(input("Please enter a number: "))
 result = 10 / x
except ValueError:
 print("Invalid input; please enter a number.")
except ZeroDivisionError:
 print("You cannot divide by zero.")
finally:
 print("This executes no matter what.")



a=int(input("enter a= "))
b=int(input("enter b= "))

leargest = max(a,b)
print(leargest)
