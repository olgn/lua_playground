import os
import lupa
from lupa import LuaRuntime

# get the path of the print_string.lua file
code_directory = os.path.split(os.path.dirname(os.path.realpath('__file__')))[0] # get the path of the project directory, based on this file's absolute path
external_lua_file_path = os.path.join(code_directory, 'lua_scripts', 'print_string.lua') # get the path of the print_string.lua file, which lives in the lua_scripts/ folder 

lua = LuaRuntime(unpack_returned_tuples=True)

# create function for opening files
open_file = lua.eval('function (filename) f = loadfile(filename)() end')

# open the 'print_string.lua file
print('loading external lua file...')
open_file(external_lua_file_path)

# opening that file dumps all the functions from that
# file into lua.globals
g = lua.globals()

# obtain the print_string function contained within print_string.lua
# call print_string on 'squirt' >> equivalent to print('squirt')
print_string = g.print_string
print_string('this string was printed by print_string()')

# obtain the print_and_return_string contained within print_string.lua
# and call print_and_return_string on 'squirt' >> prints 'squirt' and
# should store that value as a return
print_and_return_string = g.print_and_return_string
squirt = print_and_return_string('this string was printed and returned by print_and_return_string()')
print('print_and_return_string() actually returned a string? ', type(squirt) == str)