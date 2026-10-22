# TD Canada Trust business account statement layout

How a TD Canada Trust business chequing statement is typically laid out, and what one month
looks like once its debit and credit columns are merged into a single dated
list with a signed Amount column. Canadian statements share a pattern that
trips up converters built on US layouts: "cheque" spelling, separate debit and
credit columns, a running balance, and dates printed without the year. The
general method is in ZeraBooks' [bank statement converter](https://www.zerabooks.com/bank-statement-converter) guide.

## Layout

TD business statements typically print an activity table with a description, separate debit and credit amounts, the date and a running balance. The column order differs from RBC, so map columns by header name, not by position.

| Column | What it holds | Becomes |
|---|---|---|
| Date | Posting date, printed as day and month with no year | Date, with the year from the statement period |
| Description | Payee or transaction type and reference, sometimes over two lines | Description |
| Cheques and debits | Money out, printed without a minus | Amount, negative |
| Deposits and credits | Money in | Amount, positive |
| Balance | Running balance, often printed only on the last transaction of a day | Nothing: used to check |

A summary near the top of the first page prints the opening balance, total
debits, total credits and closing balance.

Column names, wording and the position of the balance column vary by account
type and year. This is the usual pattern, not a specification, and we have not
checked it against every TD Canada Trust account type.

## Quirks that matter when converting

- Dates carry no year, so a January statement that starts with a late-December
  posting needs the year from the statement period, not from the first row.
- Amounts print with a comma for thousands and a point for decimals (1,420.50).
  Some CSV downloads from Canadian banks use a comma for decimals in
  French-language profiles, so check before you import.
- Fees such as the monthly account fee are ordinary debit rows. They are easy
  to miss because they sit at month end with no payee.
- A cheque is a debit row with a number in the description. Keep the number so
  it can be matched to the cheque register.
- A foreign-currency account prints its own opening and closing balance in that
  currency; do not mix it into a Canadian-dollar proof.

## Sample

`sample-converted.csv` is a fictional month: Maple Harbour Cleaning Inc., business chequing, August
2026, in Canadian dollars. Opening balance 3105.60 plus the Amount column equals
the closing balance 5883.12. Check it in Python:

```python
import csv
from decimal import Decimal
rows = list(csv.DictReader(open("sample-converted.csv")))
print(Decimal("3105.60") + sum(Decimal(r["Amount"]) for r in rows))  # 5883.12
```

All names, account details and amounts are made up.
