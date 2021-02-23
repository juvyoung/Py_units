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
    st : TYPE
        Min. value of target array.
    end : TYPE
        Max. value of target array.
    length : TYPE
        Target array length

    Returns
    -------
    random_list : TYPE
        A random number list.

    """
    random_list = []
    length = int(abs(length))
    if end<st:
        print('Func: random_int_list --> 1st argument number should smaller than 2nd argument' )
        return None
    
    for i in range(length):
        random_list.append(random.randint(st,end))
        
    return random_list

if __name__ == "__main__":
    
    array_random = random_int_list(-10000,10000, 1000)
    print( 'Random array is: \n{0}'.center(20).format(str(array_random)) )

# END OF FILE