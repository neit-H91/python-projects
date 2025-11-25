import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton
from PyQt6.QtCore import Qt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from example import Specie, Owner, Animal, Base  # Import from example.py

class AnimalForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Animal")
        self.setGeometry(100, 100, 300, 200)

        # Database session
        engine = create_engine('sqlite:///test.db')
        # Ensure tables exist
        from example import Base
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

        # Ensure some initial data
        self.add_initial_data()

        layout = QVBoxLayout()

        # Name input
        self.name_label = QLabel("Animal Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Specie combobox
        self.specie_label = QLabel("Specie:")
        self.specie_combo = QComboBox()
        self.load_species()
        layout.addWidget(self.specie_label)
        layout.addWidget(self.specie_combo)

        # Owner combobox
        self.owner_label = QLabel("Owner:")
        self.owner_combo = QComboBox()
        self.load_owners()
        layout.addWidget(self.owner_label)
        layout.addWidget(self.owner_combo)

        # Save button
        self.save_button = QPushButton("Save Animal")
        self.save_button.clicked.connect(self.save_animal)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def add_initial_data(self):
        if not self.session.query(Specie).first():
            dog = Specie(name='Dog')
            cat = Specie(name='Cat')
            self.session.add_all([dog, cat])
            self.session.commit()
        if not self.session.query(Owner).first():
            owner1 = Owner(name='John Doe')
            owner2 = Owner(name='Jane Smith')
            self.session.add_all([owner1, owner2])
            self.session.commit()

    def load_species(self):
        species = self.session.query(Specie).all()
        for specie in species:
            self.specie_combo.addItem(specie.name, specie.id)

    def load_owners(self):
        owners = self.session.query(Owner).all()
        for owner in owners:
            self.owner_combo.addItem(owner.name, owner.id)

    def save_animal(self):
        name = self.name_input.text().strip()
        specie_id = self.specie_combo.currentData()
        owner_id = self.owner_combo.currentData()
        if name and specie_id and owner_id:
            animal = Animal(name=name, specie_id=specie_id, owner_id=owner_id)
            self.session.add(animal)
            self.session.commit()
            print("Animal saved:", animal.name)
            self.name_input.clear()
        else:
            print("Please fill all fields.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = AnimalForm()
    form.show()
    sys.exit(app.exec())
