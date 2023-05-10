def generate_gene_combinations(genes: list, index=0, current=""):
    # Base Case if no elements/characters to add to every combination since index is already at the end of the list
    if index == len(genes):
        return [current]

    # List that will contain every possible combination 
    combinations = []

    for gene in genes[index]:
        # current element (gene) that belong in the nested list is to be concatenated to new current variable 
        new_current = current + gene

        # recursive call 
        # index is added by one because to proceed to the index of the next list in the nested list 
        # new_current is the new current parameter to produce every combination
        sub_combinations = generate_gene_combinations(genes, index+1, new_current)
        
        # after a base case is reached, elements of sub_combinations is to be extended to combinations list
        combinations.extend(sub_combinations)

    return combinations


def punnet_Square(geneA: list, geneB: list, outcome: str) -> float:
    # generate gene combination based on given 2D list
    gene_A_Possibilities = generate_gene_combinations(geneA)
    gene_B_Possbilities = generate_gene_combinations(geneB)

    all_Possible_Offspring = []
    # concatenates gene_A_Possibility and gene_B_Possibility to produce all possible offspring genes using a nested loop
    for gene_A_Possibility in gene_A_Possibilities:
        for gene_B_Possbility in gene_B_Possbilities:
            combination = gene_A_Possibility+gene_B_Possbility
            all_Possible_Offspring.append(combination)

    occurance_of_outcome_offspring = 0
    # compares every element of list all_Possible_Offspring to outcome parameter
    for offspring in all_Possible_Offspring:
        # sorted because outcome offspring is of different order from the elements present in all all_Possible_Offspring list
        if sorted(offspring) == sorted(outcome):
            occurance_of_outcome_offspring += 1

    # computes for percentage or ratio based on all the possible offspring
    percentage_of_outcome_offspring = (occurance_of_outcome_offspring / len(all_Possible_Offspring)) * 100
    
    # this makes sure that the offspring is possible if not return -1
    if (percentage_of_outcome_offspring > 0):
        return percentage_of_outcome_offspring
    else:
        return -1


# 4 Gene Combinations
gene4A = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd']]
gene4B = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd']]
out1 = punnet_Square(gene4A, gene4B, 'aabbccdd')
print(out1)

# 2 Gene Combinations 
gene2A = [['A', 'a']]
gene2B = [['A', 'A']]
out2 = punnet_Square(gene2A, gene2B, 'Aa')
print(out2)

# 3 Gene Combination
gene4A = [['A', 'a'], ['B', 'b'], ['C', 'c']]
gene4B = [['A', 'a'], ['B', 'b'], ['C', 'c']]
out3 = punnet_Square(gene4A, gene4B, 'aabbcc')
print(out3)

# 2 Gene Combination
# Try lang naman ito hehe; pero ang complex pag ito ginamit
# First Set: Long or Short
# Second Set: Brown or Black
gene5A = [['Long','Long'],['Black','Black']]
gene5B = [['Long','Short'],['Black','Brown']]
out4 = punnet_Square(gene5A, gene5B, 'LongShortBlackBlack')
print(out4)

# TO DO: Change input type to string only; pero parang goods na din pag list ang first two parameter