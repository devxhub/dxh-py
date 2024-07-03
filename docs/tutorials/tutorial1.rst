=============================
Getting to Know dxh_py
=============================

.. note:: Before you begin, please install dxh_py 0.0.2 or higher.
   Instructions are in :doc:`../installation`.

dxh_py is a tool for creating projects from *dxh_pys* (project templates).

What exactly does this mean? Read on!

Case Study: dxh_py
-----------------------------------

*dxh_py* is a dxh_py template that creates the starter boilerplate for a Python package.

.. note:: There are several variations of it, but for this tutorial we'll use
   the original version at https://github.com/devxhub/dxh_py/.

Step 1: Generate a Python Package Project
------------------------------------------

Open your shell and cd into the directory where you'd like to create a starter Python package project.

At the command line, run the dxh_py command, passing in the link to dxh_py's HTTPS clone URL like this:

.. code-block:: bash

    $ dxh_py https://github.com/devxhub/dxh_py.git

Local Cloning of Project Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, dxh_py gets cloned to `~/.dxh_pys/` (or equivalent on Windows).
dxh_py does this for you, so sit back and wait.

Local Generation of Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When cloning is complete, you will be prompted to enter a bunch of values, such as `full_name`, `email`, and `project_name`.
Either enter your info, or simply press return/enter to accept the default values.

This info will be used to fill in the blanks for your project.
For example, your name and the year will be placed into the LICENSE file.

Step 2: Explore What Got Generated
----------------------------------

In your current directory, you should see that a project got generated:

.. code-block:: bash

    $ ls
    boilerplate

Looking inside the `boilerplate/` (or directory corresponding to your `project_slug`) directory, you should see something like this:

.. code-block:: bash

    $ ls boilerplate/
    MANIFEST.in      docs          
    Makefile         requirements.txt
    README.rst       setup.py
    LICENSE.md          boilerplate      

That's your new project!
Great, you just generated a skeleton Python package.
How did that work?

Step 3: Observe How It Was Generated
------------------------------------

Let's take a look at dxh_py together. Open https://github.com/devxhub/dxh_py in a new browser window.

{{ dxh_py.project_slug }}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the directory called `{{ dxh_py.project_slug }}`.
Click on it.
Observe the files inside of it.
You should see that this directory and its contents corresponds to the project that you just generated.

This happens in `find.py`, where the `find_template()` method looks for the first jinja-like directory name that starts with `dxh_py`.

dxh_py.json
~~~~~~~~~~~~~~~~~

Now navigate back up to `dxh_py/` and look at the `dxh_py.json` file.

You should see JSON that corresponds to the prompts and default values shown earlier during project generation:

.. code-block:: json

    {
        "full_name": "DEVxHUB",
        "email": "tech@devxhub.com",
        "github_username": "devxhub",
        "project_name": "Django Boilerplate",
        "project_slug": "{{ dxh_py.project_name.lower().replace(' ', '_') }}",
        "project_short_description": "Python Boilerplate contains all the boilerplate you need to create a Python package.",
        "pypi_username": "{{ dxh_py.github_username }}",
        "version": "0.1.0",
        "use_pytest": "n",
        "use_pypi_deployment_with_travis": "y",
        "create_author_file": "y",
        "open_source_license": ["MIT", "BSD", "ISCL", "Apache Software License 2.0", "Not open source"]
    }

Questions?
----------

If anything needs better explanation, please take a moment to file an issue at https://github.com/devxhub/dxh_py/issues with what could be improved
about this tutorial.

Summary
-------

You have learned how to use dxh_py to generate your first project from a dxh_py project template.

In tutorial 2 (:ref:`tutorial2`), you'll see how to create dxh_pys of your own, from scratch.
