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
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for y in list:
    if y == 0 and y < 10:
        count += 10
print(count)
