# QFX

A QFX file is a bank or credit card download made for Quicken's Web Connect
import. It is plain OFX text with one extra tag from Intuit, `INTU.BID`, which
identifies the bank. Each transaction sits in an `STMTTRN` record with a date,
a signed amount, a payee and a `FITID`.

The `FITID` is the bank's unique ID for that transaction on that account. A
plain-English walkthrough of the format is in ZeraBooks' guide,
[What is a QFX file?](https://www.zerabooks.com/what-is-a-qfx-file)

## Files in this folder

| File | What it is |
|---|---|
| `sample.qfx` | A fictional Example Bank checking download for September 2026: five transactions, ledger and available balances. Comments explain each block. |

Everything in `sample.qfx` is made up: the bank, routing and account numbers,
FITIDs, payees and amounts. The comments use SGML comment syntax inside the body
only. Strip them before testing an import, because some readers reject comments.

## Layout at a glance

1. **Header.** `KEY:VALUE` lines before any tags. `VERSION:102` with
   `DATA:OFXSGML` is the older SGML style (OFX 1.x), where single values have no
   closing tag. OFX 2.x files are XML and close every tag.
2. **Sign-on (`SONRS`).** Server time, the bank's `ORG` and `FID`, and
   `INTU.BID`. Quicken checks `INTU.BID` against the banks taking part in Web
   Connect.
3. **Statement (`STMTRS`).** Currency, the account (`BANKID`, `ACCTID`,
   `ACCTTYPE`), the date range (`DTSTART`, `DTEND`) and the transactions.
4. **Balances.** `LEDGERBAL` and `AVAILBAL` as of the end of the range. There is
   no opening balance.

## Notes for anyone parsing these

- **Dedupe on account plus `FITID`.** The OFX standard requires a FITID to be
  unique within an account and allows up to 255 characters. It is not required
  to be in order.
- **Trust the sign, not `TRNTYPE`.** Amounts are signed by their effect on the
  account. Money out is negative.
- **`NAME` is capped at 32 characters.** Extra detail, when sent, is usually in
  `MEMO`.
- **`CHARSET:1252` means Windows-1252,** not UTF-8.
- **Dates** look like `20260902120000.000[-4:EDT]`. Some banks send only the
  first 8 digits.
- **History is short.** The standard lets software ask for all available
  history, but each bank decides how much it serves; many give about 90 days
  through Web Connect.

## FAQ

### Is a QFX file the same as an OFX file?

Almost. A QFX file is an OFX file with Intuit's tags added, mainly `INTU.BID`.
Most programs that read OFX also read QFX, but Quicken looks for the Intuit tags
and expects the bank to be one it supports.

### Why does Quicken say my QFX file is from an unsupported bank?

Quicken checks the `INTU.BID` in the file against the banks that take part in
Web Connect. If the bank is not on that list, or the file has no `INTU.BID`,
Quicken can refuse it even when the transactions inside are fine. Ask the bank
whether it still supports Quicken downloads.

### Does a QFX file include the opening balance?

No. It carries the transactions for the date range and the ledger and available
balances at the end. Proving a month is complete needs both ends, which the PDF
statement prints.
