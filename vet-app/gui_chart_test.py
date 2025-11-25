import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QToolTip
from PyQt6.QtCharts import QChartView, QChart, QSplineSeries, QValueAxis, QLineSeries
from PyQt6.QtCore import QPointF, Qt, QDateTime, QDate, QTime
from PyQt6.QtGui import QCursor
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from example import AnimalWeight, Base
from datetime import datetime, timedelta

class ChartTest(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chart Test - Rex Weights")
        self.setGeometry(100, 100, 800, 600)

        engine = create_engine('sqlite:///test.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

        # Load Rex weights (assume animal_id=1)
        weights = self.session.query(AnimalWeight).filter(AnimalWeight.animal_id == 1).order_by(AnimalWeight.date).all()

        layout = QVBoxLayout()

        title = QLabel("Rex Weight Line Chart")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        series = QLineSeries()  # Using line series for cleaner look with sparse data
        series.setName("Rex Weights")

        print(f"Loading {len(weights)} weight records...")

        # Collect data points with index and dates
        data_points = []
        dates = []
        weights_list = []

        for i, w in enumerate(weights, start=1):
            dates.append(w.date.date())
            weights_list.append(w.weight)
            data_points.append((i, w.weight))
            series.append(i, w.weight)
            print(f"Added point: {i} - {w.date.date()} -> {w.weight} kg")

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.setTitle("Rex Weight Line Chart")

        # Create and configure value axis for X-axis (index)
        axis_x = QValueAxis()
        axis_x.setLabelFormat("%d")
        axis_x.setTitleText("Measurement Number")
        axis_x.setRange(0, len(weights))
        axis_x.setTickCount(len(weights) + 1)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        # Create and configure value axis for Y-axis
        axis_y = QValueAxis()
        axis_y.setLabelFormat("%.1f")
        axis_y.setTitleText("Weight (kg)")
        if weights_list:
            min_w = min(weights_list)
            max_w = max(weights_list)
            axis_y.setRange(min_w - 0.5, max_w + 0.5)
        else:
            axis_y.setRange(0, 20)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        chart_view = QChartView(chart)
        # Connect tooltip
        series.hovered.connect(lambda point, state: QToolTip.showText(QCursor.pos(), f"Date: {dates[int(point.x()) - 1]}, Weight: {point.y()} kg") if state and 1 <= int(point.x()) <= len(dates) else QToolTip.hideText())
        layout.addWidget(chart_view)

        self.setLayout(layout)
        self.session.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChartTest()
    window.show()
    sys.exit(app.exec())
