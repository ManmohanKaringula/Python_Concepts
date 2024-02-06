import json

data="""{
    "name":"manmohan",
    "roll_no":"12",
    "emails":["manmohanreddyk.999@gmail.com", "manmohanreddy.karingula@gmail.com"]
}"""

data1=json.loads(data)
print(data1)
