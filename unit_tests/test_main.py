import pytest
from main import greet

def test_greet_regular_name():
    assert greet("Alice") == "Hello, Alice!"

def test_greet_empty_string():
    assert greet("") == "Hello, !"

def test_greet_special_characters():
    assert greet("@user123")

def test_hello_world():
    assert 1 + 1 == 2