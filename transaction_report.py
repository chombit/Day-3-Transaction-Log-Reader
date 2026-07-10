INPUT_FILE = "transactions.txt"
OUTPUT_FILE = "report.txt"

def read_transactions(filename):
    
    totals = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 2:
                    continue
                name, amount_str = parts
                try:
                    amount = float(amount_str)
                except ValueError:
                    continue
                totals[name] = totals.get(name, 0) + amount
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the path.")
        return {}
    return totals


def print_summary(totals):
    sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    for name, total in sorted_totals:
        print(f"{name}: {total:.2f}")


def write_report(totals, filename):
    sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    with open(filename, "w") as f:
        for name, total in sorted_totals:
            f.write(f"{name}: {total:.2f}\n")


def main():
    totals = read_transactions(INPUT_FILE)
    print_summary(totals)
    write_report(totals, OUTPUT_FILE)


if __name__ == "__main__":
    main()
