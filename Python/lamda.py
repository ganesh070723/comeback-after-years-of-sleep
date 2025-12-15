people = [
    {
        "name": "Harry", 
        "house": "Gryff"
    },
    {
        "name":"Ganesh",
        "house": "Redbull"
    },
    {
        "name":"Max",
        "house":"Redbull"
    }
]
# def f(person):
#     return person["name"]
people.sort(key= lambda person: person["name"])

print(people)