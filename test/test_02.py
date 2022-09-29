import pytest

def test_02():
  assert True


@pytest.mark.xfail()
def test_03():
  assert False
