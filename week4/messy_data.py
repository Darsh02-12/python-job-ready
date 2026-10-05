import csv

with open('messy_data.csv','r') as a:                         #open and Reads the old file
    reader=csv.reader(a)
    header=next(reader)
    
    with open('clean_data.csv', 'w', newline='') as b:        #Create and writes in to new file
                writer=csv.writer(b)
                writer.writerow(['Name','Age','City'])        # heading clarified
                
                for row in reader:                            # looping through the old file
                    
                    name=row[0].capitalize()
                    
                    try:
                        age=int(row[1])
                    except ValueError:
                        print("Please Enter the integers only.")
                        continue
                    
                    city=row[2].strip().title()
                    
                    writer.writerow([name,age,city])          # With every loop iteration writes into the New file

                    print(name,age,city)                      #prints the output all written into new file
                    