def list1(list):
    emstr1 = ''
    #the program here loops through every element in the given list 1 and adds them to the empty string 1
    for i in list:
        emstr1 += i
    return emstr1

    #the program here loops through every element in the given list 2 and adds them to the empty string 2
def list2(sublist):
    emstr2 = ''
    for i in sublist:
        emstr2 += i
    return emstr2

#First we create a function is_sublist in which the program will check if the second argument is contained inside the first argument
def is_sublist(list, sublist):
    #finally the program should check if the second string is contained inside the first string, therefore outputting True, otherwise outputting False
    if list2(sublist) in list1(list):
        return True
    else:
        return False


#Here we define the function main in which we ask the user for two inputs passed in the program as lists, separating the elements by spaces ' '
def main():
    listA = input('write a list ').split(' ')
    listB = input('write a list contained in the previous list ').split(' ')

    #then the program should pass the two lists in the previusly defined function
    print(is_sublist(listA, listB))

if __name__ == '__main__':
    main()
