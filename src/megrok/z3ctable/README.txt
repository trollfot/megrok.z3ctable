===============
megrok.z3ctable
===============

The `megrok.z3ctable` package is a wrapper around the z3c.table
components. z3c.table allows you to define HTML tables as zope3
components, defining columns as multi adapters.

Thanks to megrok.z3ctable, these components are now fully available
in Grok, making them easy to declare and configure. The following
components are available :

  - Table
  - Column
  - Value

Beyond a simple wrapping, megrok.z3cform brings you new convenient
ways to create pages displaying a table :

  - TableView : a simple browser view displaying a table.
  - TablePage : a table browser view included in a layout
    (see megrok.layout)

For more information and more detailed examples please look in the
ftests directory of this package.


Getting started
---------------

First, we grok the package grokkers::

  >>> from megrok.z3ctable import testing
  >>> import grokcore.component as grok
  >>> testing.grok('megrok.z3ctable')
  

Test Setup
----------

Let's create simple items to demonstrate the package. Here, the
table will be the representation of a folder listing, displaying (in an
ordered way), the content of a simple container. 

  >>> from megrok.z3ctable.ftests import Container, Content
  >>> from zope.app.container import btree
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()

Let's create 2 dummy content :

  >>> christian = Content('Christian', 29)
  >>> trollfot = Content('Trollfot', 27) 

Then, we instanciate a container and store the 2 dummies inside :

  >>> container = Container()
  >>> container['christian'] = christian
  >>> container['trollfot'] = trollfot

  
A simple Table
--------------

We define a simple table. Here, the component only registers itself,
there's no logic defined inside.

  >>> from megrok.z3ctable import Table, Values 
  >>> from megrok.z3ctable import ITable

  >>> class SimpleTable(Table):
  ...    """ My Simple Table """

  >>> ITable.implementedBy(Table)
  True

Let's make an instance of the Table.

  >>> myTable = SimpleTable(container, request)
  >>> ITable.providedBy(myTable)
  True

Now, we need to feed our table with contents. In order to provide a
pluggable way to fetch the content, z3c.table proposes an adapter
called "Values". It is in charge of getting in the data to display.

  >>> class MyValues(Values):
  ...     grok.adapts(btree.BTreeContainer, None, SimpleTable)
  ...
  ...     @property
  ...     def values(self):
  ...         return self.context.values()

We grok the MyValues Adapter:

  >>> grok_component('MyValues', MyValues)
  True

  >>> myTable.update()
  >>> myTable.render()
  u''

There is currently no output this is because the table itself contains
no logic. The data is displayed by components called "Column". A
Column is a multi adapter, adapting the view, the request and the
table. It permits a very flexible handling of the tables and the data
representations. Let's define a simple Column :

  >>> from megrok.z3ctable import NameColumn
  >>> class Names(NameColumn):
  ...     grok.adapts(None, None, SimpleTable)

Now we grok our Column:

  >>> grok_component('Names', Names)
  True

and render the Table again.

  >>> myTable.update()
  >>> print myTable.render()
  <table>
    <thead>
      <tr>
        <th>Name</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>christian</td>
      </tr>
      <tr>
        <td>trollfot</td>
      </tr>
    </tbody>
  </table>

Here you go. A fully functional and pluggable table. Enjoy.