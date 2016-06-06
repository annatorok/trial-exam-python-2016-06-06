# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list

def double_value(input):
    new_list = []
    try:
        if type(input) != list:
            raise TypeError
        for x in input:
            new_list.append(x*2)
        return new_list
    except TypeError:
        print('The input is not a list')

print(double_value([1, 2, 3, 4, 5, 6]))
(double_value('a, b'))
