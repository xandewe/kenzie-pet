data = {
    "name": "Diana",
    "age": 1,
    "weight": 30,
    # "sex": "Femea",
    "group": {
        "name": "cão",
        "scientific_name": "canis familiaris"
    },
    # "traits": [
    #     {
    #         "name": "peludo"
    #     },
    #     {
    #         "name": "médio porte"
    #     }
    # ]
}

INVALID_UPDATE = {"traits", "group", "sex"}

print(INVALID_UPDATE.intersection(set(data)))