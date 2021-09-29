x = input("Enter a sentence that is the same forwards and backwards  ")
print("Your sentence is:\n'{}'".format(x))

l = ((int(len(x))) + 1 )
print(l)

a = x[0:]
b = x[(l):None:-1]
print(a)
print(b)

if a == b:
    print("Your sentence is a palindrome.")
elif a != b:
    print("Your sentence is NOT a palindrome.")
else:
    pass




# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
