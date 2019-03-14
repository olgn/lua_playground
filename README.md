# Lua Playground

This repository serves as a playground for me to experiment with the [Lua](https://www.lua.org/) language. I became interested in the embeddable, portable, and modular nature of Lua, and decided it would be interesting to play around with importing some simple `.lua` scripts and executing them in several different languages.

A good resource for learning low-level Lua is [Programming in Lua](https://www.lua.org/pil/contents.html)

## Python

### Setup

Clone the project repository and change into the python folder:
```
git clone https://github.com/olgn/lua_playground.git
cd lua_playground/python
```

Then set up a virtual environment with python3.6 and [Lupa](https://github.com/scoder/lupa), an integrated Lua runtime for Python. This code requires virtualenv - install with `pip install virtualenv`
```
python -m virtualenv -p python3.6 .env
source .env/bin/activate
pip install -r requirements.txt
```

### Run an example

Now that you are sitting pretty in a virtualenv with python3.6 and Lupa, go ahead and run a script ending in `.py` (within the python folder).

For example, here is a script that demonstrates how to use lua function calls inline with python and adds 1 + 1 and then 1 + 2 (fancy!):
```
python simple_addition.py
```
Expected output:
```
2
3
```

Another example shows how to import the functions contained in an external `.lua` file, and use them inline with python code:
```
python call_external_file.py
```
Expected output:
```
loading external lua file...
this string was printed by print_string()
this string was printed and returned by print_and_return_string()
print_and_return_string() actually returned a string?  True
```