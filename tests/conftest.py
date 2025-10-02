from threading import Thread

import anyio
import pytest

from asyncclick.testing import CliRunner


class SyncCliRunner(CliRunner):
    def invoke(self, *a, _sync=False, **k):
        fn = super().invoke
        if _sync:
            return fn(*a, **k)

        # anyio now protects against nested calls, so we use a thread
        result = None

        def f():
            nonlocal result, fn

            async def r():
                return await fn(*a, **k)

            result = anyio.run(r)  ## , backend="trio")

        t = Thread(target=f, name="TEST")
        t.start()
        t.join()
        return result


@pytest.fixture(scope="function")
def runner(request):
    return SyncCliRunner()


@pytest.fixture(scope="function")
def arunner(request):
    return CliRunner()
