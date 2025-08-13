.. rst-class:: hide-header

.. image:: _static/click-logo.png

Welcome to AsyncClick
=====================

.. image:: _static/click-name.svg
    :align: center
    :height: 200px

AsyncClick ist a fork of Click that works well with (some) async
frameworks. Supported: asyncio, trio, and curio.

Click, in turn, is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit".  It's highly configurable but comes with
sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun
while also preventing any frustration caused by the inability to implement
an intended CLI API.

AsyncClick in four points:

-   arbitrary nesting of commands
-   automatic help page generation
-   supports lazy loading of subcommands at runtime
-   seamlessly use async-enabled command and subcommand handlers

What does it look like?  Here is an example of a simple Click program:

.. click:example::

    import asyncclick as click
    import anyio

    @click.command()
    @click.option('--count', default=1, help='Number of greetings.')
    @click.option('--name', prompt='Your name',
                  help='The person to greet.')
    async def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        for x in range(count):
            if x: await anyio.sleep(0.1)
            click.echo(f"Hello {name}!")

    if __name__ == '__main__':
        hello()

And what it looks like when run:

.. click:run::

    invoke(hello, ['--count=3'], prog_name='python hello.py', input='John\n')

It automatically generates nicely formatted help pages:

.. click:run::

    invoke(hello, ['--help'], prog_name='python hello.py')

You can get the library directly from PyPI::

    pip install asyncclick

Documentation
-------------

.. note::

    asyncclick closely tracks click's releases and development.
    In order to streamline this process, the documentation was changed
    as lightly as possible. Thus, the author decided not to mangle the
    text and did not replace ``click`` with ``asyncclick``.

    Please adjust all ``import click`` statements to
    ``import asyncclick as click``, or apply similar changes, as required.

This part of the documentation guides you through all of the library's
usage patterns.

.. toctree::
   :maxdepth: 2

   faqs

Tutorials
------------
.. toctree::
   :maxdepth: 1

   quickstart
   virtualenv

How to Guides
---------------
.. toctree::
   :maxdepth: 1

   entry-points
   setuptools
   support-multiple-versions

Conceptual Guides
-------------------
.. toctree::
   :maxdepth: 1

   why
   click-concepts

General Reference
--------------------

.. toctree::
   :maxdepth: 1

   parameters
   parameter-types
   options
   option-decorators
   arguments
   commands-and-groups
   commands
   documentation
   prompts
   handling-files
   advanced
   complex
   extending-click
   testing
   utils
   shell-completion
   exceptions
   unicode-support
   wincmd

API Reference
-------------------

.. toctree::
   :maxdepth: 2

   api

About Project
===============

* This documentation is structured according to `Diataxis <https://diataxis.fr/>`_

* `Version Policy <https://palletsprojects.com/versions>`_

* `Contributing <https://palletsprojects.com/contributing/>`_

* `Donate <https://palletsprojects.com/donate>`_

.. toctree::
   :maxdepth: 1

   contrib
   license
   changes
