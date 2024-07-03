.. _user-config:

User Config
===========

*New in dxh_py 0.0.3*

If you use dxh_py a lot, you'll find it useful to have a user config file.
By default dxh_py tries to retrieve settings from a `.dxh_pyrc` file in your home directory.

*New in dxh_py 0.0.3*

You can also specify a config file on the command line via ``--config-file``.

.. code-block:: bash

    dxh_py --config-file /home/devxhub/my-custom-config.yaml dxh_py

Or you can set the ``dxh_py_CONFIG`` environment variable:

.. code-block:: bash

    export dxh_py_CONFIG=/home/devxhub/my-custom-config.yaml

If you wish to stick to the built-in config and not load any user config file at all, use the CLI option ``--default-config`` instead.
Preventing dxh_py from loading user settings is crucial for writing integration tests in an isolated environment.

Example user config:

.. code-block:: yaml

    default_context:
        full_name: "DEVxHUB"
        email: "tech@devxhub.com"
        github_username: "devxhub"
    dxh_pys_dir: "/home/devxhub/my-custom-dxh_pys-dir/"
    replay_dir: "/home/devxhub/my-custom-replay-dir/"
    abbreviations:
        pp: https://github.com/devxhub/dxh_py.git
        gh: https://github.com/{0}.git
        bb: https://bitbucket.org/{0}

Possible settings are:

``default_context``:
    A list of key/value pairs that you want injected as context whenever you generate a project with dxh_py.
    These values are treated like the defaults in ``dxh_py.json``, upon generation of any project.
``dxh_pys_dir``
    Directory where your dxh_pys are cloned to when you use dxh_py with a repo argument.
``replay_dir``
    Directory where dxh_py dumps context data to, which you can fetch later on when using the
    :ref:`replay feature <replay-feature>`.
``abbreviations``
    A list of abbreviations for dxh_pys.
    Abbreviations can be simple aliases for a repo name, or can be used as a prefix, in the form ``abbr:suffix``.
    Any suffix will be inserted into the expansion in place of the text ``{0}``, using standard Python string formatting.
    With the above aliases, you could use the ``dxh_py`` template simply by saying ``dxh_py pp``, or ``dxh_py gh:devxhub/dxh_py``.
    The ``gh`` (GitHub), ``bb`` (Bitbucket), and ``gl`` (Gitlab) abbreviations shown above are actually **built in**, and can be used without defining them yourself.

Read also: :ref:`injecting-extra-content`
