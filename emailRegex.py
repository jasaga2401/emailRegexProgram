
import re

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

email = input("Enter an email address: ")

if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

    
