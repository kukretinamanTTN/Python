'''
Structure:

    -Project
        __init__.py
        -Package1
            __init__.py
            -module1.py
            -module2.py
        -Package2
            -__init__.py
            -module3.py
            -module4.py
            -subpackage1
                -module5.py
        -imports.py

'''

#relative import

#importing Project/Package2/subpackage1/module5.py/fun5 to Project/Package2/imports.py
# from .subpackage1.module5 import fun5
# fun5()

# #importing Project/Package1/module1.py/fun5 to Project/Package2/imports.py
# from ..Package1.module1 import fun1
# fun1()


# from . import module3
# module3.fun3()

# import module3
# module3.fun3()


from Package1 import module1
module1.fun1()