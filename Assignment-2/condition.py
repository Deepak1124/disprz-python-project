def is_palindrome(str):
    reversed_s = str[::-1]
    if str == reversed_s:
        print(str,"is a palindrome")
    else:
         print(str,"is a not a palindrome")   

def check_palindrome():
    arr = ["ab", "abc", "aba"]
    for str in arr:
        is_palindrome(str)

check_palindrome()