
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	allen_wordcount = 0
	viki_wordcount = 0
	allen_sticker = 0
	viki_sticker = 0
	allen_pic = 0
	viki_pic = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker += 1
			elif s[2] == '圖片':
				allen_pic += 1
			else:
				for msg in s[2:]:
					allen_wordcount += len(msg)
			
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker += 1
			elif s[2] == '圖片':
				viki_pic += 1
			else:
				for msg in s[2:]:
					viki_wordcount += len(msg)

	print('Allen says: ', allen_wordcount, 'words, sent ', allen_sticker, 'stickers, and sent ', allen_pic, 'images')
	print('Viki says: ', viki_wordcount, 'words, sent ', viki_sticker, 'stickers, and sent ', viki_pic, 'images')



def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()