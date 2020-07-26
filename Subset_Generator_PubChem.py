########################################################################################################
#                                                                                                      #
# This script draws x random samples of size y from a dataset without loading the dataset into memory. #
#                                                                                                      #
########################################################################################################

dataset_filepath = '../sample_file_numbered.txt' #'../datasets/PubChem/CID-SMILES'

number_of_samples = 4 #15

sample_size = 3 #200

number_of_lines_in_dataset = 101 # 103276515     # true number of lines (looked up in linux terminal, as the file is "just" 2,2 G in size.

random_seed = 3

######################################## adapt parameters above ########################################


import random

random.seed(a=random_seed)

subset_linecount = number_of_lines_in_dataset // number_of_samples

with open(dataset_filepath) as ds:
    for i in range(number_of_samples):

        # generate and open an output file
        sample_filename = 'sample_' + str(i + 1) + '.txt'
        current_sample_file = open(sample_filename, 'a')

        # determine the line range
        my_to = int((i + 1) * (number_of_lines_in_dataset / number_of_samples))  # replace later part with linecount (floor // )
        my_from = int(my_to - subset_linecount + 1)

        # generate the random lines       
        lines_to_draw = random.sample(range(my_from-1, my_to+1), sample_size)
        lines_to_draw.sort()

        # draw the samples
        next_searched_line = lines_to_draw.pop(0)

        for index, line in enumerate(iterable=ds):    # The index starts new every iteration, the line aka enumeration doesn't!!!

            if index > my_to:
                break

            if index == next_searched_line:
                current_sample_file.write(line)

                if len(lines_to_draw) != 0:
                    next_searched_line = lines_to_draw.pop(0)

        current_sample_file.close()
        


