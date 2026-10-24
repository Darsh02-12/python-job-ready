with open("notes.txt","w") as f:
    f.write("The blue teapot hummed a quiet tune before the storm.\n Velvet curtains whispered secrets to the open window.\nThree")
# n=0
with open("notes.txt","r") as f:
    for line_num, line in enumerate(f,start=1):
        # n+=1
        print(f'{line_num}:{line.strip()}')