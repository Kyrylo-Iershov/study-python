queue = ["John", "James", "Adam", "Adrian", "Amy", "Ali"]
txt = input(" Input custumer name : ")
queue.append(txt)
print(queue)
num = int(input(" Input custumer number : "))
print(queue[num])
print(len(queue))
half_list = len(queue)//2
print(queue[half_list])
print(queue.count("J"))
