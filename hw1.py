import data
import math
# Write your functions for each part in the space below.

# Part 1
def vowel_count(string:str)->int:
    vowelCounter = 0
    '''for loop reads each character in string and runs through the code for that many strings
     if statement reads the character and will only continue if that character is part of the 
     "aeiouAEIOU" listo of characters and adds 1 to the counter'''
    for var in string:
        if var in "aeiouAEIOU":
            vowelCounter +=1
    #returns the final count of vowels
    return vowelCounter

# Part 2
def short_lists(lists : list[list[int]])->list[int]:
    shorter_list = []
    '''for statment loops through the list of lists, going through each list and checking with the if statement
    if the length of the list is 2. If the length is 2, then it adds both values in the list to the new list that is made
    finally returns what the new list is'''
    for i in range(len(lists)):
        if len(lists[i]) == 2:
            shorter_list.append(lists[i][0])
            shorter_list.append(lists[i][1])
    return shorter_list

# Part 3
def ascending_pairs(lists : list[list[int]]) ->list[int]:
    ascending_list = []
    '''for loop goes through each of the lists and then checks with the if statement if their length is 2.
    if this is true then it checks if the first value is greater than the second value and if this is true
    then it switches those values on line 40 then adds the change to the list. If the if statement is false 
    then it just adds the list that has two values as is. For other lists that have more or less than two they
    are just added to the list as is in line 45'''
    for i in range(len(lists)):
        if len(lists[i]) == 2:
            if lists[i][0] > lists[i][1]:
                lists[i][0], lists[i][1] = lists[i][1], lists[i][0]
                ascending_list.append(lists[i])
            else:
                ascending_list.append(lists[i])
        else:
            ascending_list.append(lists[i])
    return ascending_list

# Part 4
def add_prices(price1 : data.Price, price2: data.Price)->data.Price:
    '''Line: 55 takes the total dollar amount from both of the inputs and adds them together
    Line: 56 takes the total cents amount from both of the inputs and adds them together
    Line: 57 takes the total dollar amount and adds the number of times that the cents is divisable by 100
    Line: 58 takes the remainder of the cents that are divided by 100
    return value returns the new price with total of dollars and cents'''
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents
    total_dollars += total_cents //100
    total_cents = total_cents % 100
    return total_dollars,total_cents

# Part 5
def rectangle_area(shape : data.Rectangle)->int:
    '''coords pulls the top left and bottom right inputs from the class Rectangle. it then adds those dimensions to
    a new list by taking the first value from each (x) and subtracting the 1st value from the 2nd value and absolute valuing it
    after that it does the same with the (y) and while doing this for both adds them to the dimensions list. Finally the
    dimensions list gets each value pulled from it and multiplied together to get the area of the Rectangle'''
    coords = [shape.top_left, shape.bottom_right]
    dimensions = []
    dimensions.append(abs(coords[1].x - coords[0].x))
    dimensions.append(abs(coords[1].y - coords[0].y))
    return dimensions[0] * dimensions[1]

# Part 6
def books_by_author(author : str, listOfBooks : list[data.Book])->list[data.Book]:
    '''takes the book title from the list for every book in the list if the author of the book is
    the same as the author that we are searching for. This returns a list of the books that have
    the same author as the chosen one'''
    return [book.title for book in listOfBooks if author in book.authors]

# Part 7
def circle_bound(shape2 : data.Rectangle)->data.Circle:
    '''top left and bottom right pull the two coordinates from Rectangle'''
    top_left = shape2.top_left
    bottom_right = shape2.bottom_right
    '''center x and center y find the center points for both x and y values
    for the two points'''
    center_x = abs(top_left.x + bottom_right.x) / 2
    center_y = abs(top_left.y + bottom_right.y) / 2
    '''radius creates the radius value for the circle which is printed'''
    radius = math.sqrt(((center_x - top_left.x) **2) + ((center_y - top_left.y)**2))
    return radius

# Part 8
def below_average_pay(employees : list[data.Employee])-> list[str]:
    '''adds up all of the different employees pay with total pay
    takes the average of their pay with average pay by dividing the total pay
    by the number of workers'''
    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)
    '''takes employees that have below average pay and adds them to the list only if their pay is below average
    if an employees pay is above the average they are not included in the list'''
    below_average_employees = [employee.name for employee in employees if employee.pay_rate < average_pay]
    return below_average_employees
