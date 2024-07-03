.. _templates-in-context-values:

Templates in Context Values
--------------------------------

The values (but not the keys!) of `dxh_py.json` are also Jinja2 templates.
Values from user prompts are added to the context immediately, such that one context value can be derived from previous values.
This approach can potentially save your user a lot of keystrokes by providing more sensible defaults.

Basic Example: Templates in Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python packages show some patterns for their naming conventions:

- a human-readable project name
- a lowercase, dashed repository name
- an importable, dash-less package name

Here is a `dxh_py.json` with templated values for this pattern:

.. code-block:: JSON

    {
      "project_name": "My New Project",
      "project_slug": "{{ dxh_py.project_name|lower|replace(' ', '-') }}",
      "pkg_name": "{{ dxh_py.project_slug|replace('-', '') }}"
    }

If the user takes the defaults, or uses `no_input`, the templated values will be:

- `my-new-project`
- `mynewproject`

Or, if the user gives `Yet Another New Project`, the values will be:

- ``yet-another-new-project``
- ``yetanothernewproject``
