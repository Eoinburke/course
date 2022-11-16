
# # # # # # # # sales = [30000, 32000, 25000, 40000]
# # # # # # # # quote = "Turn chould've, would've, and should've into can, will, can do."

# # # # # # # # print("do" in quote)


# # # # # # # # print("did" in quote)


# # # # # # # # print(25000 in sales)


# # # # # # # # print("quote" not in quote)

# # # # # # # # print(40000 not in sales)

# # # # # # # # print(3 * 4 + 2**4 / 2)

# # # # # # # # listX = ['A', 'B', 'C', 'D', 'E', 'F']
# # # # # # # # listY = list(listX)

# # # # # # # # listY.remove('B')
# # # # # # # # listA = [1,2,3,4,5,6]
# # # # # # # # listB = listA
# # # # # # # # listB.remove(3)

# # # # # # # # print(listX, listY, listA, listB)

# # # # # # # # regions = ["North", "South", "East", "West"]
# # # # # # # # sales = [30000, 20000, 40000, 35000]
# # # # # # # # employees = ["Alice", "Vera", "Flo", "Mel"]

# # # # # # # # print("Region: ", regions[0], "Sales: ", sales[0])
# # # # # # # # print("Region: ", regions[-1], "Sales: ", sales[-1])

# # # # # # # # price = 3.95
# # # # # # # # widgets = 5
# # # # # # # # print("The price of the widget is ", price)
# # # # # # # # print("We have " + str(widgets) + " in stock")
# # # # # # # # print(price * widgets) 
# # # # # # # # print(int(price), float(widgets))

# # # # # # # # a = 3
# # # # # # # # b = a
# # # # # # # # north_items = ["Rain gear", "Snow shoes"]
# # # # # # # # east_items = ["Rain gear", "Snow shoes"]

# # # # # # # # print(a == b)


# # # # # # # # print(a is not b)


# # # # # # # # print(a is b)


# # # # # # # # print(north_items is not east_items)


# # # # # # # # print(north_items == east_items)

# # # # # # # # print(north_items is east_items)

# # # # # # # # a = 8
# # # # # # # # b = 3
# # # # # # # # print( 'Addition:\t' , a , '+', b , '=' , a + b )        
 
 
# # # # # # # # print( 'Subtraction:\t' , a , '-', b , '=' , a - b )     
 
 
# # # # # # # # print( 'Multiplication:\t' , a , 'x', b , '=' , a * b )  
 
 
# # # # # # # # print( 'Division:\t' , a , '÷', b , '=' , a / b )        
 
 
# # # # # # # # print( 'Floor Division:\t' , a , '÷', b , '=' , a // b ) 
 
 
# # # # # # # # print( 'Modulus:\t' , a , '%', b , '=' , a % b )         
 
 
# # # # # # # # print( 'Exponent:\t ' , a , '² = ' , a ** b , sep = '' ) 

# # # # # # # # north = 200
# # # # # # # # south = 300
# # # # # # # # northwins = north > south
# # # # # # # # southwins = south > north
# # # # # # # # print("Northwins = ", northwins, "Southwins = ", southwins)  

# # # # # # # # value = 4

# # # # # # # # a = str(value)
# # # # # # # # b = a + "⌃" + "2"
# # # # # # # # c = a + "⌃" + "3"

# # # # # # # # print(value, "+", b, "+", c)

# # # # # # # # a = "40.6 "
# # # # # # # # b = "60.4 "
# # # # # # # # c = a + b
# # # # # # # # print(c)

# # # # # # # if 'bin' in {'float': 1.2, 'bin': 0b010}:
# # # # # # #     print('a')
# # # # # # #     print('b')
# # # # # # # print('c')

# # # # # # a =[1, 'one', {2: 'two'}, 3]
# # # # # # b = len(a)

# # # # # # if b == 4:
# # # # # #     print('Length of this list is 4')
# # # # # #     if b == 5:
# # # # # #         print('length of this list is 5')
# # # # # #     else:
# # # # # #         print(b)

# # # # # # var = "hi"
# # # # # # if(type(var) == int):
# # # # # #     print('Type is int')
# # # # # # elif(type(var) == float):
# # # # # #     print("type is flot")
# # # # # # elif(type(var) == complex):
# # # # # #     print("type is complex")
# # # # # # else:
# # # # # #     print("type unknown")

# # # # # num_one = 76
# # # # # num_two = 23.4
# # # # # print("datatype of num_one:", type(num_one))
# # # # # print("datatype of num_two:", type(num_two))

# # # # a = "six"
# # # # b = (int(a), float(a))

# # # total_classes = 100
# # # attended_classes = 67

# # # attendance = (attended_classes/total_classes)*100
# # # if attendance >= 75:
# # #     print("you are good")
# # # else:
# # #     print("no good hoomie")

# # my_list = [['tiger', 'lion'], ['camel', 'llama'], ['zebra', 'donkey']]

# # for x in my_list:
# #     print(type(x))

# x = list(range(-17, -7, 2))
# print(xx)

# x = 4
# while x <10:
#     print(x+1)

# inventory = []
# item = ""
# while item != "quit":
#     item = input("Enter item:")
#     print("Adding item:", item)
#     inventory.append(item)

# words = ['eoin', 'burke', 'hey', 'just']
# for i in words:
#     print(i)

# for i in range(5):
#     print('hello')

max = 5

max = input("How many tickets?:")
if max > str(5):
    print('im sorry you are over the max')

if max < str(5):
    print(input("How old are you?:"))

age = 12


age = input("How old are you?:")
if age < str(12):
    print("You are not old nough hommie")
else:

 if age >= str(12) and age < str(18):
  if age > str(12):
        print(input("Have you a school ID?:"))

 elif age == "Y":
        print("enjoy the ride rember you are only allowed 3 rides")

 if age == "N":
        print("Not today dawg")

ride = 3

ride = input("How many times have you done this ride?:")

if ride == str(3):
    print("health issue, enjoy")

if ride < str(3):
    print("enjoy")

if ride > str(3):
    print("you have done it more than 3 times ") 



