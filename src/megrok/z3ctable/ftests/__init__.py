import os.path
import grokcore.component as grok
import megrok.z3ctable

from zope.app.container import btree
from zope.app.testing.functional import ZCMLLayer


class Container(grok.Context, btree.BTreeContainer):
    """Example Container. 
    """
    __name__ = u'container'


class Content(grok.Context):
    """Example Content.
    """
    def __init__(self, title, number):
        self.title = title
        self.number = number


ftesting_zcml = os.path.join(os.path.dirname(megrok.z3ctable.__file__),
                             'ftesting.zcml')
FunctionalLayer = ZCMLLayer(ftesting_zcml, __name__, 'FunctionalLayer',
                            allow_teardown=True)
