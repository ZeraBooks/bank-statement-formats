# Chase bank statement layout

How a Chase business statement is laid out, and what one month looks like
once its sections are merged into a single dated list with a signed Amount
column. The full guide, with download steps and what goes wrong when the PDF
is copied into Excel, is ZeraBooks' [Chase bank statement to Excel](https://www.zerabooks.com/chase-bank-statement-to-excel).

## Layout

A Chase business checking statement typically prints, in this order:

| Section | What it holds | Becomes |
|---|---|---|
| Checking Summary | Beginning balance, a total and instance count for each section, ending balance | The proof, not rows |
| Deposits and Additions | Deposits, incoming transfers, refunds | Type Deposit, positive |
| Checks Paid | Check number, date paid, amount | Type Check, negative |
| ATM & Debit Card Withdrawals | Card purchases and ATM cash, when there is a debit card | Type Withdrawal, negative |
| Electronic Withdrawals | ACH payments, bill pay, outgoing transfers | Type Withdrawal, negative |
| Fees | Monthly service fee and other charges | Type Fee, negative |
| Daily Ending Balance | One balance per day with activity | Nothing: it repeats balances |

Quirks: transaction dates print as MM/DD with the year only in the statement
period; every amount prints positive and the section says which way it went;
ACH descriptions often wrap onto a second line.

Download the PDF from chase.com, main menu, Statements & documents (up to 7
years online, depending on the account). The activity CSV has no beginning or
ending balance, so it can't be proven.

Section and column names vary a little between products and years; treat this
as the usual pattern, not a specification.

## Sample

`sample-converted.csv` is a fictional month: Ridgeline Plumbing LLC, business checking ending 4417, July 2026. Opening balance
8,642.18 plus the Amount column equals the printed closing balance
9,877.33. Check it in Python:

```python
import csv
from decimal import Decimal
rows = list(csv.DictReader(open("sample-converted.csv")))
print(Decimal("8642.18") + sum(Decimal(r["Amount"]) for r in rows))  # 9877.33
```

All names, account numbers and amounts are made up.
