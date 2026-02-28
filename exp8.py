a=input("enter string:")
v="aeiouAEIOU"
for letter in a:
    if letter in v:
        print("it contains vowel")
        break
else:
    print("it doesn't contain vowels")
