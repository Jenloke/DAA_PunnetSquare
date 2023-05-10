function genes(gene1, gene2) {
    // for edge cases
    if (gene1.length % 2 == 1 || gene2.length % 2 == 1) {
        return -1;
    }

    if (gene1.length != gene2.length) {
        return -1; 
    }

    // Alogorithm Proper

    geneLength = gene1 / 2; 

    gene1Arr = [];
    gene2Arr = [];

    for (let i=0; i < gene1.length; i+=geneLength) {
        gene1Arr.push(gene1.slice(i,i+2));
        gene2Arr.push(gene2.slice(i,i+2));
    }

    console.log(gene1Arr);
    console.log(gene2Arr);

    // String Comparison
    // in js lower case is higher than upper case    

    // for (let i=0; i < gene1Arr.length; i++) {
    //   for (let j=0; j < gene2Arr.length; j++) {
        
    //   }
    // }
}

console.log(genes('AaBb', 'aabb'));
//console.log('a'=='A');
//console.log('a'<'A');
//console.log('a'>'B');