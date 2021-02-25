__author__      = "Juvyoung"
__copyright__   = "Copyright 2018"
__version__     = "0.0.1"
__email__       = ""
__status__      = "Prototype"
__date__        = "2021-xx-xx"

#import 
import random

# ======================================  Library =================================================

# ======================================  Data types   ============================================

# ==================================   Public functions   =========================================
def random_hex( num ):
    
    _bin = 0
    
    for i in range(num):
        j = random.randint(0,1)
        _bin |= j << i
    
    return hex(_bin)


def test_case_1():
    """
    Basic application summery
    
    Returns
    -------
    None.

    """
    print ("\n".rjust(40, '-') +
       "  test case 1: feature of literator ".center(30) +
       "\n".ljust(40, '-') )
    lis = ['One','Two','Three','Four','Five','Six']

    enum_lis_= enumerate(lis,10)
    
    
    for index, item in enumerate(lis):
        print(' Index : {0}, Item: {1}'.format( index, item) )
    print(list(enumerate(lis)))
    
    #note: The following case show us enumerate object return a literator, it's 
    #  __next__ method return None at the end.
    print('\n start index from 10.')
    print(list(enum_lis_))
    for index, item in enum_lis_:
        print(' Index : {0}, Item: {1}'.format( index, item) )
        
    return None


def test_case_2():

    print ("\n".rjust(40, '-') +
       "  test case 2: string and tuple  ".center(30) +
       "\n".ljust(40, '-') )
    
    str = 'Hello Tony'
    tup = ( 'Monday', 'Friday', 'Sunday')
    
    for ind, letter in enumerate(str):
        print( 'The index is {0}, and the corresponding letter is: {1}'.format(ind, letter) )
    for ind, content in enumerate(tup,-5):
        print( 'The index is {0}, and the corresponding content is: {1}'.format(ind, content))
    
    return None


def test_case_3():

    print ("\n".rjust(40, '-') +
       "  test case 3: tuple list ".center(30) +
       "\n".ljust(40, '-') )
       
    ary = [('a','A'),('b', 'B'),('c','C')]

    for ind, (low,up) in enumerate(ary): 
            print( 'The index is {0}, and the corresponding letter is: {1} and {2}'.format(ind, low, up))

    return None


def test_case_4():
    
    print ("\n".rjust(40, '-') +
       "  test case 4  dictionary ".center(30) +
       "\n".ljust(40, '-') )
    
    animals = {'cat':2, 'dog':3, 'bugs':9, 'pig':9 }
    for k, v in animals.items():
        print(f'Animal spicis: {k:4s}, number: {v:2d}')
    
    return None


# ==================================   Application Zone   ===========================================
'''------------------------------------------
            by: Juvyoung
--------------------------------------------'''
print ("\n".rjust(40, '=') +       
       "  Built-in  ".center(30) +
       "\n".ljust(40, '=') )  
# ----------------------------------
#         MAIN FUNCTION
# ----------------------------------
def main():
    
    print( 'Random bin 64 is: {0}'.format( random_hex(16)) )
    test_case_1()  # list and liter()
    test_case_2()  # string and Tuple
    test_case_3()  # tuple list
    test_case_4()  # dictionary (no enumerate)
    
    print("\nTHE END \n ")


if __name__ == "__main__":
    
    """
     An enumerate object;
     
     enumerate(iterable,start=0)
     
     @par: Any iterable sequence like list, tuple or dictionary.
         
     @return: returns a tuple containing a count (from start which defaults to 0) 
     and the values obtained from iterating over iterable 

    """
    seq = [1,2,3,4,5]
    print('enumerate is an object:\n{0}'.format(enumerate(seq)))
    
    main()

#Template

'''
          Comments

    lis = ['One','Two','Three','Four','Five','Six']
    str = 'Hello Tony'
    tup = ( 'Monday', 'Friday', 'Sunday')
    ary = [('a','A'),('b', 'B'),('c','C')]
    
    animals = {'cat':2, 'dog':3, 'bugs':9, 'pig':9 }
          
# -----  define  -----
print ("\n".rjust(40, '=') +       
       "  Create Classes  ".center(30) +      
       "\n".ljust(40, '=') )          

    print ("\n".rjust(40, '-') +
       "  test case 3  ".center(30) +
       "\n".ljust(40, '-') )
    
    
print( 'ca_tan() :\n\
       degree value is: %f\n\
       ca_tan() value is: %f'
       %(deg, ca_tan( rad )) )
           
print('visit object 1 -> name: {0:5s}, age:{1:3d}'.format( obj_1.name, obj_1.age) )           
           
'''
# END OF FILE