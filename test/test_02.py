import pytest

def test_02():
  assert True


@pytest.mark.xfail(strict=True)
def test_03():
  assert True
