import secrets
import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation
allChars = lower + upper + digits + special
password = ""

pwLen = int(input("How long should the password be? "))
minUpper = int(input("Minimum Upper Case: "))
minLower = int(input("Minimum Lower Case: "))
minDigits = int(input("Minimum Numbers: "))
minSpec = int(input("Minimum Special: "))

for i in range(minUpper):
    password += "".join(random.choice(secrets.choice(upper)))

for i in range(minLower):
    password += "".join(random.choice(secrets.choice(lower)))

for i in range(minDigits):
    password += "".join(random.choice(secrets.choice(digits)))

for i in range(minSpec):
    password += "".join(random.choice(secrets.choice(special)))

remaining = pwLen - minLower - minUpper - minDigits - minSpec

for i in range(remaining):
    password += "".join(random.choice(secrets.choice(allChars)))

password = list(password)
random.shuffle(password)
print("".join(password))
