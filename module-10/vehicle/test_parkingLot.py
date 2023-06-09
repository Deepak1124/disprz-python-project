import pytest
from ParkingLot import ParkingLot
from Vehicle import Car

@pytest.fixture
def parking_lot():
    return ParkingLot()

def test_create_parking_lot(parking_lot):
    assert parking_lot.create_parking_lot(5) == 5

def test_park(parking_lot):
    parking_lot.create_parking_lot(5)
    assert parking_lot.park("ABC123", "Red") == 1
    assert parking_lot.park("XYZ456", "Blue") == 2

def test_leave_slot(parking_lot):
    parking_lot.create_parking_lot(5)
    parking_lot.park("ABC123", "Red")
    assert parking_lot.leave_slot(1) == True

def test_check_status(parking_lot, capsys):
    parking_lot.create_parking_lot(3)
    parking_lot.park("ABC123", "Red")
    parking_lot.park("XYZ789", "Blue")
    parking_lot.check_status()
    captured = capsys.readouterr()
    assert "1\tABC123\tRed" in captured.out
    assert "2\tXYZ789\tBlue" in captured.out

def test_get_regno_from_color(parking_lot):
    parking_lot.create_parking_lot(5)
    parking_lot.park("ABC123", "Red")
    parking_lot.park("XYZ456", "Blue")
