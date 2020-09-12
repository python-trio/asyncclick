asyncclick
==========

What's AsyncClick?
------------------

AsyncClick is a fork of Click that works well with trio, asyncio, or
curio.

Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary. It's the "Command
Line Interface Creation Kit". It's highly configurable but comes with
sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun
while also preventing any frustration caused by the inability to
implement an intended CLI API.

AsyncClick in four points:

-   Arbitrary nesting of commands
-   Automatic help page generation
-   Supports lazy loading of subcommands at runtime
-   Seamlessly use async-enabled command and subcommand handlers

Installing
----------

Install and update using `pip`_:

.. code-block:: text

    $ pip install asyncclick

AsyncClick supports Python 3.5 and newer, and PyPy3.

.. _pip: https://pip.pypa.io/en/stable/quickstart/

A Simple Example
----------------

What does it look like? Here is an example of a simple Click program:

.. code-block:: python

    import anyio
    import asyncclick as click
    
    @click.command()
    @click.option("--count", default=1, help="Number of greetings.")
    @click.option("--name", prompt="Your name",
                  help="The person to greet.")
    async def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        for x in range(count):
            if x: await anyio.sleep(0.1)
            click.echo("Hello, %s!" % name)

    if __name__ == '__main__':
        hello(_anyio_backend="trio")  # or asyncio, or curio

.. note::
    AsyncClick automagically starts an anyio event loop and runs your
    code asynchronously.

And what it looks like when run:

.. code-block:: text

    $ python hello.py --count=3
    Your name: Click
    Hello, Click!
    Hello, Click!
    Hello, Click!


Donate
------

The Pallets organization develops and supports Click and other popular
packages. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, `please
donate today`_.

.. _please donate today: https://palletsprojects.com/donate

The AsyncClick fork is maintained by Matthias Urlichs <matthias@urlichs.de>.
It's not a lot of work, so if you'd like to motivate me, donate to the
charity of your choice and tell me that you've done so. ;-)

Links
-----

These links point to the original, non-async-enabled, version of ``Click``.

*   Website: https://palletsprojects.com/p/click/
*   Documentation: https://click.palletsprojects.com/
*   License: `BSD <https://github.com/pallets/click/blob/master/LICENSE.rst>`_
*   Releases: https://pypi.org/project/click/
*   Code: https://github.com/pallets/click
*   Issue tracker: https://github.com/pallets/click/issues
*   Test status: https://dev.azure.com/pallets/click/_build
*   Official chat: https://discord.gg/t6rrQZH
