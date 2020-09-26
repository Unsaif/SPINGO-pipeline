# SPINGO-pipeline
The SPINGO Pipeline is a tool that uses SPINGO to produce compatible input for mgPipe

# SYSTEM REQUIREMENTS
To run the SPINGO Pipeline and its supporting python scripts requires:

* A modern Linux operating system.
* Python3 or greater.
* [SPINGO](https://github.com/GuyAllard/SPINGO)
    
# INSTALLATION

The SPINGO Pipeline is hosted on GitHub

The SPINGO Pipeline source code and executables can be obtained via two different methods:

Either clone the repository using git:

`git clone https://github.com/Unsaif/SPINGO-pipeline`

Or download and extract the zip file using the 'Download ZIP' link of the GitHub project page.

No further installation is necessary for the single-end pipeline. The program can be run from within the cloned repository or from the location that the zip was extracted to.

To use the paired-end pipeline these following installation steps must be made:

1. `sudo apt-get update`
1. `sudo apt-get upgrade -y`
1. `sudo apt-get install libboost-all-dev`
1. `sudo apt install jellyfish`
1. `pip install HTSeq`

This document will assume that the SPINGO Pipeline is located in your home directory in a folder named `/home/your_username/SPINGO-pipeline`. This location will be referred to from hereon in as 'SPINGOPIPELINEDIR'.
If you have placed SPINGO Pipeline in a different location, use that path in place of 'SPINGOPIPELINEDIR'.

# SPINGO

Before the SPINGO Pipeline can be used SPINGO must be installed. 

Follow the necessary installation steps here: https://github.com/GuyAllard/SPINGO 

# RUNNING THE SPINGO PIPELINE

To run the pipeline, accession codes of individuals of interest are needed. This can be contained in a file of .txt, .tsv or .csv format.

What is necessary in the file of one of these formats is that there is a column named "accession" along with the codes of individuals underneath. 

The pipeline is capable of dealing with both single-end and paired-end. It will have to be specified in the command line which one is being dealt with. 

To run the pipeline using a file described above, and saving the output in the pipeline directory which will be labeled "the file's name + _output" for single-end (1) or paired-end (2):

`SPINGOPIPELINEDIR/pipeline -a path_to_accession_file/accession.csv -s full_path_to_spingo_directory -o 1`

If running from within the pipeline directory:

`./pipeline -a path_to_accession_file/accession.csv -s full_path_to_spingo_directory -o 1`

# OUTPUT

The SPINGO Pipeline writes output in a plain text format with tab separated columns (.tsv). The output of SPINGO Pipeline is a directory named "name of the accession file" + "\_output" situated in the SPINGO Pipeline directory and it consists of seven files::

* The unprocessed abundance tables: **SPINGO_abundances.tsv** & **SPINGO_abundances_genus.tsv**, respectively.
    
* The relative abundance tables on a species and genus level: **SPINGO_MbT_Species.tsv** & **SPINGO_MbT_Genus.tsv**, respectively.

* A file containing the total reads for each sample: **total_reads.tsv**
    
* Finally, two files that relay for each found species and genera, if they are absent, present or have a been renamed as a synonym in AGORA: **absent_present_species.tsv** & **absent_present_genus.tsv**.
