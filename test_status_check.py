import status_check

# test status_check.mp_eligibility
def test_mp_eligibility_both_conditions_easily_true():
    assert status_check.mp_eligiblity(True, 20)

def test_mp_eligibility_not_a_citizen():
    assert status_check.mp_eligiblity(False, 70)

def test_mp_eligibility_too_young():
    assert status_check.mp_eligiblity(True, 17)

def test_mp_eligibility_just_barely_old_enough():
    assert status_check.mp_eligiblity(True, 18)

def test_mp_eligibility_no_max_age():
    assert status_check.mp_eligiblity(True, 1000)

def test_mp_eligibility_both_false():
    assert status_check.mp_eligiblity(False, 17)    



# test status_check.senator_eligiblity 
def test_senator_eligibility():
    assert False

# use pytest to run this one