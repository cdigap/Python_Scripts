# Ashok Gangadharan 2018-03-05

# Opening and closing a file in Python use "with" and 
# splitting the file and printing in a good format

with open("iris_data.csv") as f:
# Header formatting ...  
    print('________________________________________________________________')
    print("|Petal Length\t|Petal Width\t|Sepal Length\t|Sepal Width\t|")
    print('________________________________________________________________')
# For Loop to feed in line by line to print   
    for line in f:
# Details printed with 2 tab delimiters to make sure they are printed in a good format...
        print('|',line.split(',')[0],'\t\t|',line.split(',')[1],'\t\t|', line.split(',')[2],'\t\t|',line.split(',')[3],'\t\t|')
        print('________________________________________________________________')
