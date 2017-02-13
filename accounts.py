import constants

ACCT_VALUE_INDEX=1


def get_balance(person=constants.TEST_1, acct=constants.ALL):
    if acct == constants.ALL:
        value = 0
        for a_type in constants.ACCT_TYPES:
            value += get_indv_balance(person, a_type)
        return value
    else:
        return get_indv_balance(person, acct)


def get_indv_balance(person=constants.TEST_1, acct=constants.PI):
    value = 0
    for acct_tuple in person[acct]:
        value += acct_tuple[ACCT_VALUE_INDEX]
    return value

def get_balance_named(person,name):
    pass