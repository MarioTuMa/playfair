import sys
args = sys.argv

method = args[1]
msg = args[2]
key = args[3]

def handle(char1,char2):
    x1 = keydict[char1][0]
    y1 = keydict[char1][1]
    x2 = keydict[char2][0]
    y2 = keydict[char2][1]
    toreturn = None
    if x1==x2:
        toreturn = keyarr[(x1+1)%5][y1]+keyarr[(x2+1)%5][y2]
    elif y1==y2:
        toreturn = keyarr[x1][(y2+1)%5]+keyarr[x2][(y2+1)%5]
    else:
        toreturn = keyarr[x1][y2]+keyarr[x2][y1]
    return toreturn

def handleReverse(char1,char2):
    x1 = keydict[char1][0]
    y1 = keydict[char1][1]
    x2 = keydict[char2][0]
    y2 = keydict[char2][1]
    toreturn = None
    if x1==x2:
        toreturn = keyarr[(x1-1)%5][y1]+keyarr[(x2-1)%5][y2]
    elif y1==y2:
        toreturn = keyarr[x1][(y2-1)%5]+keyarr[x2][(y2-1)%5]
    else:
        toreturn = keyarr[x1][y2]+keyarr[x2][y1]
    return toreturn

keydict = {}
keyarr = []
for i in range(5):
    newrow = []
    for j in range(5):
        keydict[key[5*i+j]]=[i,j]
        newrow.append(key[5*i+j])
    keyarr.append(newrow)
for row in keyarr:
    print(row)
codedstr = ""

if method == "encode":
    codedstr = ""
    while(len(msg)>0):
        if(msg[0]==msg[1]):
            codedstr += handle(msg[0],'X')
            msg = msg[1:]
        else:
            codedstr += handle(msg[0],msg[1])
            msg = msg[2:]
    print(codedstr)

if method == "decode":
    decodedstr = ""
    while(len(msg)>0):
        if(msg[0]==msg[1]):
            decodedstr += handleReverse(msg[0],'X')
            msg = msg[1:]
        else:
            decodedstr += handleReverse(msg[0],msg[1])
            msg = msg[2:]
    print(decodedstr)

