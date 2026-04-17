# for loop

for i in range( 6):
    print(i)

#find sum

total = 0

for i in range(15):
    total = total + i
print("Total" , total)


#while loop

i = 1;
while i <=5 :
    i =i+1
    print(i)


#count down

count = 5
while count > 0:
 print (count)
 count = count -1


 print ("Done!")


 #Guess Number

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high, try a lower number")
    elif guess < secret_number:
        print("Too low, try a higher number")
    else:
        print("🎉 Yay! You found the number")




#guess Number using Attempts
number = 7
attempts = 3

while attempts > 0:
    guess1 = int(input("Enter Your Guess"))

    if guess1 == number:
        print("🎉 You win!")
        break
    else:
        print("try again")
        attempts = attempts-1


if attempts == 0:
    print("Game Over")