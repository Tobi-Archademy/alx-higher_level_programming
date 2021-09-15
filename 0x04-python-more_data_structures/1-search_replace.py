#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_e(elm):
        if elm != search:
            return elm
        else:
            return replace
    return list(map(s_r_e, my_list))
