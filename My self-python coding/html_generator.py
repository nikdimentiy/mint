# # Another rewarding day in the fast-paced world of WebDev. Man, you love your job! But as with any job, somtimes things can get a little tedious.
# Part of the website you're working on has a very repetitive structure,
# # and writing all the HTML by hand is a bore. Time to automate! You want to write some functions that will generate the HTML for you.

# # To organize your code, make of all your functions methods of a class called HTMLGen.
# Tag functions should be named after the tag of the element they create.
#  Each function will take one argument, a string, which is the inner HTML of the element to be created.
# The functions will return the string for the appropriate HTML element.


class HTMLGen:

    def a(self, strng):
        return "<a>{}</a>".format(strng)

    def p(self, strng):
        return "<p>{}</p>".format(strng)

    def b(self, strng):
        return "<b>{}</b>".format(strng)

    def body(self, strng):
        return "<body>{}</body>".format(strng)

    def div(self, strng):
        return "<div>{}</div>".format(strng)

    def span(self, strng):
        return "<span>{}</span>".format(strng)

    def title(self, strng):
        return "<title>{}</title>".format(strng)

    def comment(self, strng):
        return "<!--{}-->".format(strng)
