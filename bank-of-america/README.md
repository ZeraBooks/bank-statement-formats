# Bank of America bank statement layout

How a Bank of America business statement is laid out, and what one month looks like
once its sections are merged into a single dated list with a signed Amount
column. The full guide, with download steps and what goes wrong when the PDF
is copied into Excel, is ZeraBooks' [Bank of America bank statement to Excel](https://www.zerabooks.com/bank-of-america-statement-to-excel).

## Layout

A Bank of America business statement typically prints, in this order:

| Section (recent statements) | Older statements called it | Becomes |
|---|---|---|
| Account summary | Account summary | The proof, not rows; also prints the number of deposits and credits |
| Deposits and other credits | Deposits and other additions | Type Deposit, positive |
| Withdrawals and other debits | Withdrawals and other subtractions; ATM and debit card subtractions | Type Withdrawal, negative |
| Checks | Checks | Type Check, negative |
| Service fees | Service fees | Type Fee, negative |
| Daily ledger balances | Daily ledger balances | Nothing: balances, not transactions |

Quirks: checks print in their own block, often in two columns side by side;
ACH descriptions run labelled fields together (Des:, ID:, Indn:); the
statement list in Online Banking filters by account and year.

Download the PDF from Online Banking, Accounts, Statements & Documents (6 years
online; older, up to 7, on request).

Section and column names vary a little between products and years; treat this
as the usual pattern, not a specification.

## Sample

`sample-converted.csv` is a fictional month: Bayview Dental Lab Inc., Business Advantage ending 7720, September 2026. Opening balance
21,406.90 plus the Amount column equals the printed closing balance
24,311.35. Check it in Python:

```python
import csv
from decimal import Decimal
rows = list(csv.DictReader(open("sample-converted.csv")))
print(Decimal("21406.90") + sum(Decimal(r["Amount"]) for r in rows))  # 24311.35
```

All names, account numbers and amounts are made up.
