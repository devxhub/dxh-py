=====
Usage
=====

Grab a dxh_py template
----------------------------

First, clone a dxh_py project template::

    $ git clone https://github.com/devxhub/dxh_py.git

Make your changes
-----------------

Modify the variables defined in `dxh_py.json`.

Open up the skeleton project. If you need to change it around a bit, do so.

You probably also want to create a repo, name it differently, and push it as
your own new dxh_py project template, for handy future use.

Generate your project
---------------------

Then generate your project from the project template::

    $ dxh_py dxh_py/

The only argument is the input directory. (The output directory is generated
by rendering that, and it can't be the same as the input directory.)

.. note:: see :ref:`command_line_options` for extra command line arguments

Try it out!



Works directly with git and hg (mercurial) repos too
------------------------------------------------------

To create a project from the dxh_py.git repo template::

    $ dxh_py gh:devxhub/dxh_py

dxh_py knows abbreviations for Github (``gh``), Bitbucket (``bb``), and
GitLab (``gl``) projects, but you can also give it the full URL to any
repository::

    $ dxh_py https://github.com/devxhub/dxh_py.git
    $ dxh_py git+ssh://git@github.com/devxhub/dxh_py.git
    $ dxh_py hg+ssh://hg@bitbucket.org/audreyr/dxh_py

You will be prompted to enter a bunch of project config values. (These are
defined in the project's `dxh_py.json`.)

Then, dxh_py will generate a project from the template, using the values
that you entered. It will be placed in your current directory.

And if you want to specify a branch you can do that with::

    $ dxh_py https://github.com/devxhub/dxh_py.git --checkout develop

Works with private repos
------------------------

If you want to work with repos that are not hosted in github or bitbucket you can indicate explicitly the
type of repo that you want to use prepending `hg+` or `git+` to repo url::

    $ dxh_py hg+https://example.com/repo

In addition, one can provide a path to the dxh_py stored
on a local server::

    $ dxh_py file://server/folder/project.git

Works with Zip files
--------------------

You can also distribute dxh_py templates as Zip files. To use a Zip file
template, point dxh_py at a Zip file on your local machine::

    $ dxh_py /path/to/template.zip

Or, if the Zip file is online::

    $ dxh_py https://example.com/path/to/template.zip

If the template has already been downloaded, or a template with the same name
has already been downloaded, you will be prompted to delete the existing
template before proceeding.

The Zip file contents should be the same as a git/hg repository for a template -
that is, the zipfile should unpack into a top level directory that contains the
name of the template. The name of the zipfile doesn't have to match the name of
the template - for example, you can label a zipfile with a version number, but
omit the version number from the directory inside the Zip file.

If you want to see an example Zipfile, find any dxh_py repository on Github
and download that repository as a zip file - Github repository downloads are in
a valid format for dxh_py.

Password-protected Zip files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your repository Zip file is password protected, dxh_py will prompt you
for that password whenever the template is used.

Alternatively, if you want to use a password-protected Zip file in an
automated environment, you can export the `dxh_py_REPO_PASSWORD`
environment variable; the value of that environment variable will be used
whenever a password is required.

Keeping your dxh_pys organized
------------------------------------

As of the dxh_py 0.7.0 release:

* Whenever you generate a project with a dxh_py, the resulting project
  is output to your current directory.

* Your cloned dxh_pys are stored by default in your `~/.dxh_pys/`
  directory (or Windows equivalent). The location is configurable: see
  :doc:`advanced/user_config` for details.

Pre-0.7.0, this is how it worked:

* Whenever you generate a project with a dxh_py, the resulting project
  is output to your current directory.

* Cloned dxh_pys were not saved locally.
