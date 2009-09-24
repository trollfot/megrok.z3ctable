import martian

class table(martian.Directive):
    scope = martian.CLASS
    store = martian.ONCE
    validate = martian.validateInterfaceOrClass

