def calculate_bill(pu, cu, cust_type):
    # rates can be changed to match assignment requirements
    rates = {
        "domestic": {"FC": 50.0, "CC": 25.0, "ED_rate": 0.05},
        "commercial": {"FC": 100.0, "CC": 50.0, "ED_rate": 0.10},
        "industrial": {"FC": 200.0, "CC": 100.0, "ED_rate": 0.15},
    }

    key = cust_type.strip().lower()
    if key not in rates:
        raise ValueError(f"Unknown customer type: {cust_type}")

    ec = pu * cu
    fc = rates[key]["FC"]
    cc = rates[key]["CC"]
    ed = ec * rates[key]["ED_rate"]
    total = ec + fc + cc + ed
    return ec, fc, cc, ed, total

def main():
    try:
        pu = float(input("Enter PU (per-unit rate): ").strip())
        cu = float(input("Enter CU (units consumed): ").strip())
        cust_type = input("Enter customer type (Domestic/Commercial/Industrial): ").strip()
        ec, fc, cc, ed, total = calculate_bill(pu, cu, cust_type)
        print(f"EC(Energy Charges): {ec:.2f}")
        print(f"FC(Fixed Charges): {fc:.2f}")
        print(f"CC(Customer Charges): {cc:.2f}")
        print(f"ED(Electricity Duty Charges): {ed:.2f}")
        print(f"Total Bill: {total:.2f}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
# filepath: c:\Users\sunil\OneDrive\Desktop\AIAPS\assignment-3\task-1.py
def calculate_bill(pu, cu, cust_type):
    # rates can be changed to match assignment requirements
    rates = {
        "domestic": {"FC": 50.0, "CC": 25.0, "ED_rate": 0.05},
        "commercial": {"FC": 100.0, "CC": 50.0, "ED_rate": 0.10},
        "industrial": {"FC": 200.0, "CC": 100.0, "ED_rate": 0.15},
    }

    key = cust_type.strip().lower()
    if key not in rates:
        raise ValueError(f"Unknown customer type: {cust_type}")

    ec = pu * cu
    fc = rates[key]["FC"]
    cc = rates[key]["CC"]
    ed = ec * rates[key]["ED_rate"]
    total = ec + fc + cc + ed
    return ec, fc, cc, ed, total

def main():
    try:
        pu = float(input("Enter PU (per-unit rate): ").strip())
        cu = float(input("Enter CU (units consumed): ").strip())
        cust_type = input("Enter customer type (Domestic/Commercial/Industrial): ").strip()
        ec, fc, cc, ed, total = calculate_bill(pu, cu, cust_type)
        print(f"EC(Energy Charges): {ec:.2f}")
        print(f"FC(Fixed Charges): {fc:.2f}")
        print(f"CC(Customer Charges): {cc:.2f}")
        print(f"ED(Electricity Duty Charges): {ed:.2f}")
        print(f"Total Bill: {total:.2f}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()