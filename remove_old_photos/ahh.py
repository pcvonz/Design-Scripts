import glob
import os

new = glob.glob("new\*")
old = glob.glob("old\*")
for i in range(len(new)):
    new_split = new[i].split('\\')
    
for i in range(len(old)):
    old_split = old[i].split('\\')
    #print(old_split[1])

for item in old:
    for i in new:
        if item[4:].lower() == i[4:].lower():
            try:
                pass
                #print(item, "\n=", i)
                os.remove(i)
            except WindowsError:
                print("FILE LOCKED:", i)
        else:
            print(item.lower(), "\n!=", i)


