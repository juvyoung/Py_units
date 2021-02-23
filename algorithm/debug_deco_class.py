__author__      = "Juvyoung"
__copyright__   = "Copyright 2018"
__version__     = "0.0.1"
__email__       = ""
__status__      = "Prototype"
__date__        = "2020-xx-xx"

#import 
from timeit import default_timer as timer
from functools import wraps
import random
# import time

# ======================================     Class     ============================================
class deco_test_module(object):
    
    def __init__(self, show = False ):
        self.init_test_deco(show)

    def init_test_deco(self, show):
        self.show_res = show
        self.wrap_fn_name = None
        self.res = None
        
    def __call__(self, fn):
        """
        Parameters
        ----------
        fn : TYPE
            DESCRIPTION.
        Returns
        -------
        deco_measure_time : TYPE
            decorator function: Time measurement.
    
        """
        @wraps(fn)
        def wrap_time_measure(*args, **kwargs):
            
            tic = timer() #time.clock()
            self.res = fn(*args, **kwargs)
            toc = timer() #time.clock()
            
            self.wrap_fn_name = fn.__name__
            print( "@_time_operation: {0} took [ {1:5f}s ]".format(self.wrap_fn_name, toc-tic ) )
            
            if not self.show_res:
                pass
            else:
                self.print_result()
            
            return self.res
        
        return wrap_time_measure


    def print_result(self):
        ''' Print target function return value '''
        print( "Function [{0}] return value: \n{1} \n".center(20).format(self.wrap_fn_name, self.res) )

    
# ======================================  Test module  ============================================
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

# ======================================  Decorator  =============================================


# ==================================   Public functions   =========================================
@deco_test_module(show= True)
def bubble_sort( data_input ):
    """Pure implementation of bubble sort algorithm (basic) in Python 
    
    :param data_input: some mutable ordered data_input with heterogeneous 
    comparable items inside 
    :return: the same data_input ordered by ascending 
    
    Examples: 
    >>> bubble_sort([0, 5, 3, 2, 2]) 
    [0, 2, 2, 3, 5] 
    
    >>> bubble_sort([]) 
    [] 
    
    >>> bubble_sort([-2, -5, -45]) 
    [-45, -5, -2] 
    
    >>> bubble_sort([-23, 0, 6, -4, 34])
    [-23,-4,0,6,34] 
    """
    length = len(data_input)
    
    for j in range(0,length-1):
        for i in range(0,length-1-j):
            if data_input[i] > data_input[i+1]:
                data_input[i],data_input[i+1] = data_input[i+1],data_input[i]

    return data_input

@deco_test_module(show= True)
def bubble_sort_advanced( data_input ):
    """Pure implementation of bubble sort algorithm (advanced) in Python 
    
    :param data_input: some mutable ordered data_input with heterogeneous 
    comparable items inside 
    :return: the same data_input ordered by ascending
    
    Examples: 
    >>> bubble_sort_advanced([0, 5, 3, 2, 2]) 
    [0, 2, 2, 3, 5] 
    
    >>> bubble_sort_advanced([]) 
    [] 
    
    >>> bubble_sort_advanced([-2, -5, -45]) 
    [-45, -5, -2] 
    
    >>> bubble_sort_advanced([-23, 0, 6, -4, 34]) 
    [-23,-4,0,6,34] 
    """
    length = len(data_input)
    swapped = False
    for j in range(0,length-1):
        for i in range(0,length-1-j):
            if data_input[i] > data_input[i+1]:
                swapped = True
                data_input[i],data_input[i+1] = data_input[i+1],data_input[i]
        if True == swapped:
            break
        
    return data_input
# ==================================   Application Zone   ===========================================
'''------------------------------------------
            by: Juvyoung
--------------------------------------------'''
print ("\n".rjust(40, '=') +       
       "  Bubble sort  ".center(30) +      
       "\n".ljust(40, '=') )  
# ----------------------------------
#         MAIN FUNCTION
# ----------------------------------
def main():
    # try: 
        # raw_input          # Python 2 
    # except NameError: 
        # raw_input = input  # Python 3 
    # user_input = raw_input('Enter numbers separated by a comma:').strip() 
    # print( user_input )
    # unsorted = [ item for item in user_input.split(',')] 
    # Create a arry with random numbers
    unsorted = random_int_list(-10000,10000, 100)
    print( 'input array is: {0}'.center(20).format(str(unsorted)) )
    
    print("\n".rjust(40, '-'))
    sort_res = bubble_sort(unsorted)
    sort_res_adv = bubble_sort_advanced(unsorted)
    print("\n".rjust(40, '-'))
    
    print("\nTHE END \n ")


if __name__ == "__main__":
    main()


#Template
'''
          Comments
          
# -----  define  -----
print ("\n".rjust(40, '=') +
       "  Create Classes  ".center(30) +
       "\n".ljust(40, '=') )
          
print( 'ca_tan() :\n\
       degree value is: %f\n\
       ca_tan() value is: %f'
       %(deg, ca_tan( rad )) )
           
print('visit object 1 -> name: {0:5s}, age:{1:3d}'.format( obj_1.name, obj_1.age) )

    # print(' timer -> [0]: {0:10f},\n timer -> [1]: {1:10f}' 
    # .center(30).format( test_time_bubble_sort, 
    #           test_time_bubble_sort_advanced) )
    
'''
# END OF FILE