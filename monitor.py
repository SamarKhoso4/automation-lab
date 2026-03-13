import datetime

def main():
    admin = input("Enter your name: ")
    inventory = {
        "Workstations": 15,
        "Servers": 3,
        "Printers": 2
    }
    
    print(f"\n--- System Report for {admin} ---")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    
    for item, count in inventory.items():
        if count < 5:
            status = "LOW STOCK - Order More"
        else:
            status = "Healthy"
        print(f"{item}: {count} ({status})")

if __name__ == "__main__":
    main()
