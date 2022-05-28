# check if two words are anagrams
# Example:
# find_anagrams("hello","check")-->False
# find_anagrams("below"'"elbow")-->True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if len(word) != len(anagram):
        return False

    word = sorted(word)
    anagram = sorted(anagram)

    if (word == anagram):
        return True
    return False
        


print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
