# Given a text file containing paragraphs. Based on its contents, determine:
# - Meeting time: Convert the total number of lines in the file to 12-hour format. 
# - Meeting place: Find the most frequently occurring word in the file and use it as the name of the street in the format

import string
from collections import Counter

def decode_meeting_info(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    # meeting time
    num_lines = len(lines)
    hour = num_lines % 12 if num_lines % 12 != 0 else 12
    period = 'AM' if num_lines < 12 else 'PM'
    meeting_time = f"{hour} {period}"

    # meething place
    all_words = []
    for line in lines:
        # Removing punctuation and lowercase everything
        cleaned = line.translate(str.maketrans('', '', string.punctuation)).lower()
        all_words.extend(cleaned.split())
    
    word_counts = Counter(all_words)
    most_common = word_counts.most_common(1)[0][0].capitalize()
    meeting_place = f"{most_common} Street"
    
    print("Meeting time:", meeting_time)
    print("Meeting place:", meeting_place)
