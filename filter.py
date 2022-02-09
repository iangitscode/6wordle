w = open("output.txt", "w+")
f = open("words.txt", "r")
for line in f:
  if len(line) == 7:
    w.write(line)
f.close()
w.close()