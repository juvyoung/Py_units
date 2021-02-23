__author__      = "Juvyoung"
__copyright__   = "Copyright 2018"
__version__     = "0.0.1"
__email__       = ""
__status__      = "Prototype"
__date__        = "2020-xx-xx"

#import 
from timeit import default_timer as timer
from functools import wraps

# import time

# ======================================     Class     ============================================
class deco_time_record(object):

    def __init__(self, show = False ):
        """ 
         Init. class deco_time_record
         
         Arguments description
            show: print target function result
            
         """
        self.init_test_deco(show)

    def init_test_deco(self, show):
        'Standard init. function'
        self.show_res = show
        self.wrap_fn_name = None
        self.res = None
        
    def __call__(self, fn):
        """
        Parameters
        ----------
        fn : TYPE
            Target function.
        Returns
        -------
        deco_measure_time : TYPE
            decorator function: Excute time measurement .
    
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
        ' Print target function return value '
        print( "Function [{0}] return value: \n{1} \n".center(20).format(self.wrap_fn_name, self.res) )
        
# ==================================   Application Zone   ===========================================