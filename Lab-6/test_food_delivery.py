import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time

# ==============================================================================
# BRANCH COVERAGE TEST SUITE
# Designed to achieve 100% Branch Coverage on food_delivery.py
# Tests every decision branch (True and False), boundary conditions, and edge cases.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Tests for delivery_charge(distance_km, order_value, is_raining)
# ------------------------------------------------------------------------------

def test_delivery_charge_invalid_distance_lower_bound():
    """Branch: distance_km <= 0 (True via distance == 0)."""
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)

def test_delivery_charge_invalid_distance_negative():
    """Branch: distance_km <= 0 (True via negative distance)."""
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(-2, 200, False)

def test_delivery_charge_invalid_distance_upper_bound():
    """Branch: distance_km > 15 (True via distance > 15)."""
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(15.1, 200, False)

def test_delivery_charge_free_delivery_no_rain():
    """Branch: order_value >= 500 (True) with is_raining (False)."""
    assert delivery_charge(5, 500, False) == 0

def test_delivery_charge_free_delivery_with_rain():
    """Branch: order_value >= 500 (True) with is_raining (True surcharge)."""
    assert delivery_charge(5, 600, True) == 30

def test_delivery_charge_tier1_boundary_no_rain():
    """Branch: distance_km <= 3 (True boundary 3km), is_raining (False)."""
    assert delivery_charge(3, 499, False) == 20

def test_delivery_charge_tier1_with_rain():
    """Branch: distance_km <= 3 (True), is_raining (True)."""
    assert delivery_charge(1, 200, True) == 50

def test_delivery_charge_tier2_boundary_no_rain():
    """Branch: distance_km <= 8 (True boundary 8km), is_raining (False)."""
    assert delivery_charge(8, 200, False) == 40

def test_delivery_charge_tier2_with_rain():
    """Branch: distance_km <= 8 (True), is_raining (True)."""
    assert delivery_charge(5, 200, True) == 70

def test_delivery_charge_tier3_max_distance_no_rain():
    """Branch: distance_km <= 8 (False, boundary 15km), is_raining (False)."""
    assert delivery_charge(15, 200, False) == 60

def test_delivery_charge_tier3_with_rain():
    """Branch: distance_km > 8 (True), is_raining (True)."""
    assert delivery_charge(10, 200, True) == 90


# ------------------------------------------------------------------------------
# 2. Tests for apply_coupon(order_value, code, is_first_order)
# ------------------------------------------------------------------------------

def test_apply_coupon_none():
    """Branch: code is None (True)."""
    assert apply_coupon(300, None, False) == 300

def test_apply_coupon_not_in_coupons():
    """Branch: code not in COUPONS (True)."""
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "UNKNOWN_CODE", True)

def test_apply_coupon_welcome_not_first_order():
    """Branch: code == 'WELCOME' and not is_first_order (True)."""
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)

def test_apply_coupon_welcome_first_order_eligible():
    """Branch: code == 'WELCOME' and is_first_order is True, order >= 200."""
    assert apply_coupon(300, "WELCOME", True) == 200

def test_apply_coupon_welcome_first_order_ineligible():
    """Branch: code == 'WELCOME' and is_first_order is True, order < 200."""
    assert apply_coupon(150, "WELCOME", True) == 150

def test_apply_coupon_save50_order_below_200():
    """Branch: code == 'SAVE50', order_value < 200 (True)."""
    assert apply_coupon(199, "SAVE50", False) == 199

def test_apply_coupon_save50_boundary_200():
    """Branch: code == 'SAVE50', order_value >= 200 (boundary 200)."""
    assert apply_coupon(200, "SAVE50", False) == 150

def test_apply_coupon_save50_order_above_200():
    """Branch: code == 'SAVE50', order_value >= 200 (above minimum)."""
    assert apply_coupon(400, "SAVE50", True) == 350


# ------------------------------------------------------------------------------
# 3. Tests for estimated_time(distance_km, is_peak_hour, restaurant_busy)
# ------------------------------------------------------------------------------

def test_estimated_time_normal_conditions():
    """Branches: is_peak_hour (False), restaurant_busy (False).
    minutes = 15 + 5*4 = 35.
    """
    assert estimated_time(5, False, False) == 35

def test_estimated_time_peak_hour_only():
    """Branches: is_peak_hour (True), restaurant_busy (False).
    minutes = 15 + 5*4 + 10 = 45.
    """
    assert estimated_time(5, True, False) == 45

def test_estimated_time_restaurant_busy_only():
    """Branches: is_peak_hour (False), restaurant_busy (True), inner is_peak_hour (False).
    minutes = 15 + 5*4 + 15 = 50.
    """
    assert estimated_time(5, False, True) == 50

def test_estimated_time_peak_hour_and_restaurant_busy():
    """Branches: is_peak_hour (True), restaurant_busy (True), inner is_peak_hour (True).
    minutes = 15 + 5*4 + 10 + 15 + 5 = 65.
    """
    assert estimated_time(5, True, True) == 65
