from custom_package import add,upper
from custom_package.sub_package.multiply import mult
print(add(2,4))
print(upper('easy'))
print(mult(2,2))

# if do not want it to come from init.py then we can also do : from custom_package.string_utils import upper
from custom_package.math_utils import add
print(add(2,8))