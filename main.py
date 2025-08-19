import random
n = random.randint(1,50)

a = -1
guess = 0
while(a != n):
    a =  int(input("Enter a number:"))
    if (a > n):
        print("Lower Number please")
        guess += 1
        
    elif(a < n):
        print("Higher Number please")
        guess += 1

print(f"You have guessed the correct number {n} in {guess} attempt")