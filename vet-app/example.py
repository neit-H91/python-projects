from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, PrimaryKeyConstraint, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload
from datetime import datetime

Base = declarative_base()

class Specie(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Medicine(Base):
    __tablename__ = 'medicines'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Animal(Base):
    __tablename__ = 'animals'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    specie_id = Column(Integer, ForeignKey('species.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
    specie = relationship('Specie', backref='animals')
    owner = relationship('Owner', backref='animals')

class Appointment(Base):
    __tablename__ = 'appointments'
    animal_id = Column(Integer, ForeignKey('animals.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    animal = relationship('Animal')
    owner = relationship('Owner')
    __table_args__ = (PrimaryKeyConstraint('animal_id', 'owner_id', 'date'),)

class History(Base):
    __tablename__ = 'histories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    animal_id = Column(Integer, ForeignKey('animals.id'), nullable=False)
    medicine_id = Column(Integer, ForeignKey('medicines.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    animal = relationship('Animal', backref='histories')
    medicine = relationship('Medicine', backref='histories')

class AnimalWeight(Base):
    __tablename__ = 'animal_weights'
    id = Column(Integer, primary_key=True, autoincrement=True)
    animal_id = Column(Integer, ForeignKey('animals.id'), nullable=False)
    weight = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    animal = relationship('Animal', backref='weights')

engine = create_engine('sqlite:///test.db')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example usage
# Create some data
if not session.query(Specie).first():
    specie1 = Specie(name='Dog')
    owner1 = Owner(name='John Doe')
    medicine1 = Medicine(name='Aspirin')
    session.add_all([specie1, owner1, medicine1])
    session.commit()
    animal1 = Animal(name='Rex', specie_id=specie1.id, owner_id=owner1.id)
    session.add(animal1)
    session.commit()
    history1 = History(animal_id=animal1.id, medicine_id=medicine1.id, date=datetime(2023, 10, 1, 10, 0))
    session.add(history1)
    session.commit()
    weight1 = AnimalWeight(animal_id=animal1.id, weight=15.5, date=datetime(2023, 10, 1))
    weight2 = AnimalWeight(animal_id=animal1.id, weight=16.0, date=datetime(2023, 10, 15))
    weight3 = AnimalWeight(animal_id=animal1.id, weight=16.5, date=datetime(2023, 11, 1))
    session.add_all([weight1, weight2, weight3])
    session.commit()

# Query history with animal and medicine names
history_entry = session.query(History).options(joinedload(History.animal), joinedload(History.medicine)).first()
if history_entry:
    print(f"History: Medicine '{history_entry.medicine.name}' given to '{history_entry.animal.name}' id : {history_entry.animal.id} on {history_entry.date}")


session.close()
