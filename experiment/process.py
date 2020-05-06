#  Morning Consult
#  Your task is to write a program that returns all books that have been recommended n times.

# Use this as a test, shows one title with 5 recommendations:  "The Selfish Gene"
# cut -d$'\t' -f1 master_list |sort| uniq -c|sort -n

import sys
from collections import defaultdict
import pprint

args = sys.argv
if len(args) != 2:
    raise Exception("You must provide an argument for the number of recommendations.")

num_recs = int(args[1])
FILENAME = '../master_list'

gen_lines = (line.strip() for line in open(FILENAME, 'r'))

# Skip the header line
next(gen_lines)
counts = defaultdict(int)

for line in gen_lines:
    columns = line.split('\t')
    # clean each entry
    columns = list(map(lambda x: x.strip(), columns))
    title_author_comb = columns[0] + ' by ' + columns[1]
    counts[title_author_comb] += 1

final = list()
for title, count in counts.items():
    if count == num_recs:
        final.append(title)

print(final)



