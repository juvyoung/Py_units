__author__      = "Juvyoung"
__copyright__   = "Copyright 2018"
__version__     = "0.0.1"
__email__       = ""
__status__      = "Prototype"
__date__        = "2021-xx-xx"

#import 
# ======================================  Library =================================================

# ======================================  Data types   ============================================

# ==================================   Public functions   =========================================
def example_func1():
    
    lis1 = [ 2, 15, 6, 8, 2 ]
    tup1 = ( 23, 0 , 15, 6, 1, 23 )
    str1 = 'Hello Tony'
    dic1 = {'me': 22, 2: 'Hi', 3: 50 }
    
    print('original list: {0}, after set() function :{1}'.format( lis1, set(lis1) ))
    print('original list: {0}, after set() function :{1}'.format( tup1, set(tup1) ))
    print('original list: {0}, after set() function :{1}'.format( str1, set(str1) ))
    print('original list: {0}, after set() function :{1}'.format( dic1, set(dic1) ))
    
    print( set(lis1) & set(tup1) )
    print( set(lis1) | set(tup1) )
    print( set(lis1) - set(tup1) )
    print( set(tup1) - set(lis1) )
    

    return None

# ==================================   Application Zone   ===========================================
'''------------------------------------------
            by: Juvyoung
--------------------------------------------'''
print ("\n".rjust(40, '=') +       
       "  Built-in set() function ".center(30) +
       "\n".ljust(40, '=') )  
# ----------------------------------
#         MAIN FUNCTION
# ----------------------------------
def main():
    
    """
     set is a built-in class;
     It takes iterable as an argument and returns a new set object;
     set([iterable])
     
     @par: Any iterable sequence like list, tuple or dictionary.
         * Dictionary can also be created using set, 
         but only keys remain after conversion, values are lost.
         
     @return: An empty set if no element is passed. 
     Non-repeating element iterable modified as passed as argument. 

    """
    s = set()
    tup = ()
    print('A basic set class: {0}; type: {1}'.format(s, type(s)))
    print('A empty tuple: {0}; type: {1}\n'.format(tup, type(tup)))
    
    example_func1()
    
    
    print("  THE END \n ")



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
           
'''
# END OF FILE