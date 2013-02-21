Example Usage
===

Python module to create deep, formatted viualization of python dictionaries and lists

spprint
---

To visualize an object using `spprint`:

    import spprint
    
    data = {'boolean':True,'string':"Test",'dict':{'a':1,'b':2},'array':['a',False,4.5]}
    
    print spprint.spprint(data,"Full Glory")
    print spprint.spprint(data,name="Compact",whitespace=' ',indexFormat=False)

would output

    Full Glory = {
        array : [
            0 : 'a',
            1 : False,
            2 : 4.5
        ]
        boolean : True,
        dict : {
            a : 1,
            b : 2
        }
        string : 'Test'
    }
    
    Compact = { array : [ 'a', False, 4.5 ] boolean : True, dict : { a : 1, b : 2 } string : 'Test' } 
  

