# # Another rewarding day in the fast-paced world of WebDev. Man, you love your job! But as with any job, somtimes things can get a little tedious.
# Part of the website you're working on has a very repetitive structure,
# # and writing all the HTML by hand is a bore. Time to automate! You want to write some functions that will generate the HTML for you.

# # To organize your code, make of all your functions methods of a class called HTMLGen.
# Tag functions should be named after the tag of the element they create.
#  Each function will take one argument, a string, which is the inner HTML of the element to be created.
# The functions will return the string for the appropriate HTML element.


class HTMLGen(object):
    def __getattr__(self, name):
        def wrapper(text):
            if name == "comment":
                return "<!--{0}-->".format(text)
            else:
                return "<{0}>{1}</{0}>".format(name, text)
        return wrapper
