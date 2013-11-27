pyv8-linux-x64
==============

This is a binary distribution of PyV8 for Linux x86_64.

Dependencies:

* Boost 1.54

PyV8 and V8 versions included:

* PyV8 revision 429
* V8 revision 10452

Installation
=============

To install:
```
pip install -e git+https://github.com/taguchimail/pyv8-linux-x64.git@stable#egg=PyV8
```

Usage
=====

Import the pyv8 package to start using PyV8.

``` 
# From the PyV8 website
>>> from pyv8 import PyV8
>>> ctxt = PyV8.JSContext()          # create a context with an implicit global object
>>> ctxt.enter()                     # enter the context (also support with statement)
>>> ctxt.eval("1+2")                 # evalute the javascript expression
3                                    # return a native python int
>>> class Global(PyV8.JSClass):      # define a compatible javascript class
...   def hello(self):               # define a method
...     print "Hello World"    
...
>>> ctxt2 = PyV8.JSContext(Global()) # create another context with the global object
>>> ctxt2.enter()                    
>>> ctxt2.eval("hello()")            # call the global object from javascript
Hello World                          # the output from python script
```

Build Instructions
==================

Dependencies:

* GCC and G++
* SVN and Git
* Python
* Scons

## Boost

Download and extract Boost 1.54 and run the following:

```
[~/boost $] ./bootstrap.sh
[~/boost $] ./b2 install --prefix=/usr/local --with-python --with-thread
[~/boost $] ldconfig && ldconfig /usr/local/lib
```

## PyV8

Download PyV8 @ revision 429, and run the following:

```
[~/pyv8 $] patch -p1 < ~/pyv8-linux-x64/patches/pyv8.patch 
[~/pyv8 $] python setup.py build
```

Once built, copy the necessary build artifacts into the src folder.
