from trio_click.testing import CliRunner

import pytest
import trio
from functools import partial

class SyncCliRunner(CliRunner):
    def invoke(self,*a,_sync=False,**k):
        fn = super().invoke
        if _sync:
            return fn(*a,**k)
        if k:
            fn = partial(fn, **k)
        return trio.run(fn, *a)

@pytest.fixture(scope='function')
def runner(request):
    return SyncCliRunner()
