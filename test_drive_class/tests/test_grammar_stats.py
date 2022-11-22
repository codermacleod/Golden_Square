from lib.grammar_stats import GrammarStats

'''
    Returns True when
    Starts with capital and
    End with valid punctuation:
'''

def test_returns_true_if_capital_and_punc():
    gs = GrammarStats()
    gs_good = gs.check("Hello!")
    gs_nocaps = gs.check("hello!")
    gs_nopunc = gs.check("Hello")
    gs_nothing = gs.check("hello")
    assert gs_good == True
    assert gs_nocaps == False
    assert gs_nopunc == False
    assert gs_nothing == False


'''
    Check number of tests
    which pass against number which fail
    and return percentage as an integer:
'''

def test_returns_percentage_of_valid_checks():
    gs = GrammarStats()
    gs.check("Hello!")
    gs.check("hello!")
    gs.check("Hello")
    gs.check("hello")
    assert gs.percentage_good() == '25%'
