

class HtmlNode:

    def __init__(self, tag=None, value=None, childern=None, props=None):
        self.tag = tag # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.childern = childern # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}


        """ An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes """


    def to_html(self):
        # Child classes will override this method to render themselves as HTML.
        raise NotImplementedError("Child class must use this method")


    def props_to_html(self):
        if self.props == None:
            return ""

        attr_str = ""
        #print(self.props)
        for attr, value in self.props.items():
            attr_str += f' {attr}="{value}"'

        return attr_str

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, childern: {self.childern}, {self.props})"
    



class LeafNode(HtmlNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value == "":
            raise ValueError("Must have a value")

        if self.tag == None:
            return self.value
        else:
            
            if self.props != None:
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'

    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"




class ParentNode(HtmlNode):

    def __init__(self, tag, childern, props=None):
        super().__init__(tag, None, childern, props)


    def to_html(self):
        comb_childern = ""
        if self.tag is None:
            raise ValueError("A tag is required.")
        elif self.childern is None:
            raise ValueError("A list of HtmlNode object/childern required.")
        else:
            #print(f"---------> {self.childern[count]}")
            for child in self.childern:
                comb_childern += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{comb_childern}</{self.tag}>"



    def __repr__(self):
        return f"ParentNode({self.tag}, childern: {self.childern}, {self.props})"




