import re

def is_haiku(commit_message: str) -> bool:
    """Check if a given text follows the 5-7-5 haiku pattern."""
    lines = commit_message.strip().split("-")
    if len(lines) != 3:
        return False
    
    sylanbles_in_lines = []
    
    for line in lines:
        sylanbles_in_lines.append(count_syllables_in_line(line))

    return sylanbles_in_lines == [5,7,5]
        
def count_syllables_in_line(line: str) -> int:
    words = line.strip().split(" ")
    return sum(count_syllables(word) for word in words)

def count_syllables(word: str) -> int:
    word = word.lower()
    if word.endswith("e") and not word.endswith("le"):
        word = word[:-1]  
        
    syllables = re.findall(r'[aeiouy]+', word)
    return max(1, len(syllables))  


print(is_haiku("An old silent pond-A frog jumps into the pond-splash! Silence again"))