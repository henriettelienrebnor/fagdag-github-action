import re

def is_haiku(commit_message: str) -> bool:
    """Check if a given text follows the 5-7-5 haiku pattern."""
    lines = commit_message.split('-')
    isHaiku = True
    
    if count_syllables_in_line(lines[0]) != 5:
        isHaiku = False
    if count_syllables_in_line(lines[1]) != 7:
        isHaiku = False
    if count_syllables_in_line(lines[2]) != 5:
        isHaiku = False

    return isHaiku

def count_syllables_in_line(line: str) -> int:
    syllables = 0
    words = line.strip().split(' ')
    for word in words:
        syllables += count_syllables(word)
    return syllables
        
def count_syllables(word: str) -> int:
    """Count vowel groups in a word. Remove silent e unless word ends with le"""
    word = word.lower()
    
    if word.endswith('e') and not word.endswith('le'):
        word = word[:-1]

    syllables = re.findall(r'[aeiouy]+', word)
    return max(1, len(syllables))  
