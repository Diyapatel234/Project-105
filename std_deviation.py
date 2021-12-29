import csv
import math
with open ('data.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
#Converting the data into a list.
data = file_data[0]
def mean (data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)

    mean = total/n 
    return mean

#Subtracting the mean from all the values and squareing them.
squared_list = []
for number in data:
    a  = int(number) -mean(data)
    a = a**2
    squared_list.append(a)

#Getting the sum of all the elements from the squared list.
sum = 0
for i in squared_list:
    sum = sum +i 

#Dividing the sum by the number of values in the dataset.
result = sum/(len(data)-1)

#Getting deviation by getting the square root of the result
std_deviation = math.sqrt(result)
print(std_deviation)


