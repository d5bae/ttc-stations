
# needs some fucntions to do work here
# needs something to determine MP eligibility 
# needs something to determine Senator 

def mp_eligiblity(is_citizen, age): 
    """to be an Mp need to be a citizen and 18 or older"""
    min_age = 18
    result = is_citizen and age >= min_age
    return result

def senator_eligibility(is_citizen, age, net_worth):
    """TODO: Write doc string"""
    return None


def main(): 
    is_citizen = True # True is a Canadian Citizen, o.w. False
    age = 55          # age in years
    net_worth = 5000  # networth in dollars 

    can_be_mp = None
    can_be_senator = None
    print("Eligible to be an MP?", can_be_mp)
    print("Eligible to be a Senator", can_be_senator)

if __name__ == "__main__":
    main()