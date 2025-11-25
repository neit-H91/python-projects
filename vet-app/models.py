class Specie:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"Specie(id={self._id}, name={self._name})"

class Owner:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"Owner(id={self._id}, name={self._name})"

class Medicine:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"Medicine(id={self._id}, name={self._name})"

class Animal:
    def __init__(self, id, name, specie_id, owner_id):
        self._id = id
        self._name = name
        self._specie_id = specie_id
        self._owner_id = owner_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def specie_id(self):
        return self._specie_id

    @specie_id.setter
    def specie_id(self, value):
        self._specie_id = value

    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value

    def __str__(self):
        return f"Animal(id={self._id}, name={self._name}, specie_id={self._specie_id}, owner_id={self._owner_id})"

class Appointment:
    def __init__(self, animal_id, owner_id, date):
        self._animal_id = animal_id
        self._owner_id = owner_id
        self._date = date

    @property
    def animal_id(self):
        return self._animal_id

    @animal_id.setter
    def animal_id(self, value):
        self._animal_id = value

    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def __str__(self):
        return f"Appointment(animal_id={self._animal_id}, owner_id={self._owner_id}, date={self._date})"

    def __repr__(self):
        return f'Appointment(animal_id={self.animal_id}, owner_id={self.owner_id}, date={self.date})'

class History:
    def __init__(self, id, animal_id, medicine_id, date):
        self._id = id
        self._animal_id = animal_id
        self._medicine_id = medicine_id
        self._date = date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def animal_id(self):
        return self._animal_id

    @animal_id.setter
    def animal_id(self, value):
        self._animal_id = value

    @property
    def medicine_id(self):
        return self._medicine_id

    @medicine_id.setter
    def medicine_id(self, value):
        self._medicine_id = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def __str__(self):
        return f"History(id={self._id}, animal_id={self._animal_id}, medicine_id={self._medicine_id}, date={self._date})"
