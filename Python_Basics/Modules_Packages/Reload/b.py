from importlib import reload
from . import a

#unchanged
print(a.x)

#changed
a.x = 2
print(a.x)

#reloaded
reload(a)
print(a.x)