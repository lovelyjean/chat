import os

# read file
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	jean_word_count = 0
	jean_pic_count = 0
	jean_sticker_count = 0
	cat_word_count = 0
	cat_pic_count = 0
	cat_sticker_count = 0
	for line in lines:
		s = line.split('	')
		time = s[0]
		name = s[1]
		if name == 'lovely jean':
			if s[2] == '[写真]':
				jean_pic_count += 1
			elif s[2] == '[スタンプ]':
				jean_sticker_count +=1
			else:
				for m in s[2:]:
					jean_word_count += len(m)
		elif name == 'コンドウヒトシ':
			if s[2] == '[写真]':
				cat_pic_count += 1
			elif s[2] == '[スタンプ]':
				cat_sticker_count +=1
			else:
				for m in s[2:]:
					cat_word_count += len(m)
		# print(s)

	print('jean say ', jean_word_count, 'words and send ', jean_pic_count, 'pics ', jean_sticker_count, ' stamps')
	print('cat say ', cat_word_count, 'words and send ', cat_pic_count, 'pics ', cat_sticker_count, ' stamps')

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	filename = 'line.txt'
	if os.path.isfile(filename):
		lines = read_file('line.txt')
		lines = convert(lines)
		# write_file('output.txt', lines)
	else:
		print('file not found...')

main()