import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time

# ==============================================================================
# CODE COVERAGE TEST SUITE
# Designed to achieve 100% Line (Statement) Coverage on food_delivery.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Tests for delivery_charge(distance_km, order_value, is_raining)
# ------------------------------------------------------------------------------

def test_delivery_charge_out_of_range():
    """Executes lines 5->6: raises ValueError when distance is invalid."""
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)

def test_delivery_charge_free_delivery_over_500():
    """Executes lines 7->8: charge = 0 when order_value >= 500."""
    assert delivery_charge(5, 500, False) == 0

def test_delivery_charge_distance_upto_3km():
    """Executes lines 9->10: charge = 20 for short distance (<= 3 km)."""
    assert delivery_charge(2, 200, False) == 20

def test_delivery_charge_distance_upto_8km():
    """Executes lines 11->12: charge = 40 for medium distance (<= 8 km)."""
    assert delivery_charge(6, 200, False) == 40

def test_delivery_charge_distance_above_8km():
    """Executes lines 13->14: charge = 60 for long distance (> 8 km)."""
    assert delivery_charge(10, 200, False) == 60

def test_delivery_charge_with_rain_surcharge():
    """Executes lines 15->16: adds 30 surcharge when is_raining is True."""
    assert delivery_charge(2, 200, True) == 50


# ------------------------------------------------------------------------------
# Tests for apply_coupon(order_value, code, is_first_order)
# ------------------------------------------------------------------------------

def test_apply_coupon_none():
    """Executes lines 21->22: returns unchanged order_value when code is None."""
    assert apply_coupon(300, None, False) == 300

def test_apply_coupon_invalid_code():
    """Executes lines 23->24: raises ValueError when coupon code is not recognized."""
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "DISCOUNT50", False)

def test_apply_coupon_welcome_not_first_order():
    """Executes lines 25->26: raises ValueError when WELCOME coupon used on non-first order."""
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)

def test_apply_coupon_order_below_minimum_value():
    """Executes lines 27->28: returns original order_value if under 200."""
    assert apply_coupon(150, "SAVE50", False) == 150

def test_apply_coupon_success():
    """Executes line 29: deducts coupon discount from eligible order."""
    assert apply_coupon(350, "SAVE50", False) == 300


# ------------------------------------------------------------------------------
# Tests for estimated_time(distance_km, is_peak_hour, restaurant_busy)
# ------------------------------------------------------------------------------

def test_estimated_time_peak_hour_and_busy():
    """Executes lines 33, 34->35, 36->37, 38->39, 40:
    All conditional branches evaluate to True, executing every line in function.
    Base (15 + 5*4 = 35) + peak (10) + busy (15) + peak-busy (5) = 65 mins.
    """
    assert estimated_time(5, True, True) == 65

