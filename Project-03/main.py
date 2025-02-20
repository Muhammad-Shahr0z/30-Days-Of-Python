#Word Counter App



word = input("Enter your word to count: ")

wordList= word.split()


print(f"\nThe length of the entered word is: {len(wordList)}")
print(f"The length of the entered Characters is: {len(word.strip())}")


