.. _suppressing-command-line-prompts:

Suppressing Command-Line Prompts
--------------------------------

To suppress the prompts asking for input, use ``no_input``.

Note: this option will force a refresh of cached resources.

Basic Example: Using the Defaults
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dxh_py will pick a default value if used with ``no_input``:

.. code-block:: python

    from dxh_py.main import dxh_py
    dxh_py(
        'dxh_py-django',
        no_input=True,
    )

In this case it will be using the default defined in ``dxh_py.json`` or ``.dxh_pyrc``.

.. note::
   values from ``dxh_py.json`` will be overridden by values from  ``.dxh_pyrc``

Advanced Example: Defaults + Extra Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you combine an ``extra_context`` dict with the ``no_input`` argument, you can programmatically create the project with a set list of context parameters and without any command line prompts:

.. code-block:: python

    dxh_py('dxh_py/',
                 no_input=True,
                 extra_context={'project_name': 'TheGreatest'})


See also :ref:`injecting-extra-content` and the :ref:`API Reference <apiref>` for more details.
