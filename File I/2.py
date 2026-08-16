with open("story.txt", "r") as file:
    data = file.read()
count = data.lower().count("engineer")

print(f"Engineer Apperead {count} times ")