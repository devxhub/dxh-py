.. _calling-from-python:

Calling dxh_py Functions From Python
------------------------------------------

You can use dxh_py from Python:

.. code-block:: python

    from dxh_py.main import dxh_py

    # Create project from the dxh_py/ template
    dxh_py('dxh_py/')

    # Create project from the dxh_py.git repo template
    dxh_py('https://github.com/devxhub/dxh-py.git')

This is useful if, for example, you're writing a web framework and need to provide developers with a tool similar to `django-admin.py startproject` or `npm init`.

See the :ref:`API Reference <apiref>` for more details.
