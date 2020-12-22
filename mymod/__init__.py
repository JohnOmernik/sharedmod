
#from mymod._version import __version__
from mymod._funcdocs import funcdict


__version__ = funcdict['modvers']
__modname__ = funcdict['modname']

from mymod.base import base_describe
from mymod.math_funcs import *
from mymod.string_funcs import *

