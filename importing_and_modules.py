## Modules & Packages

# A module in Python is just a script file that contains some code/classes/whatever else. # A package is a directory
# that contains modules.
# Instead of just having one giant script that contains all the code that you need, using modules & packages allows us
# to separate Python code into chunks that make it easy to reuse bits of code.

# You can import a specific function or class from a module
from a_module import hello_from_a_module

hello_from_a_module()

# By using *, you can import all functions/classes from a module
from a_module import *

hello_from_a_module()
greetings_from_a_module()

# You can import specific modules from a package by using <PackageName><dot><module_name>.
from a_package.in_package import *
hello_from_a_package()

# Note that a_package contains a function called _secret_hello_from_a_package(). Because this is a function prefixed
# by an underscore (recall from the section on classes), it is not visible outside the module where it is defined.
# _secret_hello_from_a_package()  # won't run

# You can, however, call public functions which call private functions inside them.
calls_secret_hello()

# You can have packages inside other packages - just use More Dots.
# Python doesn't let you use * to import all modules or subpackages from a package. However, you can add
# code to the package's __init__.py define what gets imported when you import * on that package. Check out __init__.py
# in a_package/a_subpackage to see how this works.
from a_package.a_subpackage import *

hello_from_a_subpackage()
another_subpackage_function_says_hello

