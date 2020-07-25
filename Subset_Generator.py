########################################################################################################
#                                                                                                      #
# This script draws x random samples of size y from a dataset without loading the dataset into memory. #
#                                                                                                      #
########################################################################################################

# dataset_filepath = '../datasets/ZINC15_testset.txt'
dataset_filepath = '/media/verena/Data/1_Studium/03_Aufbaustudium_Informatik/Sem_2/Rostlab_Praktikum/4_Code/datasets/ZINC15_testset.txt'

number_of_samples = 3  # 15

sample_size = 2  # 200

number_of_lines_in_dataset = 50  # This is the range of number of lines within the samples will be drawn.
                                 # If unknown provide a rough estimation of the number, but one that will definitely
                                 # be <= the true number.

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
        my_to = (i + 1) * number_of_samples
        my_from = (i * number_of_samples) + 1
        current_line_range = (my_from, my_to)

        # generate the random lines       
        lines_to_draw = random.sample(current_line_range, sample_size)
        lines_to_draw.sort()

        # draw the samples
        next_searched_line = lines_to_draw.pop(0)

        for index, line in enumerate(ds):

            if index > current_line_range[1]:
                break

            if index == next_searched_line:
                current_sample_file.write(line)

                if len(lines_to_draw) != 0:
                    next_searched_line = lines_to_draw.pop(0)



        # increase i if index > current_line_range[1]    bzw. break out of the correct for loop

        current_sample_file.close()
        


