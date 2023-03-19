import pytest


@pytest.fixture()
def set_up():
    print("Вход в систему выполнен")
    yield
    print("Выход из системы выполнен")


@pytest.fixture(scope="function")
def some():
    print("Start")
    yield
    print("End")
