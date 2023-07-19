astr = 'bob'
try:
    print("hello")
    istr = int(astr) # unsatisfies won't see anything below it and move to except ----badline traceback
    print("there")
except:
    istr = -1

print('done', istr)

