# Counting line numbers in large documents

i = 0

for line in open("../datasets/Lenselink_et_al/Lenselink_1_Molecular_Notation_Transformation_150samples.csv"):
    i += 1

print('Number of lines: ' + str(i))
