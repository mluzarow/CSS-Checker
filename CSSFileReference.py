from re import compile

GENERIC_NUMBERIC_RE = compile ("^(\-?\d+(px|%|vw|vh))|0|auto|initial|inherit$")

PROPERTIES = dict ()

#################################################
##
## Box Sizing Properties
##
#################################################
PROPERTIES ["top"] = GENERIC_NUMBERIC_RE
PROPERTIES ["right"] = GENERIC_NUMBERIC_RE
PROPERTIES ["bottom"] = GENERIC_NUMBERIC_RE
PROPERTIES ["left"] = GENERIC_NUMBERIC_RE

PROPERTIES ["clear"] = compile ("^none|left|right|both|initial|inherit$")
PROPERTIES ["clip"] = compile ("^((rect\(((\-?\d+(px|%|vw|vh))|0), ((\-?\d+(px|%|vw|vh))|0), ((\-?\d+(px|%|vw|vh))|0), ((\-?\d+(px|%|vw|vh))|0)\))|auto|initial|inherit)$")
PROPERTIES ["display"] = compile ("^inline|block|flex|inline-block|inline-flex|inline-table|list-item|run-in|table|table-caption|table-column-group|table-header-group|table-footer-group|table-row-group|table-cell|table-column|table-row|none|initial|inherit$")
PROPERTIES ["float"] = compile ("^none|left|right|initial|inherit$")

PROPERTIES ["margin"] = compile ("^((\-?\d+(px|%|vw|vh))|0|auto|initial|inherit)( ((\-?\d+(px|%|vw|vh))|0|auto|initial|inherit)){0,3}$")
PROPERTIES ["margin-top"] = GENERIC_NUMBERIC_RE
PROPERTIES ["margin-right"] = GENERIC_NUMBERIC_RE
PROPERTIES ["margin-bottom"] = GENERIC_NUMBERIC_RE
PROPERTIES ["margin-left"] = GENERIC_NUMBERIC_RE

PROPERTIES ["height"] = GENERIC_NUMBERIC_RE
PROPERTIES ["min-height"] = GENERIC_NUMBERIC_RE
PROPERTIES ["max-height"] = GENERIC_NUMBERIC_RE
PROPERTIES ["width"] = GENERIC_NUMBERIC_RE
PROPERTIES ["min-width"] = GENERIC_NUMBERIC_RE
PROPERTIES ["max-width"] = GENERIC_NUMBERIC_RE

PROPERTIES ["overflow"] = compile ("^visible|hidden|scroll|auto|initial|inherit$")
PROPERTIES ["overflow-x"] = compile ("^visible|hidden|scroll|auto|initial|inherit$")
PROPERTIES ["overflow-y"] = compile ("^visible|hidden|scroll|auto|initial|inherit$")

PROPERTIES ["padding"] = compile ("^((\-?\d+(px|%|vw|vh))|0|auto|initial|inherit)( ((\-?\d+(px|%|vw|vh))|0|auto|initial|inherit)){0,3}$")
PROPERTIES ["padding-top"] = GENERIC_NUMBERIC_RE
PROPERTIES ["padding-right"] = GENERIC_NUMBERIC_RE
PROPERTIES ["padding-bottom"] = GENERIC_NUMBERIC_RE
PROPERTIES ["padding-left"] = GENERIC_NUMBERIC_RE

PROPERTIES ["position"] = compile ("^static|absolute|fixed|relative|initial|inherit$")
PROPERTIES ["visibility"] = compile ("^visible|hidden|collapse|initial|inherit$")
PROPERTIES ["vertical-align"] = compile ("^(\-?\d+(px|%|vw|vh))|0|initial|inherit|baseline|sub|super|top|text-top|middle|bottom|text-bottom$")
PROPERTIES ["z-index"] = compile ("^(\-?\d+)|auto|initial|inherit$")