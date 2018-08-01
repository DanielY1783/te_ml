# Name: Daniel Yan
# Date: 2018-07-13
# Email: daniel.yan@vanderbilt.edu

# Tests on functions within shuffled_pca.py
import shuffled_pca as sp

def test_generate_configurations_1():
    assert sp.generate_configurations([]) == []

def test_generate_configurations_2():
    assert sp.generate_configurations([1, 2, 3]) == [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2,), (2, 3),
                                               (3, 1), (3, 2), (3, 3)]
def test_generate_configurations_3():
    assert sp.generate_configurations("ab", n = 3) == [('a', 'a', 'a'), ('a', 'a', 'b'), 
                                                     ('a', 'b', 'a'), ('a', 'b', 'b'), 
                                                     ('b', 'a', 'a'), ('b', 'a', 'b'),
                                                     ('b', 'b', 'a'), ('b','b', 'b')]
def test_generate_combinations_1():
    assert sp.generate_combinations([]) == []

def test_generate_combinations_2():
    assert sp.generate_combinations([1, 2, 3]) == [(1, 2), (1, 3), (2, 3)]
    
def test_generate_combinations_3():
    assert sp.generate_combinations("ab", n = 3) == []

def test_generate_combinations_4():
    assert sp.generate_combinations("abcd", n = 3) == [('a', 'b', 'c'), ('a', 'b', 'd'),
                                                      ('a', 'c', 'd'), ('b', 'c', 'd')]

