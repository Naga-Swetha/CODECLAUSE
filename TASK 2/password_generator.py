import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','+']
print("***WELCOME TO RANDOM PASSWORD GENERATOR***")
letters_password=int(input("How many letters you want in your password?:\n"))
symbols_password=int(input("How many symbols you need in your password?:\n"))
numbers_password=int(input("How many numbers you need in your password?:\n"))
password_list=[]
for i in range(1,letters_password+1):
    char=random.choice(letters)
    password_list+=char
for i in range(1,symbols_password+1):
    char=random.choice(symbols)
    password_list+=char
for i in range(1,numbers_password+1):
    char=random.choice(numbers)
    password_list+=char
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password+=char
print("PASSWORD:",password)