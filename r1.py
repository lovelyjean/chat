import os

# read file
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Kaede Chen':
			person = 'Kaede'
			continue
		elif line == 'Wendy Chiang':
			person = 'Wendy'
			continue
		elif line == 'Kally Lin':
			person = 'Kally'
			continue

		if person:
			new.append (person + ': ' + line)	
	# print(new)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	filename = 'input.txt'
	if os.path.isfile(filename):
		lines = read_file('input.txt')
		lines = convert(lines)
		write_file('output.txt', lines)
	else:
		print('file not found...')

main()