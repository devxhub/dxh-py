===============
Troubleshooting
===============

I created a dxh_py, but it doesn't work, and I can't figure out why
-------------------------------------------------------------------------

* Try upgrading to dxh_py 0.8.0, which prints better error
  messages and has fixes for several common bugs.

I'm having trouble generating Jinja templates from Jinja templates
------------------------------------------------------------------

Make sure you escape things properly, like this::

    {{ "{{" }}

Or this::

    {% raw %}
    <p>Go <a href="{{ url_for('home') }}">Home</a></p>
    {% endraw %}

Or this::

    {{ {{ url_for('home') }} }}

See https://jinja.palletsprojects.com/en/latest/templates/#escaping for more info.

You can also use the `_copy_without_render`_ key in your `dxh_py.json`
file to escape entire files and directories.

.. _`_copy_without_render`: http://dxh_py.readthedocs.io/en/latest/advanced/copy_without_render.html


Other common issues
-------------------

TODO: add a bunch of common new user issues here.

This document is incomplete. If you have knowledge that could help other users,
adding a section or filing an issue with details would be greatly appreciated.
