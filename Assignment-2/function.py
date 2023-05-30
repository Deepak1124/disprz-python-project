def check_palindrome(*strings):
    results = []
    for string in strings:
        reversed_string = string[::-1]
        is_palindrome = string == reversed_string
        results.append(is_palindrome)
    return results

def check_repeated_characters(*strings):
    results = []
    for string in strings:
        seen = set()
        has_repeated_chars = False
        for char in string:
            if char in seen:
                has_repeated_chars = True
                break
            seen.add(char)
        results.append(has_repeated_chars)
    return results

def get_elements_from_list(lst, start, end):
    return lst[start:end]

palindrome_results = check_palindrome("ab", "abc", "aba")
print(palindrome_results)

repeated_char_results = check_repeated_characters("aab", "abc", "def")
print(repeated_char_results)

lst = [1, 2, 3, 4, 5, 6]
elements = get_elements_from_list(lst, 1, 5)
print(elements)
