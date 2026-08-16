with open("text.txt", "r") as file:
    data = file.read()

count = data.count("twinkle")

print(f"Twinkle appeared {count} times")