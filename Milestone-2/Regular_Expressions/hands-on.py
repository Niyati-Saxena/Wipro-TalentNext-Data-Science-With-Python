import re
import requests

# WAP to check if a string has only octal digits (0–7)
strings = ['789', '123', '004']
octal_check = [s for s in strings if re.fullmatch(r'[0-7]+', s)]
print(octal_check)


# WAP to extract user ID, domain name, and suffix from emails
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

results = [re.match(r'(\w+)@(\w+)\.(\w+)', email).groups() for email in emails.split('\n')]
print(results)


# WAP to split irregular sentence into proper words
sentence = "A, very   very; irregular_sentence"
words = re.sub(r'[^\w\s]', ' ', sentence)  
words = re.sub(r'_', ' ', words)      
output = ' '.join(words.split())        
print(output)


# Clean up the tweet text so that it contains only the user's msg. Remove all URLs, hashtags, punctuations, mentions, RTs, CCs.
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
clean_tweet = re.sub(r"http\S+|@\S+|#\S+|RT|cc:|[^\w\s]", '', tweet)
clean_tweet = ' '.join(clean_tweet.split())
print(clean_tweet)


# Extract all text portions between the tags from the given HTML page
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text
text_inside_tags = re.findall(r'>([^<>]+)<', html)
cleaned_text = [text.strip() for text in text_inside_tags if text.strip()]
print("Text between HTML tags:", cleaned_text)


# Given below list of words, identify the words that begin and end with the same character.
# civic, trust,  widows, maximum, museums, aa, as

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
matching_words = [word for word in words if word[0] == word[-1]]
print("Words that begin and end with the same character:", matching_words)
