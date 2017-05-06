import korean.hangul as kr
import sys

hangul_roman = {
				'ㄱ' : 'g',
				'ㄴ' : 'n',
				'ㄷ' : 'd',
				'ㄹ' : 'r',
				'ㅁ' : 'm',
				'ㅂ' : 'b',
				'ㅅ' : 's',
				'ㅇ' : '',
				'ㅈ' : 'j',
				'ㅊ' : 'ch',
				'ㅋ' : 'k',
				'ㅌ' : 't',
				'ㅍ' : 'p',
				'ㅎ' : 'h',
				'ㄲ' : 'kk',
				'ㄸ' : 'tt',
				'ㅃ' : 'pp',
				'ㅆ' : 'ss',
				'ㅉ' : 'jj',
				'ㅏ' : 'a',
				'ㅑ' : 'ya',
				'ㅓ' : 'eo',
				'ㅕ' : 'yeo',
				'ㅗ' : 'o' ,
				'ㅛ' : 'yo',
				'ㅜ' : 'u',
				'ㅠ' : 'yu', 
				'ㅡ' : 'eu' ,
				'ㅣ' : 'i',
				'ㅐ' : 'ae',
				'ㅒ' : 'yae',
				'ㅔ' : 'e',
				'ㅖ' : 'ye',
				'ㅘ' : 'wa',
				'ㅙ' : 'wae',
				'ㅚ' : 'oe' ,
				'ㅝ' : 'wo',
				'ㅟ' : 'wi',
				'ㅞ' : 'we',
				'ㅢ' : 'ui'
				}

batchim = {
			'ㄱ' : 'k',
			'ㄴ' : 'n',
			'ㄷ' : 't',
			'ㄹ' : 'l',
			'ㅁ' : 'm',
			'ㅂ' : 'p',
			'ㅅ' : 't',
			'ㅇ' : 'ng',
			'ㅈ' : 't',
			'ㅊ' : 't',
			'ㅋ' : 'k',
			'ㅌ' : 't',
			'ㅍ' : 'p',
			'ㅎ' : 't',
			'ㄲ' : 'k',
			'ㅆ' : 't',
			'ㄺ': 'lg',
			'ㅄ': 'ps',
			'ㄵ': 'nj',
			'ㄼ': 'lb',
			'ㅀ': 'l',
			'ㄶ': 'n',
			'ㄾ': 'lt,',
			'ㄻ': 'lm,',
			'ㄿ': 'lp',
			'ㄳ': 'g'
}

def romanize(sentence):
	blocks = list(sentence)
	romanized_sentence = ''
	upper = True

	for block in blocks:
		if kr.is_hangul(block):
			letters = kr.split_char(block)
			
			for i in range(len(letters)):
				if i == 2:
					if letters[i] != '' and letters[i] in batchim:
						romanized_sentence = romanized_sentence + batchim[letters[i]]
				else:
					if upper:
						romanized_sentence = romanized_sentence + str.upper(hangul_roman[letters[i]])
						upper = False
					else:
						romanized_sentence = romanized_sentence + hangul_roman[letters[i]]
		else:
			if block in '.!?':
				upper = True

			romanized_sentence = romanized_sentence + block

	# return str.upper(romanized_sentence[0] + romanized_sentence[1:]
	return(romanized_sentence.strip())

print('Welcome to the Hangul->Latin Script Conversor 0.9\n')
print('Please insert the korean text:\n')

lines = []

while True:
	line = input()
	if line:
		lines.append(line)
	else:
		break

for sentence in lines:       
	print(romanize(sentence))

print()