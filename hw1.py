import data

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


# Part 6


# Part 7


# Part 8


