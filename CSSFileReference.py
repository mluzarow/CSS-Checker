from re import compile

PROPERTIES = dict ()
PROPERTIES ["left_re"] = compile ("^(\-?\d+(px|%|vw|vh))|0$")
PROPERTIES ["left"] = ["auto", "inherit", "initial"]
