import hashlib
import inspect

inspect.getfullargspec(hashlib.new)
inspect.FullArgSpec(args=['name', 'data'], varargs=None, varkw='kwargs', defaults=(b'',),
                    kwonlyargs=['usedforsecurity'], kwonlydefaults={'usedforsecurity': False}, annotations={})

print("**************Ethical Hacking ******************")

# Here we check if the password
# was found or not
Password_found = 0

Input_hash = input("Enter the password in the hashed form :")

Password_doc = input("\nEnter passwords filename including path(root / home/):")

try:
    # We try to open the password from
    # the given path where we have stored
    # the password.txt file with the list of passwords
    # in the read format
    Password_file = open(Password_doc, 'r')
except:
    print("ErrorFoundInPath:")
    print(Password_doc, "is not found.\nPlease enter the file path correctly again.")
    quit()

# comparing the input_hash with the hashes
# of the words in password file,
# and finding password.

for word in Password_file:
    # we encode the word in the utf-8 format
    Encoded_word = word.encode('utf-8')
    # encode the string
    str = "Ishita Sarkar"
    Encoded_str = str.encode()

    # we change the word into a hash word using the md5 format
    hash_word = hashlib.md5(Encoded_word.strip())

    # create a sha1 hash object initialized with the encoded string
    hash_obj = hashlib.sha1(Encoded_word)

    # we digest the hash word into a hexadecimal word
    digestNew = hash_word.hexdigest()

    # convert the hash object to a hexadecimal value
    hexa_value = hash_obj.hexdigest()

    if digestNew == Input_hash:
        # now we compare the hashes to see if the passwords match or not
        print("Password found.\nThe password is:", word)
        Password_found = 1
        break
    elif hash_obj == Input_hash:
        # now we compare the hashes to see if the passwords match or not
        print("\n", hexa_value, "\n")


# if the passwords were not found in
# the password.txt file
if not Password_found:
    print("Password is not found in the", Password_doc, "file")
    print('\n')
print("***************** Please visit us again**********************")
