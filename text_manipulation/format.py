from sys import argv
script, text = argv

f = open(text, "r+")
w = open("new_text.txt", "w+")
count = 0
white_space = 0
new_string = ""
w.truncate()

for character in f:
    count += 1
    print(count)
    print(character)
    string = character
    for i in range(len(string)):
        if i == 0:
            if string[i] == " ":
                white_space += 1
        if string[i] == " ":
            white_space += 1
        else:
            white_space = 0
        if white_space > 1:
            pass
        else:
            new_string += string[i]
        #print(new_string)

new_string += "\n"
w.write(new_string)
w.close()
f.close()

