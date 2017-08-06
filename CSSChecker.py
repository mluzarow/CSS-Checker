import CSSFile

def getPath ():
    from sys import argv
    
    if (len (argv) != 2):
        print ("Incorrect number of arguments.")
        exit ();

    print ("Loading file: %s" % argv[1])

    return (argv[1])

def openFile (path):
    try:
        with open (path, 'r') as f:
            data = f.read ()
        f.closed

        return (data)
    except:
        print ("Something bad happened.")

if (__name__ == "__main__"):
    path = getPath ()
    rawData = openFile (path)

    test = CSSFile.Property ("left", "butt")

    print (CSSFile.validateProperty (test))
    
    
