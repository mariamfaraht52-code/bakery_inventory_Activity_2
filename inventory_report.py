import csv

def load_inventory(filename):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

def main():
    items = load_inventory('inventory.csv')

    print(f"Total items tracked: {len(items)}")

    low_stock = [row for row in items if int(row['quantity']) < 10]
    print(f"\nLow stock items (fewer than 10 units): {len(low_stock)}")
    for row in low_stock:
        print(f"  - {row['item_name']}: {row['quantity']} left")

    most_valuable = max(items, key=lambda row: float(row['unit_price']))
    print(f"\nMost expensive item per unit: {most_valuable['item_name']} "
          f"(${float(most_valuable['unit_price']):.2f})")

    total_value = sum(int(row['quantity']) * float(row['unit_price']) for row in items)
    print(f"\nTotal value of current inventory: ${total_value:.2f}")
