def generate_gene_combinations(genes, index=0, current=""):
    #Base Case if 
    if index == len(genes):
        return [current]

    combinations = []

    for gene in genes[index]:
        new_current = current + gene
        #print(new_current)
        #print(current)
        sub_combinations = generate_gene_combinations(genes, index+1, new_current)
        #print(sub_combinations)
        combinations.extend(sub_combinations)

        print(combinations)

    return combinations

# genes = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd'], ['E', 'e'], ['f', 'f']]
# gene3A = generate_gene_combinations(genes, 0, "")
# print(gene3A, len(gene3A))

genes = [['A', 'a'], ['B', 'b']]
gene3A = generate_gene_combinations(genes, 0, "")
print(gene3A, len(gene3A))
