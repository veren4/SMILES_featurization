########################################################################################################
#                                                                                                      #
# This script draws x random samples of size y from a dataset without loading the dataset into memory. #
#                                                                                                      #
########################################################################################################

#dataset_filepath = '../datasets/PubChem/CID-SMILES'
dataset_filepath = '../datasets/Lenselink_et_al/Dataset_files_342_MB/data/Supplementary_Information/dataset/compound_additional_physchem_features.txt'


sample_size = 10000

#number_of_lines_in_dataset = 103276515     # PubChem
number_of_lines_in_dataset = 204086   # Lenselink

random_seed = 42

######################################## adapt parameters above ########################################


import random
random.seed(a=random_seed)

# generate and open an output file
sample_filename = 'Lenselink_sample_' + str(random_seed) + '.txt'
sample_file = open(sample_filename, 'a')

# generate the random lines
lines_to_draw = random.sample(range(-1, number_of_lines_in_dataset), sample_size)
lines_to_draw.sort()

with open(dataset_filepath) as ds:

    # draw the samples
    next_searched_line = lines_to_draw.pop(0)

    for index, line in enumerate(iterable=ds):

        if index == next_searched_line:
            sample_file.write(line)

            if len(lines_to_draw) != 0:
                next_searched_line = lines_to_draw.pop(0)
            else:
                break

sample_file.close()
        


