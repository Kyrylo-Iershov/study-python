x = 1
while x < 5:
    if x%2 == 0:
        print(str(x) + " is even ")
    else:
        print(str(x) + " is odd ")
    x+=1
n = int(input())
lenght = 0
while n > 0:
    n//=10
    lenght +=1
print(lenght)