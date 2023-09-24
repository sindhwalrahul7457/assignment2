#  Q1. How do you comment code in Python? What are the different types of comments?
# we can use (#) key to comment our code. in python we have single line comment and python doesnt support
# multi line comment. if wa need to a multiline code which python has to be ignore than we simply put (#) key in each
# line or  we can select all the line and then press (ctrl + /). and one more way we can use ('''      ''') to comment
# our code. python will ignore it.

# Q2. What are variables in Python? How do you declare and assign values to variables?
# in python variable are very important. we use variable to assign some value which can be (int, float, string, tuple,
# list, dictionary etc) and we can also take input from user using variable.
# it's very easy to declare a variable in python. simply we can use any letter or name. but we cant use any special
# symbole integer, floating etc as a variable, except the underscore(_) special sympole.
# we can assign a value in variable using assignment (=) operator.
# example           a = 14      b = input("enter your name")

# Q3. How do you convert one data type to another in Python?
# we can convert one data type to another by using type casting if we have a string variable number = '123' and we need
# to convert it into integer datatype then the syntex will a = int(a).
# example............
a = '123'
print(int(a))                                   # a string variable converted into an integer value.
tuple_1 = (1,23,4,5,"rahul")
tuple_1 = list(tuple_1)
print(tuple_1)                                  # here a tuple data type variable converted into a list datatype.

#Q4. How do you write and execute a Python script from the command line?
# firstly open the command prompt than enter your file location where it is located then press enter to execute the file.
# for example..
# "C:\Users\HP\rahul\python projects\p.py"
# to write python script on command promp  write py and then write your code and press enter to execute it.

#Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].
my_list = [1, 2, 3, 4, 5]
my_list2 = my_list[1:2]
print(my_list2)

#Q6. What is a complex number in mathematics, and how is it represented in Python?
# in mathamatics complex numbers are, the number that are expressed in the form of a + ib where a and b are the
# real number and i is the imaginary number.
# we represent complex number in python like this
# example
a = 1 + 2j                      # 1 and 2 are real number and python takes j as imaginary number.
print(type(a))

#Q7. What is the correct way to declare a variable named age and assign the value 25 to it?
age = 25

#Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable
#belong to?
Price = 9.99                  #data type = float
print(type(Price))            #output <class> float

#Q9. Create a variable named name and assign your full name to it as a string. How would you print the
#value of this variable?
name = "Rahul Singh Sindhwal"
print(name)

#Q10. Given the string "Hello, World!", extract the substring "World".
stringg = "hello, World!"
substring = stringg[7:12]
print(substring)

#Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are
#currently a student or not.
is_student = True
if is_student == 1:
      print("you are currently a student")
else:
      print("you are not a student")
