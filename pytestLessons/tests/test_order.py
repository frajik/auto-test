import pytest


@pytest.mark.run(order=2)
def test_method_mail_1():
    print("Метод_1")

@pytest.mark.run(order=1)
def test_method_mail_2():
    print("Метод_2")

@pytest.mark.run(order=4)
def test_method_mail_3():
    print("Метод_3")

@pytest.mark.run(order=3)
def test_method_mail_4():
    print("Метод_4")

@pytest.mark.run(order=5)
def test_method_mail_5():
    print("Метод_5")

@pytest.mark.run(order=6)
def test_method_mail_6():
    print("Метод_6")
