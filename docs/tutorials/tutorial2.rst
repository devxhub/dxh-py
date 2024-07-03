.. _tutorial2:

==================================
Create a dxh_py From Scratch
==================================

In this tutorial, we are creating `dxh_py-website-simple`, a dxh_py for generating simple, bare-bones websites.

Step 1: Name Your dxh_py
------------------------------

Create the directory for your dxh_py and cd into it:

.. code-block:: bash

    $ mkdir dxh_py-website-simple
    $ cd dxh_py-website-simple/

Step 2: Create dxh_py.json
----------------------------------

`dxh_py.json` is a JSON file that contains fields which can be referenced in the dxh_py template. For each, default value is defined and user will be prompted for input during dxh_py execution. Only mandatory field is `project_slug` and it should comply with package naming conventions defined in `PEP8 Naming Conventions <https://www.python.org/dev/peps/pep-0008/#package-and-module-names>`_ .

.. code-block:: json

    {
      "project_name": "dxh_py Website Simple",
      "project_slug": "{{ dxh_py.project_name.lower().replace(' ', '_') }}",
      "author": "Anonymous"
    }


Step 3: Create project_slug Directory
---------------------------------------

Create a directory called `{{ dxh_py.project_slug }}`.

This value will be replaced with the repo name of projects that you generate from this dxh_py.

Step 4: Create index.html
--------------------------

Inside of `{{ dxh_py.project_slug }}`, create `index.html` with following content:

.. code-block:: html

    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>{{ dxh_py.project_name }}</title>
        </head>

        <body>
            <h1>{{ dxh_py.project_name }}</h1>
            <p>by {{ dxh_py.author }}</p>
        </body>
    </html>

Step 5: Pack dxh_py into ZIP
----------------------------------
There are many ways to run dxh_py templates, and they are described in details in `Usage chapter <https://dxh_py.readthedocs.io/en/latest/usage.html#grab-a-dxh_py-template>`_. In this tutorial we are going to ZIP dxh_py and then run it for testing.

By running following command `dxh_py.zip` will get generated which can be used to run dxh_py. Script will generate `dxh_py.zip` ZIP file and echo full path to the file.

.. code-block:: bash

   $ (SOURCE_DIR=$(basename $PWD) ZIP=dxh_py.zip && # Set variables
   pushd .. && # Set parent directory as working directory
   zip -r $ZIP $SOURCE_DIR --exclude $SOURCE_DIR/$ZIP --quiet && # ZIP dxh_py
   mv $ZIP $SOURCE_DIR/$ZIP && # Move ZIP to original directory
   popd && # Restore original work directory
   echo  "dxh_py full path: $PWD/$ZIP")

Step 6: Run dxh_py
------------------------
Set your work directory to whatever directory you would like to run dxh_py at. Use dxh_py full path and run the following command:

.. code-block:: bash

   $ dxh_py <replace with dxh_py full path>

You can expect similar output:

.. code-block:: bash

   $ dxh_py /Users/admin/dxh_py-website-simple/dxh_py.zip
   project_name [dxh_py Website Simple]: Test web
   project_slug [test_web]:
   author [Anonymous]: dxh_py Developer

Resulting directory should be inside your work directory with a name that matches `project_slug` you defined. Inside that directory there should be `index.html` with generated source:

.. code-block:: html

    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Test web</title>
        </head>

        <body>
            <h1>Test web</h1>
            <p>by dxh_py Developer</p>
        </body>
    </html>
