#!/usr/bin/env python3
"""Prove every sample month in this repository against its printed balances.

For each row of balances.csv, read <folder>/sample-converted.csv and check:
- the header is exactly Date,Description,Type,Amount
- every Date is YYYY-MM-DD and every row falls in one calendar month
- every Amount has exactly two decimals and no Description is blank
- bank:  opening + sum(Amount) == closing
- card:  previous balance - sum(Amount) == new balance (charges are negative
  and payments positive, as in capital-one/README.md)

Standard library only. Exit code 1 if any check fails.
Usage: python3 check_samples.py
"""
import csv
import re
import sys
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HEADER = ["Date", "Description", "Type", "Amount"]
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
AMOUNT = re.compile(r"^-?\d+\.\d{2}$")


def check(folder, kind, opening, closing):
    errors = []
    with open(ROOT / folder / "sample-converted.csv", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [r for r in reader if r]
    if header != HEADER:
        errors.append(f"header is {header}, expected {HEADER}")
    months = set()
    total = Decimal("0")
    for n, (date, desc, _type, amount) in enumerate(rows, start=2):
        if not DATE.match(date):
            errors.append(f"line {n}: date {date!r} is not YYYY-MM-DD")
        months.add(date[:7])
        if not desc.strip():
            errors.append(f"line {n}: blank description")
        if not AMOUNT.match(amount):
            errors.append(f"line {n}: amount {amount!r} needs exactly two decimals")
            continue
        total += Decimal(amount)
    if len(months) > 1:
        errors.append(f"rows span {sorted(months)}; a sample is one statement month")
    opening, closing = Decimal(opening), Decimal(closing)
    result = opening + total if kind == "bank" else opening - total
    if result != closing:
        errors.append(f"{kind} proof gives {result}, printed closing is {closing} (off by {result - closing})")
    return len(rows), result, errors


def main():
    failed = 0
    with open(ROOT / "balances.csv", newline="") as f:
        for b in csv.DictReader(f):
            count, result, errors = check(b["folder"], b["kind"], b["opening"], b["closing"])
            status = "ties" if not errors else "FAILS"
            print(f"{b['folder']:<16} {b['currency']} {count:>3} rows  {b['opening']:>10} -> {result:>10}  {status}")
            for e in errors:
                print(f"    {e}")
            failed += bool(errors)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
