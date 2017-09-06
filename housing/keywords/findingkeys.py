import re


words = 'asdf fsfo w fdifa aohfoeh ahfdi wefih!! 3 toilets. 1 shared toilet. no toilet ok and maybe seven shared toilet.'

toilet_patt = '\w+ \w+ toilet*|[\!\.] \w+ toilet*|\w+ toilet*'

num_patt = 'a|one|two|three|four|five|six|seven|eight|nine|ten'
num_dic = ['a', 'one',  'two', 'three', 'four', 'five',
	'six', 'seven', 'eight', 'nine', 'ten']
toilet_sta_patt = 'private|personal|independent|bublic|shared' 
toilet_sta_dic = [['private', 'personal', 'independent'],['bublic', 'shared']]


def toilet_finder(words):
	# return a list === [private , public]
	# [0, 0] === no mention
	return_this = [0, 0]
	
	keyn = re.findall('toilet*', words)

	# find toilet, if no then there is no description about toilet
	if(keyn == []):
		print('no toilet')
		return return_this
		
		
	prob_pattern = re.findall(toilet_patt, words)
	# analyze every toilet descriptions
	for key in prob_pattern:
		num_t = re.findall('[1-9]+', key)
		if(num_t !=[]):
			# luckly toilet with a number
			# the first result(must be only one)
			num_t = int(num_t[0])
			print(num_t)
		
		else:
			# there is no number before toilet, try words
			num_t = re.findall(num_patt, key)
			if(num_t != []):
				for i in [i for i,x in enumerate(num_dic) if x == num_t[0]]:
					if(i == 0):
						# 'a' == 1
						num_t = 1
						print(num_t)
					else:
						num_t = i
						print(num_t)
			else:
				num_t = 0
				print('no numnber belones to this toilet.')
		
		# then find private, public or none
		num_s = re.findall(toilet_sta_patt, key)
		if(num_s != []):
			for sta,i in enumerate(toilet_sta_dic):
				for j in i :
					if j == num_s[0]:
						return_this[sta] += num_t
						print('0=private, 1=public: ' + str(sta))
		else:
			return_this[1] += num_t
			print('dont Know, so add to public')
			
		print('--')

	print(prob_pattern)
	
	return return_this
	
toilet_info = toilet_finder(words)
print(toilet_info)
