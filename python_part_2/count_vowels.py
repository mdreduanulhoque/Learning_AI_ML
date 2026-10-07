

txt = input("Enter a text: ")

vowel_count = 0
for ch in txt:
    if(ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U'):
        vowel_count +=1

print("Your text contains total", vowel_count, "vowels")