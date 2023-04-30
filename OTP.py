import random
char="0987654321"
otp=""
for i in range(0,6):
    num=random.choice(char)
    otp=otp+num

print(otp)
