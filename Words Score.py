def score_words(words):
    score = 0
    if len(words)<=20:
        for word in words:
            num_vowels = 0
            if len(word)<=20 and word.lower()==word:
    	        for letter in word:
    	            if letter in 'aeiouy':
    	                num_vowels = num_vowels + 1
    	        if num_vowels % 2 == 0:
    	            score = score + 2
    	        elif num_vowels % 2 != 0:
    	            score = score + 1
            else: break
    else: pass
    return score

#print(score_words(input().split()))