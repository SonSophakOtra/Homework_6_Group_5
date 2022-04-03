# EXERCISE 1 by Sophalkalyan Chheny
def replace_last():
    if len(num_lst) == 1:
        return num_lst
    
    last_item = num_lst[-1]
    last_index = num_lst.index(last_item)

    num_lst.pop(last_index)
    num_lst.insert(last_index, 1)
    num_lst.pop(0)
    num_lst.insert(0, last_item)

    return num_lst

# EXERCISE 2 by Son Sophak Otra
def index_power(array, n):
    return array[n] ** 2 if n < len(array) else -1
#EXERCISE 3 by Song Rithykun
if b not in num_lst:
        return num_lst
    if len(num_lst) <= 0:
        return num_lst

    bindex = num_lst.index(b)
    del num_lst[bindex+1:]

    return num_lst

# EXERCISE 4
def chunking_by():
    result = []
    for i in range(0, len(num_lst), chunksize): 
        result.append( num_lst[i:i + chunksize] )

    return result

# EXERCISE 5
def backward_string_by_word():
    return word[::-1]

def init():
    pass

if __name__ == "__main__":
    init()
    
