data = [["Bob","123"],
        ["Joe","234"],
        ["Mary","345"]]

data2 = []
f = open("file.txt","w")

for d in data:
        f.write(d[0]+","+d[1]+"\n")

f.close()
f = open("file.txt","r")
text = f.readlines()
for t in text:
        t = t.strip()
        temp = t.split(",")
        data2.append(temp)

f.close()
print(data2)

