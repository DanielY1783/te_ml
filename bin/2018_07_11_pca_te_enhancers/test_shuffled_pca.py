
# coding: utf-8

# File to run tests on functions within shuffled_pca.py that are easy to test

# In[ ]:


# Tests for shuffled_pca.py
import shuffled_pca as sp

def test_generate_permutations_1():
    assert sp.generate_components([]) = []

def test_generate_permutations_2():
    assert sp.generate_components([1, 2, 3]) = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2,], [2, 3],
                                               [3, 1], [3, 2], [3, 3]]
def test_generate_permutations_3():
    assert sp.generate_components("ab", n = 3) = ["aaa", "aab", "aba", "abb", "baa", "bab",
                                                 "bba", "bbb"]

