def scan(inputs):
    dlist = ["north","south","east","west","down","up","left","right","back"]
    vlist = ["go","stop","kill","eat"]
    slist = ["the","in","of","from","at","it"]
    nolist = ["door","bear","princess","cabinet"]
    nulist = [0,1,2,3,4,5,6,7,8,9]
    output = []
    input = inputs.split()
    for i in input:
        if i in dlist:     
            output.append(('direction', i))
        elif i in vlist:
            output.append(('verb', i))
        elif i in slist:
            output.append(('stop', i))
        elif i in nolist:
            output.append(('noun', i))
        elif convert_number(i):
            output.append(('number', i))
        else:
            output.append(('error', i))
    return output
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def lower(s):
    print(type(s))
    if s.isalpha():
        print(s.lower())
        return s.lower()
    else:
        return s

#print(scan("the"))
lower("TEST")