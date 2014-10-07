text = input("filename:")

f = open(text, "r+")
w = open("new_sorted_list.txt", "w+")
count = 0
white_space = 0
new_string = ""
w.truncate()

list = []

for i in f:
    string = i[0].upper() + i[1:]
    list.append(string)

list.sort()

for i in list:
    w.write(i)

w.close()