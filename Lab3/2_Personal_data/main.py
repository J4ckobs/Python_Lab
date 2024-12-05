import json
from dataclasses import dataclass, asdict


@dataclass
class Persona:
        name: str
        last_name: str
        address: str
        post_code: str
        pesel: str

class People:
    def __init__(self, people: [Persona] = []):
        self.people = people

    def save(self, filename):
        list = []
        for p in self.people:
            list.append({
                    'name': p.name,
                    'last_name': p.last_name,
                    'address': p.address,
                    'post_code': p.post_code,
                    'pesel': p.pesel
                 })

        with open(filename, 'w') as file:
            json.dump(list, file)

    @classmethod
    def read(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)

            matrix = []

            for p in data:
                matrix.append(cls({p['name'], p['last_name'], p['address'], p['post_code'], p['pesel']}))
            return matrix


person1 = Persona("Jack", "Kowalski", "Lipinki", "00-000", "12354364607")
person2 = Persona("Molly", "Tomaszek", "Florianska", "11-345", "09876543212")
person3 = Persona("Tom", "Tomaszek", "Florianska", "11-345", "09876543212")

p = People([person1, person2, person3])

p.save("people.json")

people_json = People.read("people.json")

for p in people_json:
    print(p.people)