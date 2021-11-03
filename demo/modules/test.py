
import sys

print(sys.path)   # Module search path

sys.path.insert(0, r"c:\classroom\oct12\demo\lib")

import numbers as nf
from numbers import ispositive


print(nf.iseven(10))
print(ispositive(10))