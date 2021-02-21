def outer_function():
    var = 8  # creating a local var variable

    def inner_function():
        # specifies that a global variable should be used
        global var
        print(var)  # 0
        var = 10

    print(var)  # 8
    inner_function()  # calling an internal(inner) function
    print(var)  # 8


# creating a global (var) variable
var = 0
print(var)  # 0
outer_function()
print(var)  # 10
