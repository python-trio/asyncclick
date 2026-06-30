from typing import assert_type

import asyncclick as click


@click.group(context_settings={})
def hello() -> None:
    pass


assert_type(hello, click.Group)
