ALL = "all"
CP529 = "529"
PI = "PI"
WI = "WI"

ACCT_TYPES = ["529", "PI", "WI"]


def ERR_DICT(speech="something wrong"): return {
        "speech": speech,
        "displayText": "something very wrong",
        #"data": {},
        # "contextOut": [],
        "source": "home"
    }


TEST_1 = {
    "529": [("Martha", 5), ("Bobby", 10), ("Daniel", 35)],
    "WI": [("Bob's Heating Service", 100)],
    "PI": [("Traditional", 20)]
}

TEST_2 = {
    "529": [],
    "WI": [],
    "PI": [("Roth", 200)]
}

TEST_3 = {
    "529": [],
    "WI": [("Bob's Heating Service", 100)],
    "PI": []
}