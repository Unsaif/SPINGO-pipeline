import pandas as pd
import os

def abundances(path):
    
    data = pd.read_csv(path, sep='\t', header = None)
    
    accession = path.split('.')[0]
    
    abundance = {}

    data = data[data[6] != "AMBIGUOUS"]
    data = data[data[7] >= 0.5]

    unqe = data[6].unique()

    for species in unqe:
        spcs = str(species)
        abundance[spcs] = data[6].str.count(spcs).sum()

    abundances = pd.DataFrame.from_dict(abundance, orient='index', columns = [accession])
    
    total_reads = pd.DataFrame(abundances.sum(), columns = ["Total Reads"])
    total_reads.to_csv("../abundance_files/" + accession + '_total_reads.tsv', sep="\t", index = True, header = True)
 
    abundances = abundances.loc[:].div(abundances.sum(axis = 0))

    abundances.to_csv("../abundance_files/" + accession + '.csv', index = True, header = True)
    
if __name__ == '__main__':
    abundances(os.environ["inp"])
