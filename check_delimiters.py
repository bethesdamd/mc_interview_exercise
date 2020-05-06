# Locate any lines in delimited file that don't have the expected
# number of delimiters

filename = 'master_list'

# Use a generator since it can scale to any sized data file
gen_lines = (line for line in open(filename, 'r'))

for line in gen_lines:
  c = line.count('\t')
  if c != 11:
    print(c)

