import glob
import pandas as pd

if __name__ == '__main__':
    
    li = []
    li_reads = []
    lst = glob.glob("*.csv")
    reads_lst = glob.glob("*_total_reads.tsv")
    
    for csv in lst:
        df = pd.read_csv(csv,index_col=0, header = 0)
        li.append(df)
   
    for tsv in reads_lst:
        df_reads = pd.read_csv(tsv, sep ="\t", index_col=0, header = 0)
        li_reads.append(df_reads)
    
    df_reads = pd.concat(li_reads, axis=1, ignore_index = False, sort = True)
    df_reads = df_reads.fillna(0)
    df_reads = df_reads.groupby(level=0, axis=1).sum()
    df_reads.to_csv("total_reads.tsv", sep="\t", index = True, header = True)

    df = pd.concat(li, axis=1, ignore_index = False, sort = True)
    df = df.groupby(level=0, axis=1).sum()
    df = df.fillna(0)
    df.to_csv("SPINGO_abundances.tsv", sep="\t", index = True, header = True)
