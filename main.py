# EXERCISE 1
def replace_last():
    pass

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
    
