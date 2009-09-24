import martian
import grokcore.view 
import megrok.z3ctable
import grokcore.component 

from megrok.z3ctable.components import Column
from zope import component
from martian.error import GrokError
from z3c.table.interfaces import ITable
from grokcore.component.meta import default_provides # default_context
from zope.publisher.interfaces.browser import IDefaultBrowserLayer



class ColumnGrokker(martian.ClassGrokker):
    martian.component(Column)

    martian.directive(grokcore.view.layer,
                      default=IDefaultBrowserLayer)
                      

    martian.directive(grokcore.component.context) # Maybe we can use a default context

    martian.directive(megrok.z3ctable.table, default=ITable)

    martian.directive(grokcore.component.provides,
                      get_default=default_provides)
    martian.directive(grokcore.component.name)

    def execute(self, factory, config, layer, context, table, provides, name, **kw):
        for_ = (context, layer, table)
        config.action(
            discriminator=('adapter', for_, provides, name),
            callable=component.provideAdapter,
            args=(factory, for_, provides, name),
            )
        return True
    
