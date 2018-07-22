# -*- coding: utf-8 -*-
# @Time    : 2018/6/24
# @Author  : 
# @File    : check.py


class Check(object):
    def __init__(self):
        pass

    @staticmethod
    def check_type(obj, type_name, loc):

        variable = [k for k in loc if loc[k] == obj][0]
        if not isinstance(obj, type_name):
            raise Exception("variable {var} (value:{obj})should be {type}".format(var=variable ,obj=obj, type=type_name))
        else:
            return True

#debug
if __name__ == "__main__":

    a =None
    print (a is not None)
    print (Check.check_type(a, int, locals()))
