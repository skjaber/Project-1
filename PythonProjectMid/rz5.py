nump = int(input("Enter number : "))
is_prime = True

if nump < 2:
    is_prime = False
else:
    for i in range(2,int(nump **0.5)+1):
        if nump % i == 0:
            is_prime =False
            break

print(f"{nump} is {'a prome number' if is_prime else 'not prime number'}.")
