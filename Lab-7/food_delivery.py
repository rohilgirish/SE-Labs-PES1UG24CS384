import math
import re


def parse_order(items_csv):
    """Parse a 'name:qty,...' CSV string into a dict of positive item quantities."""
    if not isinstance(items_csv, str) or not items_csv.strip():
        return {}

    order = {}
    for raw_item in items_csv.split(','):
        item = raw_item.strip()
        if not item:
            continue
        parts = item.split(':')
        if len(parts) != 2:
            continue
        name = parts[0].strip()
        qty_str = parts[1].strip()
        if not name or not qty_str.isascii() or not qty_str.isdigit() or len(qty_str) > 9:
            continue
        qty = int(qty_str)
        if qty <= 0:
            continue
        order[name] = order.get(name, 0) + qty
    return order


def delivery_eta(distance_km):
    """Calculate delivery ETA in minutes from a non-negative finite distance in km."""
    if isinstance(distance_km, bool) or not isinstance(distance_km, (int, float, str)):
        return None
    if isinstance(distance_km, str):
        distance_km = distance_km.strip()
        if not distance_km:
            return None
    try:
        dist = float(distance_km)
    except (ValueError, TypeError, OverflowError):
        return None
    if not math.isfinite(dist) or dist < 0 or dist > 10000:
        return None
    eta = 15 + dist * 4
    if not math.isfinite(eta):
        return None
    return int(eta)


def coupon_discount(code):
    """Extract a non-negative integer discount from a SAVE<amount> coupon code."""
    if not isinstance(code, str):
        return 0
    cleaned = code.strip().upper()
    match = re.fullmatch(r"SAVE([0-9]+)", cleaned)
    if not match:
        return 0
    digits = match.group(1)
    if len(digits) > 6:
        return 0
    return int(digits)


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    result = parse_order(user_input)
    print("Order:", result)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result)

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result)


if __name__ == "__main__":
    main()
