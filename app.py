from itertools import combinations

def pos(g1: str, g2:str, out:str) -> float:
    #Edge Cases
        #CODE HERE

    #Algorithm Proper
    a = []
    b = []
    
    # Organelles
    for i in g1: 
        a.append(i)
    for i in g2: 
        b.append(i)
    
    put = []

    # Finals 
    for gene1 in a:
        for gene2 in b:
            res = gene1+gene2
            put.append(res)

    count = 0
    for a in put:
        if sorted(a) == sorted(out):
            count += 1
    
    return count 


b = pos('AaBb', 'AaBb', 'aa')

print(b)
# needs to be sorted

a = combinations('AaBbDd', 3)
print(a)


# ''.join(sorted(a))
