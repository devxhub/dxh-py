.. _private-variables:

Private Variables
-----------------

dxh_py allows the definition private variables by prepending an underscore to the variable name.
The user will not be required to fill those variables in.
These can either be not rendered, by using a prepending underscore, or rendered, prepending a double underscore.
For example, the ``dxh_py.json``:

.. code-block:: JSON

    {
        "project_name": "Really cool project",
        "_not_rendered": "{{ dxh_py.project_name|lower }}",
        "__rendered": "{{ dxh_py.project_name|lower }}"
    }

Will be rendered as:

.. code-block:: JSON

    {
        "project_name": "Really cool project",
        "_not_rendered": "{{ dxh_py.project_name|lower }}",
        "__rendered": "really cool project"
    }

The user will only be asked for ``project_name``.

Non-rendered private variables can be used for defining constants.
An example of where you may wish to use private **rendered** variables is creating a Python package repository and want to enforce naming consistency.
To ensure the repository and package name are based on the project name, you could create a ``dxh_py.json`` such as:

.. code-block:: JSON

    {
        "project_name": "Project Name",
        "__project_slug": "{{ dxh_py.project_name|lower|replace(' ', '-') }}",
        "__package_name": "{{ dxh_py.project_name|lower|replace(' ', '_') }}",
    }

Which could create a structure like this::

    project-name
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    └── src
        ├── project_name
        │   └── __init__.py
        ├── setup.py
        └── tests
            └── __init__.py

The ``README.md`` can then have a plain English project title.
