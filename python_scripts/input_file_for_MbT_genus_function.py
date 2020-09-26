####
import pandas as pd

#python code that utilises pandas module for dealing with .tsv files
#Genus function
def input_file_for_MbT_genera(path_to_spingo_file, path_to_names_in_agora2, path_to_AGORA2_infoFile):

    data = pd.read_csv(path_to_spingo_file, sep="\t", header = 0, index_col = 0) #(*)

    data.index.name = 'Genus'
    data = data.fillna(0)
####

####
#the AGORA2_infoFile is inspected to see of the genus that remain which have models in AGORA2
#genus that are not present are marked as absent and both are saved accordingly
#if a genus is marked absent its name is checked to see if it exists in AGORA under another name
#if so its then marked as not absent

    pd.options.mode.chained_assignment = None 

    agora2 = pd.read_excel(path_to_AGORA2_infoFile, sheet_name = 'AGORA2_Reconstructions_Informat') #(*)

    df = agora2[["Genus"]]
    df = df.set_index('Genus')

    reduced_idx = pd.DataFrame(df.index.drop_duplicates(keep='first'))

    data['in_agora'] = data.index.isin(reduced_idx['Genus'])

    absent = data[data["in_agora"] == False]

    names = pd.read_excel(path_to_names_in_agora2) #(*) ####

    absent['qiime2_name'] = absent.index.isin(names['Name in QIIME2'])

    not_absent = absent[absent['qiime2_name'] == True]
    
    names = names.set_index('Name in QIIME2')
    
    not_absent = pd.merge(not_absent, names['Name in AGORA2'], left_index = True, right_index=True)
    
    renamed = pd.DataFrame({'QIIME2 Genus name': not_absent.index})
    renamed["absent/present/renamed"] = not_absent["Name in AGORA2"].values.tolist()
    
    cols = not_absent.columns.tolist()
    cols = cols[-1:] + cols[:-1]

    not_absent = not_absent[cols]
    not_absent.rename({'Name in AGORA2':'Genus'}, axis = 1, inplace = True)
    not_absent = not_absent.set_index('Genus')
    not_absent.drop(columns = ["qiime2_name"], inplace = True)
    not_absent.drop(columns = ["in_agora"], inplace = True)
    
    absent = absent[absent['qiime2_name'] == False]
    absent = pd.DataFrame({'QIIME2 Genus name': absent.sort_index().index})
    absent["absent/present/renamed"] = "AA_absent"
    
####

####
#not absent genus are reindexed based on their name in AGORA2 and then marked as present
    present = data[data["in_agora"] == True]
    present.drop(columns = ["in_agora"], inplace = True)
    
    present_in = pd.DataFrame({'QIIME2 Genus name': present.sort_index().index})
    present_in["absent/present/renamed"] = 'AA_present'
    absent_present = absent.append(present_in, ignore_index=True)
    absent_present = absent_present.append(renamed, ignore_index=True)
    absent_present.rename({0:'QIIME2 Genus name', 1:'absent/present/renamed'}, axis = 1, inplace = True)
    absent_present.to_csv('absent_present_genus.tsv', sep="\t", index = False, header = True)

    if len(not_absent) != 0: #only executes if there is not absent species
        present = present.append(not_absent)
####

####
#present genus are saved in a .tsv file ready for use in MicrobiomeToolbox
#the presence of these genus are also recorded in absent_present_genus.tsv in the correct column
#If there is no present genus a "No Genus found in AGORA2" will be outputted

    if len(present) != 0: #only executes if there is present species
    
        present.set_index(present.index.str.replace(" ", "_", regex = True), inplace = True)
        present.set_index('pan' + present.index.astype(str), inplace = True)
        present = present.groupby(present.index).sum()
        present = present.sort_index()
        present.to_csv('SPINGO_MbT_Genus.tsv', sep="\t", header = True)
    
    else:
        print("No Genus found in AGORA2")
####

if __name__ == '__main__':
    input_file_for_MbT_genera("SPINGO_abundances_genus.tsv", '../../files_needed_for_MbT/names_in_agora2.xlsx', '../../files_needed_for_MbT/AGORA2_infoFile.xlsx')
