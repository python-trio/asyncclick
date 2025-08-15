import pytest

from asyncclick.testing import CliRunner


@pytest.fixture(scope="function")
def runner(request):
    return CliRunner()
