# As I don't yet have a dataset with more features, I will start to implement the workflow/ pipeline with the
# solvent dataset.

import pandas as pd
import numpy as np
#import seaborn as sns

dataset = pd.read_csv('../datasets/FreeSolv/SAMPL.csv')     # Python geht vom aktuellen Ordner aus.
                                                            # .. = gehe 1 Ordner hoch

print(dataset.describe())
#print(type(dataset))

