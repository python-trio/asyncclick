# $ asyncclick_

Asyncclick is a fork of Click (described below) that works with trio or asyncio.

AsyncClick allows you to seamlessly use async command and subcommand handlers.


<div align="center"><img src="https://raw.githubusercontent.com/pallets/click/refs/heads/stable/docs/_static/click-name.svg" alt="" height="150"></div>

# Click

Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary. It's the "Command
Line Interface Creation Kit". It's highly configurable but comes with
sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun
while also preventing any frustration caused by the inability to
implement an intended CLI API.

Click in three points:

-   Arbitrary nesting of commands
-   Automatic help page generation
-   Supports lazy loading of subcommands at runtime


## A Simple Example

```python
import asyncclick as click
import anyio

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
async def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")
        await anyio.sleep(0.2)

if __name__ == '__main__':
    hello()
    # alternately: anyio.run(hello.main)
```

```
$ python hello.py --count=3
Your name: Click
Hello, Click!
Hello, Click!
Hello, Click!
```

## Differences to Click

This async-ized version of Click is mostly backwards compatible for "normal" use:
you can freely mix sync and async versions of your command handlers and callbacks.

Several advanced methods, most notably :meth:`BaseCommand.main`, and
:meth:`Context.invoke`, are now asynchronous.

The :meth:`BaseCommand.__call__` alias now invokes the main entry point via
`anyio.run`. If you already have an async main program, simply use
``await cmd.main()`` instead of ``cmd()``.

:func:`asyncclick.prompt` is asyncronous and accepts a ``blocking`` parameter
that switches between "doesn't affect your event loop but has unwanted effects when
interrupted" (bugfix pending) and "pauses your event loop but is safe to interrupt"
with Control-C". The latter is the default until we fix that bug.

You cannot use Click and AsyncClick in the same program. This is not a problem
in practice, as replacing ``import click`` with ``import asyncclick as click``, and
``from click import ...`` with ``from asyncclick import ...``, should be all that's
required.


## Donate

The Pallets organization develops and supports Click and other popular
packages. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, [please
donate today][].

[please donate today]: https://palletsprojects.com/donate

The AsyncClick fork is maintained by Matthias Urlichs <matthias@urlichs.de>.

## Contributing

### Click

See our [detailed contributing documentation][contrib] for many ways to
contribute, including reporting issues, requesting features, asking or answering
questions, and making PRs.

[contrib]: https://palletsprojects.com/contributing/

### AsyncClick

You can file async-specific issues, ideally including a corresponding fix,
to the [MoaT/asyncclick][moat] repository on github.

[moat]: https://github.com/M-o-a-T/asyncclick

#### Testing

If you find a bug, please add a testcase to prevent it from recurring.

In tests, you might wonder why `runner.invoke` is not called asynchronously.
The reason is that there are far too many of these calls to modify them all.
Thus ``tests/conftest.py``  contains a monkeypatch that turns this call
into a thread that runs this call using `anyio.run`.
