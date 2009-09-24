import grokcore.component as grok
import grokcore.view as view 
import megrok.layout

from z3c.table import table
from z3c.table import column
from z3c.table import interfaces
from zope.publisher.publish import mapply


class Table(table.Table):
    """A table.
    """


class TableView(view.View, Table):
    """A view with renderd Tables
    """
    grok.baseclass()

    def update(self):
        Table.update(self)

    def render(self):
        return Table.render(self)

    # Mark this Method as not needed
    # We will get an error in the grokking Process
    # if we do this.
    render.base_method = True


class TablePage(megrok.layout.Page, Table):
    """A Page with a rendered Table
    """
    grok.baseclass()

    def update(self):
        Table.update(self)

    def render(self):
        template = getattr(self, 'template', None)
        if template is not None:
            return self.template.render(self)
        return self.renderTable() 
    
    render.base_method = True


class Column(column.Column):
    """ A Nbasic Column
    """
    grok.provides(interfaces.IColumn)


class NameColumn(column.NameColumn, Column):
    """ Name Column
    """


class GetAttrColumn(column.GetAttrColumn, Column):
    """ GetAttr Column
    """


class CheckBoxColumn(column.CheckBoxColumn, Column):
    """ CheckBox Column
    """


class LinkColumn(column.LinkColumn, Column):
    """ Link Column
    """


class ModifiedColumn(column.ModifiedColumn, Column):
    """ Modified Column
    """


class Values(grok.MultiAdapter):
    """ Adapter for custom Value Implementation
    """
    grok.baseclass()
    grok.provides(interfaces.IValues)

    def __init__(self, context, request, table):
        self.context = context
        self.request = request
        self.table = table

    @property
    def values(self):
        return NotImplementedError(
            """Your class must override the `Values` method."""
            )
