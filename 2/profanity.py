bad_words = ['peder', 'friednzone', 'mrsul', 'faking']
profanity_filter_on = True
sentence = ['dis', 'kars', 'faking', 'saks', 'mrsul']
for_stars = []
for i, item in enumerate(sentence):
	for j in bad_words:
		if item == j:
			for_stars.append(i)

if profanity_filter_on == True:
	for i in for_stars:
		count = len(sentence[i])
		sentence[i] = '*' * count
for_print = ""
for i in sentence:
	for_print += i + ' '
print(for_print)