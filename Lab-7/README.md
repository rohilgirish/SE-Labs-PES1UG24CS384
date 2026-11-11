# Lab 7: Fuzzing for Input Validation Bugs

- **Name:** Rohil Thimmanahalli Girish
- **SRN:** PES1UG24CS384
- **Section:** G
- **Application Module:** [`food_delivery.py`](food_delivery.py)
- **Fuzz Test Suite:** [`test_food_delivery.py`](test_food_delivery.py)
- **Consolidated Report:** [`PES1UG24CS384_LAB07.pdf`](PES1UG24CS384_LAB07.pdf)

---

## 1. Objective

Apply property-based fuzz testing using **Hypothesis** and **Pytest** to uncover crashes and input validation bugs in `food_delivery.py`, then harden all functions against unexpected or malformed inputs.

---

## 2. Bugs Discovered & Fixes Applied

| Function | Original Bugs Found via Fuzzing | Defensive Fix Implemented |
| :--- | :--- | :--- |
| `parse_order(items_csv)` | `AttributeError` on `None` or non-string; `ValueError` on empty string, missing/extra `:`, or non-integer quantity; overwrote duplicate items | Validate `isinstance(..., str)` and non-empty segments, require exactly two `:`-separated parts, verify non-empty item name and ASCII positive integer quantity (`len <= 9`), and accumulate duplicate items. |
| `delivery_eta(distance_km)` | `TypeError` on `None`; `ValueError` on empty/non-numeric strings or `NaN`; `OverflowError` on `inf`; allowed negative distances | Reject `bool` and unsupported types, safely parse `float`, check `math.isfinite` and `0 <= dist <= 10000` (and finite ETA), returning `None` for invalid inputs. |
| `coupon_discount(code)` | `AttributeError` on `None` or non-string; `IndexError` when `'SAVE'` is missing; `ValueError` on empty/non-numeric suffix; allowed negative discounts | Validate `isinstance(..., str)`, normalize whitespace/case, match `^SAVE([0-9]+)$` with bounded length (`<= 6` digits), returning `0` for invalid codes. |

---

## 3. Commands to Reproduce

```bash
# Install dependencies
pip install hypothesis pytest

# Run the application
python food_delivery.py

# Run Hypothesis fuzz tests
python -m pytest test_food_delivery.py -v
```

---

## 4. Verification Summary

- **Before Fix:** `5 failed, 2 passed in 5.53s` (crashes on `None`, `''`, `':'`, and `0`)
- **After Fix:** `7 passed in 1.58s` (`test_food_delivery.py` passes all 7 Hypothesis and unit tests)
