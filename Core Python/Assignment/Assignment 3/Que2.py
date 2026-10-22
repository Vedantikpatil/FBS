#2.Write a program to input any alphabet and check whether it is vowel or consonant.

chr=input(("Enter a alphabet:"))
if chr in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")