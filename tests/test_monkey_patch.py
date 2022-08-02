from pathlib import Path
from main import getssh, example_1_monkeypatch, example_2_monkeypatch
import os
import main2

def test_getssh(monkeypatch):
    # mocked return function to replace Path.home
    # always return '/abc'
    def mockreturn():
        return Path("/abc")

    # Application of the monkeypatch to replace Path.home
    # with the behavior of mockreturn defined above.
    monkeypatch.setattr(Path, "home", mockreturn)

    # Calling getssh() will use mockreturn in place of Path.home
    # for this test with the monkeypatch.
    x = getssh()
    assert x == Path("/abc/.ssh")

def test_getssh():
    # mocked return function to replace Path.home
    # always return '/abc'
    def mockreturn():
        return Path("/abc")

    # Application of the monkeypatch to replace Path.home
    # with the behavior of mockreturn defined above.
    #monkeypatch.setattr(Path, "home", mockreturn)

    # Calling getssh() will use mockreturn in place of Path.home
    # for this test with the monkeypatch.
    x = getssh()
    assert x == Path("/home/marcus/.ssh")

"""
def test_square(monkeypatch):
    def mock_square_return():
        return 0
    monkeypatch.setattr(, "denominator", mock_square_return())
    y = square_overall(3)
    assert y == 0

def test_square_overall(monkeypatch):
    def mock_square_return():
        return 1
    monkeypatch.setattr(MyClass, "square", mock_square_return())
    y = square_overall(3)
    assert y==1
"""

def test_example_1_monkeypatch(monkeypatch):
    def mock_return():
        return "mockreturn"
    monkeypatch.setattr(os, "getcwd", mock_return)
    assert example_1_monkeypatch() == "mockreturn"

def test_example_2_monkeypatch(monkeypatch):
    def mock_return(str1,str2):
        return "mockreturn"
    monkeypatch.setattr(main2, "addStrings", mock_return)
    assert example_2_monkeypatch("hej", "på") == "mockreturn"

def test_example_2_without_monkeypatch():
    #def mock_return(str1,str2):
    #    return "mockreturn"
    #monkeypatch.setattr(main2, "addStrings", mock_return)
    assert example_2_monkeypatch("hej", "på") == "hejpå"

#def test_square_overall():
    #def mock_square_return():
    #    return 0
    #monkeypatch.setattr(MyClass, "square", mock_square_return())
#    y = square_overall(3)
#    assert y==0