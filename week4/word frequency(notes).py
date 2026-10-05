

with open('notes.txt', 'r') as f:
    my_list = [word.strip(".,?!").lower() for line in f for word in line.split()]

new_word={}    

for words in my_list:
    if words in new_word:
        new_word[words] +=1
    else:
        new_word[words] =1



print(new_word)