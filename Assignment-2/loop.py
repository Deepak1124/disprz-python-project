def has_repeated_characters(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False

def check_repeated_characters():
    arr = ["aab", "abc", "def"]
    for str in arr:
        print(has_repeated_characters(str))

check_repeated_characters()