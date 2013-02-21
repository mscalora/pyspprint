#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    spprint
    ~~

    Python module to create deep, formatted viualization of python dictionaries and lists

    Example Usage
    =============

    To directly print the representation of an object use `spprint`::

        import json, sys

        whatsit = json.load(sys.argv[1])
        print spprint(whatsit,"What's it?")

"""

def spprint(any,name=None,level=0,indent="    ",comma=',',indexFormat="{:d}",useStr=False,whitespace=False):
    """
        any - any dictionary, list, primitive or something that has a __str
        name - option name or label of any
        level - starting indent level
        indent - used used to indent each nested level of any
        comma - use this string for commas between list and dictionary items, normally ','
        indexFormat - None to disable list indexes, otherwise Format Specification Mini-Language string defaults to "{:d}"
        useStr - use str() instead of repr() to stringify objects that are not dictionaries, list or primitives
        whitespace - True (default) use lots of whitespace and indenting, False use none, otherwise use this value as whitespace
    """
    return _spprint(any,name=name,level=level,indent=indent,comma=comma,indexFormat=indexFormat,useStr=useStr,whitespace=whitespace)

def _spprint(any,name=None,level=0,indent="    ",comma=',',prefix="",arrayItem=False,indexFormat="{:d}",dictItem=False,useStr=False,whitespace=False,last=True):
    _nl = "\n" if whitespace==False else ("" if whitespace==True else whitespace)
    _indent = '' if whitespace else indent*level
    _space = '' if whitespace==True else ' '
    s = prefix
    s += _indent + (name + (_space+":"+_space if dictItem or arrayItem else _space+"="+_space) if name and not (arrayItem and indexFormat==False) else "")
    if isinstance(any,dict):
        s += "{" + _nl
        l = len(any)
        for i, key in enumerate(sorted(any.keys())):
            value = any[key]
            s = _spprint(value,name=key,prefix=s,indent=indent,comma=comma,level=level+1,dictItem=True,indexFormat=indexFormat,useStr=useStr,whitespace=whitespace,last=i==l-1)
        s += _indent + "}" + _nl
    elif isinstance(any,list):
        s += "[" + _nl
        l = len(any)
        for i, item in enumerate(any):
            s = _spprint(item,'' if indexFormat==False else indexFormat.format(i),prefix=s,indent=indent,comma=comma,level=level+1,arrayItem=True,indexFormat=indexFormat,useStr=useStr,whitespace=whitespace,last=i==l-1)
        s += _indent + "]" + _nl
    else:
        s += (str(any) if useStr else repr(any)) + ('' if comma==None or last else comma) + _nl
    return s

def main():
    # unit tests here
    print spprint(True);
    print spprint(False,"Boolean");

    print spprint(123);
    print spprint(123.56,name="Number");

    print spprint("abc");
    print spprint("abc\n\"def\"\n'ghi'",name="String");

    print spprint({});
    print spprint({'a':1,'b':"2"});
    print spprint({'c':1,'d':"2"},name="Map");

    print spprint(["a",2,{'a':1,'b':False,'c':'three'},True]);
    print spprint(["a",2,True,{'a':1,'b':False,'c':'three'}],name="Array");
    print spprint([{'a':1,'b':False,'c':'three'},"a",2,True],name="Tabbed",indent="\t");
    print spprint([{'a':1,'b':False,'c':'three'},"a",2,True],name="Commaless",comma=None);
    print spprint([{'a':1,'b':False,'c':'three'},"a",2,True],name="Numberless",indexFormat=False);
    print spprint(range(20),name="Hex",indexFormat="0x{:04x}");

    print spprint(["a",{'a':1,'b':False,'c':'three'},2,True],whitespace=True);
    print spprint(["a",2,True,{'a':1,'b':False,'c':'three'}],name="Array",whitespace=True);
    print spprint([{'a':1,'b':False,'c':'three'},"a",2,True],name="Numberless",indexFormat=False,indent='.',whitespace=True);
    print spprint([{'a':1,'b':False,'c':'three'},"a",2,True],name="Padded",indexFormat="{:04}",indent='.',whitespace=True);
    print spprint(range(18),name="Hex",indexFormat="{:x}",indent='.',whitespace=True);

    print spprint(["a",{'a':1,'b':False,'c':'three'},2,True],whitespace=' ');
    print spprint(["a",2,True,{'a':1,'b':False,'c':'three'}],name="Array",whitespace=' ');
    print spprint([{'a':1,'b':False,'c':'three'},"a",2,True],name="Numberless",indexFormat=False,indent='.',whitespace=' ');

    pass



if __name__ == "__main__":
    main()