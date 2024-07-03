.. _choice-variables:

Choice Variables
----------------

*New in dxh_py 0.0.3*

Choice variables provide different choices when creating a project.
Depending on a user's choice the template renders things differently.

Basic Usage
~~~~~~~~~~~

Choice variables are regular key / value pairs, but with the value being a list of strings.

For example, if you provide the following choice variable in your ``dxh_py.json``:

.. code-block:: JSON

   {
       "license": ["MIT", "BSD-3", "GNU GPL v3.0", "Apache Software License 2.0"]
   }

you'd get the following choices when running dxh_py::

   Select license:
   1 - MIT
   2 - BSD-3
   3 - GNU GPL v3.0
   4 - Apache Software License 2.0
   Choose from 1, 2, 3, 4 [1]:

Depending on an user's choice, a different license is rendered by dxh_py.

The above ``license`` choice variable creates ``dxh_py.license``, which can be used like this:

.. code-block:: html+jinja

  {%- if dxh_py.license == "MIT" -%}
  # Possible license content here

  {%- elif dxh_py.license == "BSD-3" -%}
  # More possible license content here

  {% endif %}

dxh_py is using `Jinja2's if conditional expression <https://jinja.palletsprojects.com/en/latest/templates/#if>`_ to determine the correct license.

The created choice variable is still a regular dxh_py variable and can be used like this:

.. code-block:: html+jinja


  License
  -------

  Distributed under the terms of the `{{dxh_py.license}}`_ license,

Overwriting Default Choice Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choice Variables are overwritable using a :ref:`user-config` file.

For example, a choice variable can be created in ``dxh_py.json`` by using a list as value:

.. code-block:: JSON

   {
       "license": ["MIT", "BSD-3", "GNU GPL v3.0", "Apache Software License 2.0"]
   }

By default, the first entry in the values list serves as default value in the prompt.

Setting the default ``license`` agreement to *Apache Software License 2.0* can be done using:

.. code-block:: yaml

   default_context:
       license: "Apache Software License 2.0"

in the :ref:`user-config` file.

The resulting prompt changes and looks like::

  Select license:
  1 - Apache Software License 2.0
  2 - MIT
  3 - BSD-3
  4 - GNU GPL v3.0
  Choose from 1, 2, 3, 4 [1]:

.. note::
   As you can see the order of the options changed from ``1 - MIT`` to ``1 - Apache Software License 2.0``. **dxh_py** takes the first value in the list as the default.
