string = "Accio job"

freq:list[int] = [0] * 26

for ch in string:
    char = ch.lower()
    
    if char.islower():
        freq[ord(char)-ord('a')] += 1
        
print(*freq)