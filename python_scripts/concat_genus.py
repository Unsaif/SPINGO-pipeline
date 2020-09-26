import glob
import pandas as pd

if __name__ == '__main__':
    
    li = []
    lst = glob.glob("*_genus.csv")
    
    for csv in lst:
        df = pd.read_csv(csv,index_col=0, header = 0)
        li.append(df)

    df = pd.concat(li, axis=1, ignore_index = False, sort = True)
    df = df.fillna(0)
    df.to_csv("SPINGO_abundances_genus.tsv", sep="\t", index = True, header = True)
