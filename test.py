#genes = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd'], ['E', 'e']]
genes = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd']]

gene3A = []
gene3B = []
for i in genes[0]:
    for j in genes[1]:
        for k in genes[2]:
            gene3A.append(i+j+k)
            gene3B.append(i+j+k)

allGenes = []
for geneA in gene3A:
    for geneB in gene3B:
        combine = geneA+geneB
        allGenes.append(combine)

test = 'aabbcc'
occurance = 0

for i in allGenes:
    if sorted(i) == sorted(test):
        occurance += 1

print(occurance / len(allGenes))

# gene4 = []
# for i in genes[0]:
#     for j in genes[1]:
#         for k in genes[2]:
#             for l in genes[3]:
#                 for m in genes[4]:
#                     gene4.append(i+j+k+l+m)

# print(len(gene4)) 
# print(gene4)               

# gene2 = []
# for i in genes[0]:
#     for j in genes[1]:
#         gene2.append(i+j)
# print(gene2)
