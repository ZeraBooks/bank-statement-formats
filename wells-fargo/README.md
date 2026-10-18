# Wells Fargo bank statement layout

How a Wells Fargo business statement is laid out, and what one month looks like
once its sections are merged into a single dated list with a signed Amount
column. The full guide, with download steps and what goes wrong when the PDF
is copied into Excel, is ZeraBooks' [Wells Fargo bank statement to Excel](https://www.zerabooks.com/wells-fargo-bank-statement-to-excel).

## Layout

A Wells Fargo business statement typically prints one transaction table:

| Column | What it holds | Becomes |
|---|---|---|
| Date | Posting date, M/D | Date, with the year from the statement period |
| Check Number | Filled only for checks | Kept in the description; Type Check |
| Description | Payee and reference, often over two lines | Description |
| Deposits/Credits | Money in | Amount, positive |
| Withdrawals/Debits | Money out, printed without a minus | Amount, negative |
| Ending daily balance | Only on the last transaction of each day | Nothing: used to check |

An activity summary above the table prints beginning balance, total credits,
total debits and ending balance.

Download the PDF from Wells Fargo Online, Statements & Documents (up to 7 years
for checking and savings, 2 years for credit cards). The activity download
covers recent activity only and has no printed balances.

Section and column names vary a little between products and years; treat this
as the usual pattern, not a specification.

## Sample

`sample-converted.csv` is a fictional month: Cedar Row Landscaping, business checking ending 0965, August 2026. Opening balance
5,318.44 plus the Amount column equals the printed closing balance
8,191.26. Check it in Python:

```python
import csv
from decimal import Decimal
rows = list(csv.DictReader(open("sample-converted.csv")))
print(Decimal("5318.44") + sum(Decimal(r["Amount"]) for r in rows))  # 8191.26
```

All names, account numbers and amounts are made up.
