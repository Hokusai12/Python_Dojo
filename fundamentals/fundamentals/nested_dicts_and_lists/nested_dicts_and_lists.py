#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(str(students[0]))

sports_directory['soccer'][0] = 'Andres'
print(str(sports_directory))

z[0]['y'] = 30
print(z[0])


# Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for list_dict in some_list:
        log = ''
        if(type(list_dict) is dict):
            for key, value in list_dict.items():
                log += key + " - " + value + ", "
        print(log)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary(students)

# Get Values From a LIst of Dictionaries
def iterateDictionary2(key_name, some_list):
    for list_dict in some_list:
        print(list_dict[key_name])

iterateDictionary2('last_name', students)



# Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key in some_dict:
        print(str(len(some_dict[key])) + " " + key)
        for value in some_dict[key]:
            print(value)
        print("\n")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)