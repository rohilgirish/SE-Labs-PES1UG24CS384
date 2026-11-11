import math
from hypothesis import given, strategies as st
from food_delivery import parse_order, delivery_eta, coupon_discount


@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    try:
        result = parse_order(s)
    except Exception as e:
        assert False, f"parse_order crashed with: {e}"
    assert isinstance(result, dict)
    for k, v in result.items():
        assert isinstance(k, str) and len(k) > 0
        assert isinstance(v, int) and v > 0


@given(st.text() | st.none())
def test_delivery_eta_no_crash(s):
    try:
        result = delivery_eta(s)
    except Exception as e:
        assert False, f"delivery_eta crashed with: {e}"
    assert result is None or (isinstance(result, int) and not isinstance(result, bool) and result >= 15)


@given(st.text() | st.none())
def test_coupon_discount_no_crash(s):
    try:
        result = coupon_discount(s)
    except Exception as e:
        assert False, f"coupon_discount crashed with: {e}"
    assert isinstance(result, int) and not isinstance(result, bool) and result >= 0


@given(st.integers() | st.floats() | st.booleans() | st.lists(st.text()))
def test_non_string_inputs_no_crash(val):
    try:
        assert isinstance(parse_order(val), dict)
        eta = delivery_eta(val)
        assert eta is None or (isinstance(eta, int) and eta >= 15)
        discount = coupon_discount(val)
        assert isinstance(discount, int) and discount >= 0
    except Exception as e:
        assert False, f"crashed on non-string input {val!r}: {e}"


@given(st.floats(min_value=0, max_value=1000, allow_nan=False, allow_infinity=False))
def test_delivery_eta_valid_distance(d):
    result = delivery_eta(str(d))
    assert result == int(15 + d * 4)


@given(st.integers(min_value=0, max_value=10000))
def test_coupon_discount_valid_code(amount):
    assert coupon_discount(f"save{amount}") == amount
    assert coupon_discount(f"  SAVE{amount}  ") == amount


def test_parse_order_valid_csv():
    assert parse_order("pizza:2,burger:1") == {"pizza": 2, "burger": 1}
    assert parse_order(" pizza : 2 , pizza : 1 ") == {"pizza": 3}
