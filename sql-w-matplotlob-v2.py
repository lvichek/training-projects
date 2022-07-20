import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

# what I'm trying to do here is to input 
# my modified variables into query, 
# retrieve them back and then draw a simple graph 
# w matplotlib

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "menagerie"
)

def myfunc1(x):
    return x * 3

def myfunc2(x):
    return myfunc1(x) + 5   

mycursor = connection.cursor()

input_numbers = input("give me numbers to work with: ")
input_numbers = [int(i) for i in input_numbers.split()]

mycursor.execute("CREATE TABLE numbers \
    (id INT AUTO_INCREMENT PRIMARY KEY, \
    x INT, \
    func_one INT, \
    func_two INT);")

insert = ("INSERT INTO numbers \
    (x, func_one, func_two) \
    VALUES (%s, %s, %s)")

insertion_data = [] 
for x in input_numbers:

    insertion_data.append(x)
    insertion_data.append(myfunc1(x))
    insertion_data.append(myfunc2(x))

    insert = ("INSERT INTO numbers \
    (x, func_one, func_two) \
    VALUES (%s, %s, %s)")

    mycursor.execute(insert, insertion_data)
    connection.commit()  

    insertion_data.clear()

retrieve = ("SELECT x, func_two FROM numbers;")
mycursor.execute(retrieve)


x_result = []
y_result = []
for result in mycursor:
    result = list(result)
    x_result.append(result[0])
    y_result.append(result[1])

print(f"your results here: {x_result}, {y_result}")    


mycursor.close()
connection.close()

x = np.array(x_result)
y = np.array(y_result)
plt.plot(x, y, marker = 'o')
plt.show()