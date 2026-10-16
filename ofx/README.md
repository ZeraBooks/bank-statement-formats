# OFX (Open Financial Exchange)

## What is an OFX file?

An OFX file is a bank, credit card or brokerage download in Open Financial
Exchange, a format Microsoft, Intuit and CheckFree announced in January 1997.
It is tagged plain text: SGML in versions 1.0 to 1.6, XML from version 2.0
(the current banking version is 2.3).

Each transaction is an `STMTTRN` record with a posting date (`DTPOSTED`), a
signed amount (`TRNAMT`) and a unique ID (`FITID`). The specification has been
maintained by the Financial Data Exchange (FDX) since 2019.

## Files in this folder

| File | What it is |
|---|---|
| `example-card-2026-09.ofx` | Fictional OFX 2.2 (XML) credit card statement for "Example Card", September 2026, five transactions, every line commented |

All data here is made up. No real issuer, account or person.

## How to tell 1.x from 2.x

| | OFX 1.x | OFX 2.x |
|---|---|---|
| First line | `OFXHEADER:100` | `<?xml version="1.0" ...?>` |
| Syntax | SGML | XML |
| Leaf values | No closing tag: `<TRNAMT>-64.18` | Closed: `<TRNAMT>-64.18</TRNAMT>` |
| Grammar | DTD | XML Schema |
| Loads in an XML parser | No | Yes |

## Rules the sample demonstrates

- **Dates.** `YYYYMMDDHHMMSS.XXX[offset:TZ]`, year first, no separators. Banks
  may truncate from the right; a date-only value such as `20260903` is read as
  the start of that day in GMT. Converting it to a North American time zone
  shows the previous day.
- **Signs.** `TRNAMT` is signed by the effect on the customer. On a card, a
  purchase is negative and a payment or refund positive. `LEDGERBAL` is
  negative when money is owed.
- **TRNTYPE is a label.** Software follows the sign. `INT` appears on both
  interest earned (positive) and interest charged (negative).
- **No opening balance.** A statement download carries `LEDGERBAL` at the end
  and nothing at the start. The comment above `LEDGERBAL` in the sample shows
  how to derive the implied opening balance and what to check it against.
- **Card blocks.** Cards use `CREDITCARDMSGSRSV1` > `CCSTMTTRNRS` >
  `CCSTMTRS` and `CCACCTFROM`, which has no routing number.

## Reading OFX in code

The open-source Python library `ofxtools` reads both 1.x and 2.x, and QFX.

## FAQ

### Is OFX still used?

Yes. Banks, card issuers and brokerages still offer OFX, QFX and QBO downloads,
and the Financial Data Exchange says OFX is in use at over 7,000 financial
institutions. Newer bank connections run on APIs, but a file download is still
the fallback when a connection breaks.

### Is a QBO file an OFX file?

Yes. A QBO file is the QuickBooks Web Connect format, which is OFX with Intuit's
tags added. ZeraBooks does not read or create QBO files.

### Can I edit an OFX file by hand?

You can, in any text editor, but a wrong tag or a flipped sign makes the import
fail or post the wrong way. If one transaction is wrong, it is usually safer to
import the file and fix that transaction in your software.

## More

A full annotated walkthrough of the format, with the 1.x vs 2.x table, date
and sign rules, and which programs open OFX files:
[What is an OFX file?](https://www.zerabooks.com/what-is-an-ofx-file)

Note: ZeraBooks itself does not read or create OFX, QFX or QBO files; it
converts PDF statements to Excel and CSV.
