import pytest
import anyio
from functools import partial

from asyncclick.testing import CliRunner

class SyncCliRunner(CliRunner):
    def invoke(self,*a,_sync=False,**k):
        fn = super().invoke
        if _sync:
            return fn(*a,**k)
        if k:
            fn = partial(fn, **k)
        return anyio.run(fn, *a, backend="trio")

@pytest.fixture(scope="function")
def runner(request):
    return SyncCliRunner()
