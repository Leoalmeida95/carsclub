# -*- coding: utf-8 -*-
# content of test_sample.py
import pytest 
import sys

def func(x):
    return x + 1

def test_answer1():
    assert func(3) == 4

@pytest.mark.skip(reason="don't work now")
def test_answer2():
    assert func(3) == 5

@pytest.mark.skipif(sys.version_info > (3,0), reason='Version Py')
def test_answer3():
    assert func(3) == 5

