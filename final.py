# helper recursive function for punnet_square function
def generate_gene_combinations(genes: list, index: int = 0, current: str = "") -> list[str]:
    # base case if no elements/characters to add to every combination since index is already at the end of the list
    if index == len(genes):
        return [current]

    # list that will contain every possible combination 
    combinations = []

    for gene in genes[index]:
        # current element (gene) that belong in the nested list is to be concatenated to new current variable 
        new_current = current + gene

        # recursive call 
        # index is added by one because to proceed to the index of the next list in the nested list 
        # new_current is the new current parameter to produce every combination
        sub_combinations = generate_gene_combinations(genes, index + 1, new_current)
        
        # after a base case is reached, elements of sub_combinations is to be extended to combinations list
        combinations.extend(sub_combinations)

    return combinations


def punnett_square(gene_A: list[str], gene_B: list[str], outcome: str) -> float:
    # generate gene combination based on given 2D list
    gene_A_possibilities = generate_gene_combinations(gene_A)
    gene_B_possbilities = generate_gene_combinations(gene_B)

    all_possible_offspring = []
    # concatenates gene_A_possibility and gene_B_possibility to produce all possible offspring genes using a nested loop
    for gene_A_Possibility in gene_A_possibilities:
        for gene_B_Possbility in gene_B_possbilities:
            all_possible_offspring.append(gene_A_Possibility + gene_B_Possbility)

    occurance_of_outcome_offspring = 0
    # compares every element of list all_possible_offspring to outcome parameter
    for offspring in all_possible_offspring:
        # sorted because outcome offspring is of different order from the elements present in all all_possible_offspring list
        if sorted(offspring) == sorted(outcome):
            occurance_of_outcome_offspring += 1

    # computes for percentage or ratio based on all the possible offspring
    percentage_of_outcome_offspring = (occurance_of_outcome_offspring / len(all_possible_offspring)) * 100
    
    # this makes sure that the offspring is possible if not return -1
    if (percentage_of_outcome_offspring > 0):
        return percentage_of_outcome_offspring
    else:
        return -1


# 4 Gene Combinations
gene4A = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd']]
gene4B = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd']]
out1 = punnett_square(gene4A, gene4B, 'aabbccdd')
print(out1)

# 2 Gene Combinations 
gene2A = [['A', 'a']]
gene2B = [['A', 'A']]
out2 = punnett_square(gene2A, gene2B, 'Aa')
print(out2)

# 3 Gene Combination
gene4A = [['A', 'a'], ['B', 'b'], ['C', 'c']]
gene4B = [['A', 'a'], ['B', 'b'], ['C', 'c']]
out3 = punnett_square(gene4A, gene4B, 'aabbcc')
print(out3)

# 2 Gene Combination
# Try lang naman ito hehe; pero ang complex pag ito ginamit
# First Set: Long or Short
# Second Set: Brown or Black
gene5A = [['Long','Long'],['Black','Black']]
gene5B = [['Long','Short'],['Black','Brown']]
out4 = punnett_square(gene5A, gene5B, 'LongShortBlackBlack')
print(out4)

# TO DO: Change input type to string only; pero parang goods na din pag list ang first two parameter