import hashlib
import inspect

inspect.getfullargspec(hashlib.new)
inspect.FullArgSpec(args=['name', 'data'], varargs=None, varkw='kwargs', defaults=(b'',),
                    kwonlyargs=['usedforsecurity'], kwonlydefaults={'usedforsecurity': False}, annotations={})

print("**************Ethical Hacking ******************")

# Here we check if the password
# was found or not
Password_Found = 0

Input_hash = input("Enter the password in the hashed form :")

Password_Doc = input("\nEnter passwords filename including path(root / home/):")

try:
    # We try to open the password from
    # the given path where we have stored
    # the password.txt file with the list of passwords
    # in the read format
    Password_File = open(Password_Doc, 'r')
except:
    print("ErrorFoundInPath:")
    print(Password_Doc, "is not found.\nPlease enter the file path correctly again.")
    quit()
finally:
    print("We have used  finally here successfully ")
