__author__      = "Tony"
__date__        = "2021-04-13"


# ======================================  Library =================================================
import numpy as np
# ======================================  Data types   ============================================

# ==================================   Public functions   =========================================

# ==================================   Application Zone   ===========================================
'''-------------------------------------------------------------------------------------------
                       =======  numpy C function api ==========
                       Served as interface for external call
                       ! The ONLY object for external calling !
   by: Tony
---------------------------------------------------------------------------------------------'''
class api_np_cfunc(object):
    """Pure implementation of embeded system algorithm ( with numpy) in Python
    
    >>> Examples: 
    >>> import util_filter_class.class_c_lib2np as np_clib_api
    >>> np_clib_obj = np_clib_api.api_np_cfunc()
    
    """
    def __init__(self):
        pass

    def first_order_lag_filter(self, src, tst ):
        """
        
        c like 1st order lag input filter.
        ----------
        src : nparray
            Target un-fliltered datum.
        tst : float
            Time filter constant.

        Returns
        -------
        nparray
            The filtered input.
            
        >>> Examples:
        >>> np_clib_obj.first_order_lag_filter( unfilter_nparray, 0.1 )
        
        """
        self.res = []
        self.res.append(src[0])
        for i in range( 1,len(src)):
            self.res.append( (src[i]-self.res[i-1])*(0.01/tst) + self.res[i-1] )
        
        return np.array(self.res)

    def dinteg_output(self, src, k_tp ):
        """

        PT1 filter output function.
        ----------
        src : nparray
            output setpoint, unfiltered.
        k_tp : float
            Time constant PT1 filter parameter.

        Returns
        -------
        nparray
            The filtered output.
            
        >>> Examples:
        >>> c_like_f_rpm_k_100 = np_clib_obj.dinteg_output( min_rpm_set, 100 )
        """
        mod_r = 0
        
        self.res = []
        self.res.append(src[0])
    
        for i in range( 1,len(src)):
            self.res.append( (((src[i]-self.res[i-1])*10.0 + mod_r)/k_tp ) + self.res[i-1])
            mod_r = ((src[i]-self.res[i-1])*10.0 + mod_r) % k_tp
        
        return np.array(self.res)
    
    def middle_func( self, src0, src1, src2 ):
        """
        
        middle function for 3 array inputs.
        ----------
        src0,src1,src2 : nparray
            3 input array datum.

        Returns
        -------
        nparray
            middle of 3 inputs
            
        >>> Examples:
        >>> np_clib_obj.middle_func( array0,array1,array2 )
        """
        self.res = []
        
        for i in range(len(src1)):
            self.res.append( np.median([ src0[i], src1[i], src2[i]]) )

        return np.array(self.res)
    
'''
          Comments
'''
# END OF FILE