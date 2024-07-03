.. _copy-without-render:

Copy without Render
-------------------

*New in dxh_py 0.0.3*

To avoid rendering directories and files of a dxh_py, the ``_copy_without_render`` key can be used in the ``dxh_py.json``.
The value of this key accepts a list of Unix shell-style wildcards:

.. code-block:: JSON

    {
        "project_slug": "sample",
        "_copy_without_render": [
            "*.html",
            "*not_rendered_dir",
            "rendered_dir/not_rendered_file.ini"
        ]
    }

**Note**:
Only the content of the files will be copied without being rendered.
The paths are subject to rendering.
This allows you to write:

.. code-block:: JSON

    {
        "project_slug": "sample",
        "_copy_without_render": [
            "{{dxh_py.repo_name}}/templates/*.html",
        ]
    }

In this example, ``{{dxh_py.repo_name}}`` will be rendered as expected but the html file content will be copied without rendering.
