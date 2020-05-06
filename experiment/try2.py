
from collections import defaultdict
import sys

if len(sys.argv) != 2:
	raise Exception("You must provide number of recommendations")

filename = 'master_list'

# Supports huge files
gen_lines = (line.strip() for line in open(filename, 'r'))
# skip header
next(gen_lines)
counts = defaultdict(int)
for line in gen_lines:
	columns = line.split('\t')
	# clean
	columns = list(map(lambda x: x.strip(), columns))
	title_author = columns[0] + ' by ' + columns[1]
	counts[title_author] += 1
final = list()
for book, count in counts.items():
	if count == 5:
		final.append(book)

print(final)