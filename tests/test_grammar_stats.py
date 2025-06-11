from lib.GrammarStats import *

def test_initialises():
    gs = GrammarStats()
    assert isinstance(gs, GrammarStats)

def test_check():
    gs = GrammarStats()
    assert gs.check('Hello.')
    assert gs.check('Hello!')
    assert gs.check('Hello?')
    assert not gs.check('Hello')
    assert not gs.check('hello')
    assert not gs.check('hello.')

def test_percentage_good():
    pass