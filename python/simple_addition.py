import lupa
from lupa import LuaRuntime

# Import the Lua runtime
lua = LuaRuntime(unpack_returned_tuples=False)

# Evaluate string as lua code with lua.eval() - and return the value!
one_plus_one = lua.eval('1+1')
print(one_plus_one)

# Setup a function that can take a python function + two variables n, m as inputs,
# and returns the results of running that python function on n, m
lua_func = lua.eval('function(f, n, m) return f(n, m) end')

# simple addition function in python
def py_add(n, m): return n+m

# run the py_add function with one and two as arguments - in Lua!
one_plus_two = lua_func(py_add, 1, 2)
print(one_plus_two)