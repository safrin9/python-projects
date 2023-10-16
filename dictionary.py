capital={
    "France":"Paris",
    "Germeny":"Berlin"
}

travel={
    "France":{"cities_visited":["Paris","Lille"],"total":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","gwl"],"total":13}
}
travel_log=[
    {"country":"France",
     "cities_visited":["Paris","Lille"],
     "total":12
    },

    {"country":"Germany",
     "cities_visited":["Berlin","Hamburg","gwl"],
     "total":13
    }
]
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in dict:
    dict[key]+=1
print(dict)
dict[1]=4
print(dict[1])
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])