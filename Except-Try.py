astr = "Hello World"
try:
    istr = int(astr) # This condition fails and then drops to except side
except:
    istr = -1

print('First', istr)


astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)