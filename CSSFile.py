import CSSFileReference
from re import match

class SelectorBlock:
    def __init__ (self, selectors = list (), properties = list ()):
        self.selectors = selectors
        self.properties = properties

class Selector:
    def __init__ (self):
        pass

class Property:
    def __init__ (self, keyword, argument):
        self.keyword = keyword
        self.argument = argument

def validateProperty (property):
    valid = validatePropertyKeyword (property.keyword)

    if (valid):
        valid = validatePropertyArgument (property.keyword, property.argument)

    return (valid)

def validatePropertyKeyword (key):
    if (not (key in CSSFileReference.PROPERTIES)):
        print ("The value [%s] is not a valid CSS property." % key)
        return (False)
    return (True)

def validatePropertyArgument (key, arg):
    if (match (CSSFileReference.PROPERTIES ["%s_re" % key], arg) == None):
        if (not (arg in CSSFileReference.PROPERTIES [key])):
            print ("The argument [%s] is not valid for the property [%s]" % (arg, key))
            return (False)
    return (True)
        
