# Una de las características diferentes en Python es que el "else if" pasa a ser "elif".

total = int(input('How much money do you have in your pocket\n'))

if total > 100:
    print("Give me your money!")
elif total > 50:
    print("Buy me some coffee you cheap!")
else:
    print("You are a poor guy, go away!")