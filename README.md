## Featurization of SMILES for Deep Learning

This is my project for a research internship at the [Rostlab](https://www.rostlab.org/) at TUM with supervision from Prof. Dr. Burkhard Rost and Christian Dallago.
It is my task to find a representation for small molecules (a class of drugs) for Deep Learning Applications such as binding affinity prediction.
The basis for that is the SMILES representation. As a baseline, I take fingerprints.

Files and their function:
* 0_Data_Loading.ipynb\
General data loading and saving as csv.
* 0_Data_Loading_h5.ipynb\
I look at the data from ChemicalChecker, which is in h5 format. It turns out they only offer their model and not their raw data for download, so that exploration ends in this notebook.
* 1_Finding_the_alphabet.ipynb\
My personally constructed apporach to tokenize canonical SMILES.

* 1_Finding_the_alphabet_SmilesPE\
I use the [SmilesPE package](https://pypi.org/project/SmilesPE/) to tokenize SMILES.

* 1_Molecular_Notation_Transformation.ipynb\
I transform SMILES to Fingerprints using the [RDKit package](https://www.rdkit.org/).

* 2_Umap.ipynb\
I generate 3-dimensional UMAPs.

* 3_Alphabet_comparison_Lense_PubChem.ipynb\
In this notebook, load and tokenize samples drawn from the Lenselink- as well as from the PubChem dataset.

* 4_Cleaning_the_Lense_dataset.ipynb\
I filter the Lenselink dataset for entries that have a token-alphabet that is a subset of the alphabet shared with PubChem.

* 4_Cleaning_the_PubChem_dataset.ipynb\
I filter the PubChem dataset for entries that have a token-alphabet that is a subset of the alphabet shared with Lenselink.

* alphabet_finder_0.py\
A script that extracts the token-alphabet from a file that contains SMILES with my own tokenization method and saves them to a txt file.

* Handling_large_datasets.ipynb\
My (failed) approach to generate a script that can handle (large) files without loading them into memory all at once.

* Lenselink_0_Mapping_SMILES_to_Lenselink.ipynb\

* Lenselink_1_Molecular_Notation_Transformation.ipynb\

* Lenselink_2_UMAP_2D.ipynb\

* Lenselink_2_UMAP_3D.ipynb\

* Lenselink_3_UMAP_2D_binarized_properties.ipynb\

* Lenselink_4_Clustering_embeddings.ipynb\

* PubChem package.ipynb\
I explore the PubChemPy package.

* Sample_Generator_BackToBasics.py\
This script draws x random samples of size y from a dataset without loading the dataset into memory.

* Subset_Generator_linecounter.py\

* Subset_Generator_PubChem.py\
My failed attempt to make a random-subset-generator that draws x samples à n rows from a dataset without loading it into memory.

* Subset_Generator.py\
something wrong.
