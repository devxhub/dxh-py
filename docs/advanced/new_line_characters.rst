.. _new-lines:

Working with line-ends special symbols LF/CRLF
----------------------------------------------

*New in dxh_py 0.0.3*

.. note::

By default dxh_py checks every file at render stage and uses the same line end as in source.
This allow template developers to have both types of files in the same template.

The special template variable ``_new_lines`` enforces a specific line ending.
Acceptable variables: ``'\r\n'`` for CRLF and ``'\n'`` for POSIX.

Here is example how to force line endings to CRLF on any deployment:

.. code-block:: JSON

    {
        "project_slug": "sample",
        "_new_lines": "\r\n"
    }
