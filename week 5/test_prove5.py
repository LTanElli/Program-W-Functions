from prove5 import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import pytest



def main():
    test_get_determiner()
    test_get_noun()
    test_get_verb()
    test_get_preposition()
    test_get_prepositional_phrase()
    test_get_adjective()

def test_get_adjective():
    adjectives = ["fat", "skinny", "tall", "tiny", "quick", "slow"]

    for _ in range(12):
        adjective = get_adjective()
        assert adjective in adjectives
    

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners



def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(10):
        word = get_noun(1)
        assert word in single_nouns
    
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(10):
        word = get_noun(2)
        assert word in plural_nouns



def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(10):
        word = get_verb(1, 'past')
        assert word in past_verbs

    singular_presents = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(10):
        word = get_verb(1, "present")
        assert word in singular_presents

    plural_presents = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(10):
        word = get_verb(2, "present")
        assert word in plural_presents

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
        
    for _ in range(10):
        word = get_verb(1, "future")
        assert word in future_verbs

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(12):
        preposition = get_preposition()
    assert preposition in prepositions

def test_get_prepositional_phrase():
    #singular
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    single_determiners = ["a", "one", "the"]

    for _ in range(80):
        prepositional_phrase = get_prepositional_phrase(1)
        preposition, single_determiner, single_noun = prepositional_phrase
        assert preposition in prepositions
        assert single_determiner in single_determiners
        assert single_noun in single_nouns

    #plural
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    plural_determiners = ["some", "many", "the"]
    for _ in range(30):
        prepositional_phrase = get_prepositional_phrase(2)
        preposition, plural_determiner, plural_noun = prepositional_phrase
        assert preposition in prepositions
        assert plural_determiner in plural_determiners
        assert plural_noun in plural_nouns


pytest.main(["-v", "--tb=line", "-rN", __file__])