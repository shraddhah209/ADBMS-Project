import re
from django import template
from django.conf import settings

numeric_test = re.compile("^\d+$")
register = template.Library()


def getattribute(value, arg):
    if "." in str(arg):
        firstarg = str(arg).split(".")[0]
        value = getattribute(value, firstarg)
        arg = ".".join(str(arg).split(".")[1:])
        return getattribute(value, arg)
    if hasattr(value, str(arg)):
        return getattr(value, arg)
    elif hasattr(value, 'has_key') and value.has_key(arg):
        return value[arg]
    elif numeric_test.match(str(arg)) and len(value) > int(arg):
        return value[int(arg)]
    else:
        # return settings.TEMPLATE_STRING_IF_INVALID
        return 'no attr.' + str(arg) + 'for:' + str(value)


register.filter('getattribute', getattribute)


