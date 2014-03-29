pyv8-linux-x64
==============

This is a binary distribution of PyV8 for Linux x86_64.

Dependencies:

* Boost 1.54

PyV8 and V8 versions included:

* PyV8 revision 557
* V8 branch 3.22

Installation
=============

To install:
```
pip install -e git+https://github.com/taguchimail/pyv8-linux-x64.git#egg=pyv8
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
* Systemtap (systemtap-sdt-devel) / DTrace

## Boost

Download and extract Boost 1.54 and run the following:

```
[~ $] mkdir -p ~/boost && cd ~/boost
[~/boost $] wget http://sourceforge.net/projects/boost/files/boost/1.54.0/boost_1_54_0.tar.gz && tar -xvzf boost_1_54_0.tar.gz
[~/boost $] ./bootstrap.sh
[~/boost $] ./b2 install --prefix=/usr/local --with-python --with-thread
[~/boost $] ldconfig && ldconfig /usr/local/lib
```

# V8

Download V8 (via git or svn) and switch to branch 3.22. Afterwards, run the following:

```
[~/v8 $] make dependencies
[~/v8 $] patch -p1 < ~/pyv8-linux-x64/patches/v8.patch # Enables RTTI and Exception
[~/v8 $] make x64.release.check library=shared werror=no console=readline snapshot=on debuggersupport=on i18nsupport=off
```

## PyV8

Download PyV8 @ revision 557, and run the following:

```
[~/pyv8 $] patch -p1 < ~/pyv8-linux-x64/patches/pyv8.patch # Skip building V8
[~/pyv8 $] V8_HOME=/home/me/v8/ python setup.py build
```

Once built, copy the necessary build artifacts into the src folder.
