def isPalindrome(strng):
    if len(strng) == 0:
        return True
    elif strng[0] != strng[len(strng)- 1]:
        return False
    else:
        return isPalindrome(strng[1: -1])

if __name__ == "__main__":
    word = input("Enter a word: ")
    print("The palindrome of the word is: ", isPalindrome(word))