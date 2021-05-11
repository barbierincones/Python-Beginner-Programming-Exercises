import random

def get_color(color_number=4):

    color_number = int(color_number)

    switcher={
        0:'red',
        1:'yellow',
        2:'blue',
        3:'green',
        4:'black'
    }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():
    
    students_array = []
    for i in range(0,10):
        random_color_number = random.randint(0,4)
        example_color = get_color(random_color_number)
        students_array.append(example_color)
    return students_array 


print(get_allStudentColors())