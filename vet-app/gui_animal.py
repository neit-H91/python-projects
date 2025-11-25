import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QComboBox, QPushButton
from PyQt6.QtCharts import QChartView, QChart, QSplineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import QDateTime, QDate, QTime, Qt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from example import Animal, History, AnimalWeight, Specie, Owner, Base

class AnimalPage(QWidget):
    def __init__(self, stack, animal_id=None):
        super().__init__()
        self.stack = stack
        self.animal = None
        self.animal_id = animal_id
        engine = create_engine('sqlite:///test.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.load_animal()

        layout = QVBoxLayout()

        # Title
        title = QLabel("View Animal Information")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        # Animal info
        info_layout = QVBoxLayout()
        self.name_label = QLabel("Name: ")
        self.specie_label = QLabel("Specie: ")
        self.owner_label = QLabel("Owner: ")
        info_layout.addWidget(self.name_label)
        info_layout.addWidget(self.specie_label)
        info_layout.addWidget(self.owner_label)
        layout.addLayout(info_layout)

        # History table
        history_label = QLabel("Medicine History:")
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(3)
        self.history_table.setHorizontalHeaderLabels(["Medicine", "Date", ""])
        self.history_table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(history_label)
        layout.addWidget(self.history_table)

        # Weight chart
        weight_label = QLabel("Weight Chart:")
        self.chart_view = QChartView()
        layout.addWidget(weight_label)
        layout.addWidget(self.chart_view)

        # Back button
        back_button = QPushButton("Back")
        back_button.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        layout.addWidget(back_button)

        self.setLayout(layout)

        self.update_display()

    def load_animal(self):
        if self.animal_id:
            self.animal = self.session.query(Animal).options(joinedload(Animal.specie), joinedload(Animal.owner)).filter(Animal.id == self.animal_id).first()
        else:
            self.animal = None

    def update_display(self):
        if self.animal:
            self.name_label.setText(f"Name: {self.animal.name}")
            self.specie_label.setText(f"Specie: {self.animal.specie.name}")
            self.owner_label.setText(f"Owner: {self.animal.owner.name}")
            # Load history
            histories = self.session.query(History).options(joinedload(History.medicine)).filter(History.animal_id == self.animal.id).all()
            self.history_table.setRowCount(len(histories))
            for i, h in enumerate(histories):
                medicine_name = h.medicine.name if h.medicine else "Unknown"
                date_str = h.date.strftime("%Y-%m-%d %H:%M") if h.date else ""
                self.history_table.setItem(i, 0, QTableWidgetItem(medicine_name))
                self.history_table.setItem(i, 1, QTableWidgetItem(date_str))
                self.history_table.setItem(i, 2, QTableWidgetItem(""))  # Placeholder for actions if needed
            # Load weights and create chart
            weights = sorted(self.session.query(AnimalWeight).filter(AnimalWeight.animal_id == self.animal.id).all(), key=lambda w: w.date)
            series = QSplineSeries()
            for w in weights:
                dt = QDateTime(QDate(w.date.year, w.date.month, w.date.day), QTime(w.date.hour, w.date.minute))
                msecs = dt.toMSecsSinceEpoch()
                series.append(msecs, w.weight)
            chart = QChart()
            chart.setTitle("Weight Timeline")
            chart.addSeries(series)
            axis_x = QDateTimeAxis()
            axis_x.setFormat("MMM yyyy")
            axis_x.setTickCount(4)
            chart.addAxis(axis_x, 1)  # Horizontal
            series.attachAxis(axis_x)
            axis_y = QValueAxis()
            axis_y.setTitleText("Weight (kg)"
                                )
            chart.addAxis(axis_y, 2)  # Vertical
            series.attachAxis(axis_y)
            self.chart_view.setChart(chart)
        else:
            self.name_label.setText("Name: No animal selected")
            self.specie_label.setText("Specie: -")
            self.owner_label.setText("Owner: -")
            self.history_table.setRowCount(0)
            # Clear chart
            self.chart_view.setChart(QChart())

if __name__ == "__main__":
    # For testing standalone
    from PyQt6.QtWidgets import QStackedWidget
    app = QApplication(sys.argv)
    stack = QStackedWidget()
    page = AnimalPage(stack,1)
    window = QWidget()
    window.setLayout(QVBoxLayout())
    window.layout().addWidget(page)
    window.setWindowTitle("Animal Page")
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())
