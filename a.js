function generateGeneCombinations(genes, index = 0, current = "") {
    if (index === genes.length) {
      return [current];
    }
  
    const combinations = [];
  
    for (const gene of genes[index]) {
      const newCurrent = current + gene;
      const subCombinations = generateGeneCombinations(genes, index + 1, newCurrent);
      combinations.push(...subCombinations);
    }
  
    return combinations;
  }
  
  const genes = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd']];
  const gene3A = generateGeneCombinations(genes, 0, "");
  console.log(gene3A);
  