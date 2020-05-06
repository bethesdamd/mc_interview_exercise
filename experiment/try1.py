# practice 1
# Assumed run with 'python this_script.py'

from collections import defaultdict
import sys

filename = 'master_list'

#  check that argument exists
if len(sys.argv) != 2:
	raise Exception("You must provide argument for number of recommendations")

# Use generator to handle any file size
gen_lines = (line.strip() for line in open(filename, 'r'))

# Skip header line
next(gen_lines)

counts = defaultdict(int)

for line in gen_lines:
	columns = line.split('\t')
	columns = list(map(lambda x: x.strip(), columns))
	title_author = columns[0] + ' by ' + columns[1]
	counts[title_author] += 1

final = list()
for title, count in counts.items():
	if count == 5:
		final.append(title)
print(final)