# Bank statement formats

Bank-by-bank PDF statement layouts (Chase, Bank of America, Wells Fargo, Capital One, RBC, TD) and
sample download files. QFX and OFX are tagged text files that banks and card issuers offer as
transaction downloads. OFX (Open Financial Exchange) is the open standard, and
QFX is OFX with Intuit's `INTU.BID` tag added so Quicken accepts it. Neither
carries an opening balance, so a download alone can't prove a month is
complete.

| Folder | Format | Guide |
|---|---|---|
| [`qfx/`](qfx/) | Quicken Web Connect (OFX with Intuit's INTU.BID tag) | [What is a QFX file? The format line by line](https://www.zerabooks.com/what-is-a-qfx-file) |
| [`ofx/`](ofx/) | Open Financial Exchange, 1.x SGML and 2.x XML | [What is an OFX file? How the format is put together](https://www.zerabooks.com/what-is-an-ofx-file) |
| [`chase/`](chase/) | Chase business checking PDF layout, with a converted sample month | [Chase bank statement to Excel](https://www.zerabooks.com/chase-bank-statement-to-excel) |
| [`bank-of-america/`](bank-of-america/) | Bank of America business statement layout and how its section names changed | [Bank of America statement to Excel](https://www.zerabooks.com/bank-of-america-statement-to-excel) |
| [`wells-fargo/`](wells-fargo/) | Wells Fargo's single transaction table with separate credit and debit columns | [Wells Fargo statement to Excel](https://www.zerabooks.com/wells-fargo-bank-statement-to-excel) |
| [`capital-one/`](capital-one/) | Capital One credit card statement: which sections become rows and how the card proof works | [Capital One statement to Excel](https://www.zerabooks.com/capital-one-statement-to-excel) |
| [`rbc/`](rbc/) | RBC Royal Bank business chequing: debit and credit columns, dates without a year, a sample month in CAD | [Bank statement converter](https://www.zerabooks.com/bank-statement-converter) |
| [`td/`](td/) | TD Canada Trust business chequing: same debit and credit pattern with a different column order, a sample month in CAD | [Bank statement converter](https://www.zerabooks.com/bank-statement-converter) |

Every bank name, account number, payee and amount in these files is made up.

## How to use these files

- Open a `.qfx` or `.ofx` file in any text editor. The comments explain each
  block.
- Strip the comments before testing an import, because some readers reject
  them.
- To read either format in code, the open-source Python library `ofxtools`
  handles OFX 1.x, OFX 2.x and QFX.

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). Free to use and adapt with credit to ZeraBooks.

Maintained by [ZeraBooks](https://www.zerabooks.com). ZeraBooks itself reads PDF
statements and writes Excel or CSV checked against each statement's printed
opening and closing balances; it does not read or write QFX or OFX files.
Corrections and additional formats are welcome as pull requests.
