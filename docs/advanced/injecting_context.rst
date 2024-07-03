.. _injecting-extra-content:

Injecting Extra Context
-----------------------

You can specify an ``extra_context`` dictionary that will override values from ``dxh_py.json`` or ``.dxh_pyrc``:

.. code-block:: python

    dxh_py(
        'dxh_py/',
        extra_context={'project_name': 'TheGreatest'},
    )

This works as command-line parameters as well:

.. code-block:: bash

    dxh_py --no-input dxh_py/ project_name=TheGreatest

You will also need to add these keys to the ``dxh_py.json`` or ``.dxh_pyrc``.


Example: Injecting a Timestamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have ``dxh_py.json`` that has the following keys:

.. code-block:: JSON

    {
        "timestamp": "{{ dxh_py.timestamp }}"
    }


This Python script will dynamically inject a timestamp value as the project is
generated:

.. code-block:: python

    from dxh_py.main import dxh_py

    from datetime import datetime

    dxh_py(
        'dxh_py-django',
        extra_context={'timestamp': datetime.utcnow().isoformat()}
    )

How this works:

1. The script uses ``datetime`` to get the current UTC time in ISO format.
2. To generate the project, ``dxh_py()`` is called, passing the timestamp
   in as context via the ``extra_context``` dict.
