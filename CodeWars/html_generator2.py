class HTMLGen(object):
    """
    A dynamic HTML generator class that automatically creates HTML tag methods on-the-fly.
    
    This class uses Python's __getattr__ magic method to dynamically generate HTML elements.
    Any attribute called on this class will be treated as an HTML tag name and will return
    a function that wraps text in that HTML tag.
    
    Methods are created dynamically, so you can use any valid HTML tag name as a method.
    Special case: using 'comment' will create an HTML comment.
    
    Examples:
        >>> html = HTMLGen()
        >>> html.p("Hello World")
        '<p>Hello World</p>'
        >>> html.div("Content")
        '<div>Content</div>'
        >>> html.comment("This is a comment")
        '<!--This is a comment-->'
    """
    
    def __getattr__(self, name):
        """
        Magic method that handles undefined attribute access.
        
        Args:
            name (str): The name of the called method (will be used as HTML tag)
            
        Returns:
            function: A wrapper function that generates HTML elements
        """
        def wrapper(text):
            # Special case for HTML comments
            if name == "comment":
                return "<!--{0}-->".format(text)
            # Generate regular HTML tags
            else:
                return "<{0}>{1}</{0}>".format(name, text)
        return wrapper

# Driver code
if __name__ == "__main__":
    # Create an instance of HTMLGen
    html = HTMLGen()
    
    # Test various HTML tags
    test_cases = [
        ("p", "This is a paragraph"),
        ("div", "This is a div"),
        ("span", "This is a span"),
        ("h1", "This is a heading"),
        ("comment", "This is a comment"),
        ("custom", "This is a custom tag")
    ]
    
    print("HTML Generator Test Results:")
    print("-" * 50)
    
    # Test each case and print results
    for tag, content in test_cases:
        # Get the method dynamically and call it
        method = getattr(html, tag)
        result = method(content)
        print(f"Tag: {tag}")
        print(f"Content: {content}")
        print(f"Result: {result}")
        print("-" * 50)
        
    # Example of chaining (creating nested structures)
    nested = html.div(
        html.p("This is a paragraph inside a div")
    )
    print("Nested Structure Example:")
    print(nested)
