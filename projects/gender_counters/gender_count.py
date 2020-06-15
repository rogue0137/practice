from collections import Counter
import csv
   

def get_gender_count(filename):
    """ This function takes an input of a csv file.
    It then creates a counter to count number of times
    gender MALE and gender FEMALE appear. It returns 
    the counter of genders. 
    This function assumes there is a header in the file. 
    It can not be used for files without headers. For file
    header checking, I would use the has_header method in the
    csv.Sniffer class. 
    This function also assumes that column one is a name and
    column two is a gender. 
    It also assumes that the only gender options are MALE 
    and FEMALE in various casings."""
    
    gender_count = Counter()
    
    with open(filename, 'rb') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader, None) 
            
        for row in csv_reader:
            column_with_gender = row[1]
            uppercase_gender = column_with_gender.upper()
            gender_count.update({uppercase_gender: 1})
            
    return gender_count 


print(get_gender_count('gendered.csv'))

 