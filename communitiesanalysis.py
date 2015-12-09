from collections import defaultdict
md=defaultdict(list)
commcounter=0
with open('clauset.txt') as f:
    for line in f:
        if(line=="Community: \n"):
            commcounter=commcounter+1
        elif line.strip().isdigit():
            md[commcounter].append(int(line.strip()))


for entry in md:
    print len(md[entry])