from collections import *
clustertouser=defaultdict(list)
usertocluster=Counter()

commcounter=0
with open('clauset.txt') as f:
    for line in f:
        if(line=="Community: \n"):
            commcounter=commcounter+1
        elif line.strip().isdigit():
            userid = int(line.strip())
            clustertouser[commcounter].append(userid)
            usertocluster[userid]=commcounter


print commcounter
maxkey= max(clustertouser,key=lambda k:len(clustertouser[k]))
print maxkey,len(clustertouser[maxkey])

clustertoaddress=defaultdict(list)
addresscounter=1
with open('bitcoin_uic_data_and_code_20130410/userkey_list.txt') as f:
    for line in f:

        if(usertocluster[addresscounter]):
            addresses=[int(address) for address in line.split(',')]
            clustertoaddress[usertocluster[addresscounter]]+=addresses
        addresscounter=addresscounter+1
        if addresscounter%100000==0:
            print addresscounter,len(clustertoaddress)

print len(clustertoaddress)
sizecouter=Counter()
print("CLUSTERS:")
for cluster in clustertoaddress:
    print len(clustertoaddress[cluster])
    sizecouter[len(clustertoaddress[cluster])]+=1

print ("ClusterSize")
for size in sorted(sizecouter):
    print size, sizecouter[size]

