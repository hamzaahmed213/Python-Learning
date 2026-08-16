# Character Frequency
sentence = input("Enter a sentence: ")
find = input("What Letter to find? ")

sentence = sentence.lower()
count = sentence.count(find);

print(f"{find} occured {count} times")