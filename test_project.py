
from app import days_due_amount

def test_days_due_amount():
    assert days_due_amount(5) == 20
    assert days_due_amount(10) == 35
    assert days_due_amount(15) == 60
    assert days_due_amount(20) == 85
    assert days_due_amount(25) == 110
    assert days_due_amount(30) == 135
    assert days_due_amount(35) == 160
    assert days_due_amount(40) == 185
    assert days_due_amount(45) == 210
    assert days_due_amount(50) == 235
    assert days_due_amount(100) == 485
