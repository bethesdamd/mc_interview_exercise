
from collections import defaultdict
import sys

if len(sys.argv) != 2:
	raise Exception("You must enter rec number")
num_recs = int(sys.argv[1])

filename = '../master_list'
gen_lines = (line.strip() for line in open(filename, 'r'))

counts = defaultdict(int)
for line in gen_lines:
	columns = line.split('\t')
	columns = list(map( lambda x : x.strip(), columns))
	title_author = columns[0] + ' by ' + columns[1]
	counts[title_author] += 1

final = list()
for book, count in counts.items():
	if count == num_recs:
		final.append(book)

print(final)