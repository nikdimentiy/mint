# Tiny python code: variable scope

def function():
    # the definition of a local variable
    var = "local variable"
    # displaying the value of a local variable on the screen
    print(var)


# the definition of a global variable
var = "global variable"
function()
# displaying the value of a global variable on the screen
print(var)
