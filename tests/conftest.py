import os
import tempfile

import pytest
import anyio
from functools import partial
from threading import Thread

from asyncclick.testing import CliRunner

class SyncCliRunner(CliRunner):
    def invoke(self,*a,_sync=False,**k):
        fn = super().invoke
        if _sync:
            return fn(*a,**k)

        # anyio now protects against nested calls, so we use a thread
        result = None
        def f():
            nonlocal result,fn
            async def r():
                return await fn(*a,**k)
            result = anyio.run(r) ## , backend="trio")
        t=Thread(target=f, name="TEST")
        t.start()
        t.join()
        return result

@pytest.fixture(scope="function")
def runner(request):
    return SyncCliRunner()


def _check_symlinks_supported():
    with tempfile.TemporaryDirectory(prefix="click-pytest-") as tempdir:
        target = os.path.join(tempdir, "target")
        open(target, "w").close()
        link = os.path.join(tempdir, "link")

        try:
            os.symlink(target, link)
            return True
        except OSError:
            return False


symlinks_supported = _check_symlinks_supported()
