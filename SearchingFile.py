fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('checking'):
        print(line)

# Searches if starting with Hi and prints whole line