def func(var1,var2,*variable,**variable1):
    print("var1 ",var1)
    print("var2 ",var2)
    print("variable",variable)
    print("variable1",variable1)
    print (type(variable))
    print(type(variable1))
    for k,v in variable1.items():
        print(k)
        print(v)
func(1,2,3,4,5,6,7,name="taruna")