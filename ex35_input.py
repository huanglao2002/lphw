import re
int_number = str(input("please input a int number:"))
value = re.compile(r'[0-9]+')
result = value.match(int_number)
if result:
    print ("Number is a int.")
else:
    print ("Number is not a int.")

# try exception
