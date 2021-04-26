__author__      = "Juvyoung"
__copyright__   = "Copyright 2018"
__version__     = "0.0.1"
__email__       = ""
__status__      = "Prototype"
__date__        = "2020-xx-xx"

#import Zone
import random


# ======================================  Test Enviornment  =====================================

def random_int_list( st, end, length ):
    """
    Parameters
    ----------
    st : float
        Min. value of target array.
    end : TYPE
        Max. value of target array.
    length : int
        Target array length

    Returns
    -------
    random_list : TYPE
        A random number list.
        
    >>> Examples:
    >>> random_int_list(-10000,10000, 1000)
    """
    random_list = []
    length = int(abs(length))
    
    if end<st:
        print('Func: random_int_list --> 1st argument number should smaller than 2nd argument' )
        return None
    
    for i in range(length):
        random_list.append(random.randint(st,end))
        
    return random_list


def one_random_hex( num ):
    """
    
    middle function for 3 array inputs.
    ----------
    num : int
        how many bits random number.

    Returns
    -------
    hex
    One x bit random number
        
    >>> Examples:
    >>> random_hex(16); random_hex(32);
    """   
    _bin = 0
    
    for i in range(num):
        j = random.randint(0,1)
        _bin |= j << i
    
    return hex(_bin)

def random_hex_list( num, length ):
    """
    

    Parameters
    ----------
    num : TYPE
        DESCRIPTION.
    length : TYPE
        DESCRIPTION.

    Returns
    -------
    r_list : TYPE
        DESCRIPTION.

    """
    r_list = []
    length = int(abs(length))
    
    for i in range(length):
        r_list.append(one_random_hex(num))
    
    return r_list
    
    
if __name__ == "__main__":
    
    array_random = random_int_list(-10000,10000, 10)
    print( ' Random int list: \n {0}'.center(20).format(str(array_random)))
    print( '\n One Random hex number: \n {0}'.center(20).format(one_random_hex(8)))
    print( '\n One Random hex list: \n {0}'.center(20).format(random_hex_list(8,10)))

# END OF FILE