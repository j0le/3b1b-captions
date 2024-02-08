import json

with open("data.json", "w") as f:
    data = {
        "contributors": [["name", "some data", "1234", "56789"], ["name with \" and \"\"", "and less columns"]],
        "percentages": [["another name", "some project idk", "58%"], ["max mustermann", "the same project", "a percentage that does not add up to a 100"]]
    }
    f.write(json.dumps(data))
