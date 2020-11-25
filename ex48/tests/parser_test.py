from nose.tools import *
from ex48.parser import *

def test_nosubject():
    sentence = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'run')
    assert_equal(sentence.obj, 'north')

def test_stop():
    sentence = parse_sentence([('noun', 'bear'), ('verb', 'eat'),('stop', 'the'), ('noun', 'honey')])
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.obj, 'honey')

def test_noverb():
    assert_raises(ParserError, parse_sentence, [('direction', 'north')])
