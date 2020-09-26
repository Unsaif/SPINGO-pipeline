import pandas as pd
import os

def abundances_genus(path):
    
    data = pd.read_csv(path, sep='\t', header = None)
    
    accession = path.split('.')[0]
    
    abundance = {}

    data = data[data[4] != "AMBIGUOUS"]
    data = data[data[5] >= 0.5]

    unqe = data[4].unique()

    for genus in unqe:
        genera = str(genus)
        abundance[genera] = data[4].str.count(genera).sum()

    abundances = pd.DataFrame.from_dict(abundance, orient='index', columns = [accession])
    abundances = abundances.loc[:].div(abundances.sum(axis = 0))

    abundances.to_csv("../abundance_files/" + accession + '_genus.csv', index = True, header = True)
    
if __name__ == '__main__':
    abundances_genus(os.environ["inp"])
