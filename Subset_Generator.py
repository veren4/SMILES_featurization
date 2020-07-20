#dataset_filepath = '../datasets/ZINC15_testset.txt'    # is provided in wrapper

#subset_filepath = 'Subset.txt'                         # is provided in wrapper

#sample_size = 200                                      # is provided in wrapper

random_seed = 3


################# adapt parameters above #################

import random
random.seed(a=random_seed)
random_list = random.sample(range(1, 6885101), sample_size)

random_list.sort()  # sort the random set by values



f = open(subset_filepath, 'a')
  
        
with open(dataset_filepath) as ds:
    
    next_searched_line = random_list.pop(0)
        
    for index, line in enumerate(ds):  
        
        #if(index == 0):      # write the first line because of column names
        #    f.write(line)
  
        
        if index == next_searched_line:
            f.write(line)
                
            if(len(random_list) != 0):
                next_searched_line = random_list.pop(0)
            else:
                break
                
                   
f.close()