import sys
import screed

filename = sys.argv[1]
print filename

count = 0
for record in screed.open(filename):
    count += 1
    if count > 10:
        break
    print record.sequence
    #if record.name == '@895:1:4:1596:8538/2':
        #break
