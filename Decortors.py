def bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
def underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
def itlaic(fn):
    def wrapped():
        return "<i>" + fn() + "</u>"
    return wrapped
@bold
@underline
@itlaic
def name():
    return "Brady"
print(name())