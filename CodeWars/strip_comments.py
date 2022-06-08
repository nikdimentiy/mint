""" 
Strip Comments

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out.

Example

Given an input string of :

apples, pears # and bananas
grapes
bananas !apples

The output expected would be :

apples, pears
grapes
bananas

The code would be called like so :

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas""""



def strip_comments(strng, markers):
    s = strng.split("\n")
    result = ""
    for i in s:
        trimmed = ""
        for j in i:
            if j not in markers:
                trimmed += j
            else:
                break
        trimmed = trimmed.rstrip()
        result = result + trimmed + "\n"
    return result[:-1]
