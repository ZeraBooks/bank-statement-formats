# Capital One card statement layout

How a Capital One credit card statement is laid out, and what one month looks
like once only the transactions are kept as rows with a signed Amount column.
The full guide, with download steps and the checking-account differences, is
ZeraBooks' [Capital One statement to Excel](https://www.zerabooks.com/capital-one-statement-to-excel).

## Layout

Capital One's own guide to reading its credit card statement names these
sections and says they are typical, not on every statement:

| Section | What it holds | Becomes |
|---|---|---|
| Payment information | Due date, new balance, minimum payment | The proof's end point, not rows |
| Account summary | Previous balance, period activity, credit limit | The proof's starting point, not rows |
| Rewards summary | Rewards earned and redeemed | Nothing: rewards are not money moving |
| Transactions | Payments, credits, purchases, fees, interest, balance transfers, cash advances | Rows, each with a Type and a signed Amount |
| Year-end summary | Fees and interest charged so far this year | Nothing: totals of lines already counted |
| Interest charge calculation | Rate, balance subject to interest, interest charged | Nothing: the interest is already a transaction |
| Account notifications | Fee explanations, AutoPay and other notices | Nothing |

The year-end summary and the interest calculation are where hand-copied
spreadsheets most often double-count, because both print amounts that look
like charges.

Download the PDF from capitalone.com: click the card or account, then View
statements. The transaction download for Quicken, QuickBooks or Excel has no
previous or new balance, so it can't be proven. Business checking statements
download from the checking account's own page and appear online only when the
account is set to paperless.

Section names vary between products and years; treat this as the usual
pattern, not a specification. We don't publish a Capital One checking column
map because we haven't read a published checking statement to stand behind one.

## Sample

`sample-converted.csv` is a fictional month: Harbor Lane Coffee, Spark
business card ending 6102, September 2026. Money out is negative and money
back is positive. For a card, the proof is previous balance minus the Amount
column equals the new balance: 3,846.20 - 112.56 = 3,733.64. Check it in
Python:

```python
import csv
from decimal import Decimal
rows = list(csv.DictReader(open("sample-converted.csv")))
print(Decimal("3846.20") - sum(Decimal(r["Amount"]) for r in rows))  # 3733.64
```

No interest was charged because the previous month was paid in full. The cash
back in the rewards summary is not in the file.

All names, account numbers and amounts are made up.
