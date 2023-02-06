from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    #combines a persons given name and family name into one string with family name first
    assert make_full_name("Ava", "Taylor") == "Taylor; Ava"
    assert make_full_name("James", "Madison") == "Madison; James"
    assert make_full_name("Jonathon", "Taylor") == "Taylor; Jonathon"
    assert make_full_name("Jeffrey", "Chandler") == "Chandler; Jeffrey"

def test_extract_family_name():
    #extracts a persons family name from the full name
    assert extract_family_name("Taylor; Ava") == "Taylor"
    assert extract_family_name("Madison; James") == "Madison"
    assert extract_family_name("Taylor; Jonathon") == "Taylor"
    assert extract_family_name("Chandler; Jeffrey") == "Chandler"

def test_extract_given_name():
    #extracts a persons given name from the full name
    assert extract_given_name("Taylor; Ava") == "Ava"
    assert extract_given_name("Madison; James") == "James"
    assert extract_given_name("Taylor; Jonathon") == "Jonathon"
    assert extract_given_name("Chandler; Jeffrey") == "Jeffrey"


#Call the main function that is part of pytest so that the computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
