from programm import *

def test_plusmal():
    assert plusmal(2,3) == 10

def test_unterschreiben():
    assert unterschreiben("Test") == "Test_unterschrieben"

def test_kubieren():
    assert kubieren(3) == 27
