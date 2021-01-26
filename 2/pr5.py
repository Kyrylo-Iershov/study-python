words = ["spam", "eggs", "python", "tutorial", "is", "fun"]
index = 1
words.insert(index, "and")
print(words)
words = ["spam", "eggs", "python", "tutorial", "is", "fun"]
for word in words:
    print(word + "!")
str = "testing for loops"
count = 0
for x in str:
    if x == 't':
        count += 1
print(count)
