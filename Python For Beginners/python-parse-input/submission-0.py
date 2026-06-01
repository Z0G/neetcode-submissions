from typing import List

def read_integers() -> List[int]:
    numbers = input()
    my_list = numbers.split(",")
    my_list = [int(i) for i in my_list]
    return my_list
    
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
