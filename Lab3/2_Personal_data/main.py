import json


class Persona:
    def __init__(self, name, last_name, address, post_code, pesel):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.post_code = post_code
        self.pesel = pesel

class Persons:
    def __init__(self, persons: [Persona] = []):
        self.persons = persons

    def save(self, filename):
        list = []
        for p in self.persons:
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


person1 = Persona("Jack", "Kowalski", "Lipinki", "00-000","12354364607")
person2 = Persona("Molly", "Tomaszek", "Florianska", "11-345","09876543212")
person3 = Persona("Tom", "Tomaszek", "Florianska", "11-345","09876543212")

p = Persons([person1, person2,person3])

p.save("persons.json")

person_json = Persons.read("persons.json")

for p in person_json:
    print(p.persons)