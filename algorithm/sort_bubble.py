__author__      = "Juvyoung"
__copyright__   = "Copyright 2018"
__version__     = "0.0.1"
__email__       = ""
__status__      = "Prototype"
__date__        = "2020-xx-xx"

#import Zone
import test_tool.tool_random as random_tl
import test_tool.deco_utilities as deco_uti


# ======================================  Decorator  =============================================
class time_it( deco_uti.deco_time_record ):
    'sub class of time measurement'
    def __init__(self, show = True, log = True):
        self.local_util_int( show )
        self.log = log   #log argument is test only
        
    def local_util_int(self, show):
        ' call standard init. function '
        self.init_test_deco(show)

# ==================================   Public functions   =========================================
@time_it(show= False)
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

@time_it(show= False)
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
    unsorted = random_tl.random_int_list(-1000,1000, 1000)
    print( 'Random array is: \n{0}'.center(20).format(str(unsorted)) )
    
    print("\n".rjust(40, '-'))
    bubble_sort(unsorted)
    bubble_sort_advanced(unsorted)
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