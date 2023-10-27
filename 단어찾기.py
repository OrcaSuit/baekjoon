def contains_substring(str1, str2):
    str1 = str1.lower() 
    str2 = str2.lower()
    print(str1)
    print(str2)
    if str1 in str2 or str2 in str1: 
        return 1
    return 2

str1 = "ab6CDE443fgh22iJKlmn1o"
str2 = "6CD"

print(contains_substring(str1, str2))