.. _directories:

Organizing dxh_pys in directories
---------------------------------------

*New in dxh_py 0.0.3*

dxh_py introduces the ability to organize several templates in one repository or zip file, separating them by directories.
This allows using symlinks for general files.
Here's an example repository demonstrating this feature::

    https://github.com/user/repo-name.git
        ├── directory1-name/
        |   ├── {{dxh_py.project_slug}}/
        |   └── dxh_py.json
        └── directory2-name/
            ├── {{dxh_py.project_slug}}/
            └── dxh_py.json

To activate one of templates within a subdirectory, use the ``--directory`` option:

.. code-block:: bash

    dxh_py https://github.com/user/repo-name.git --directory="directory1-name"
