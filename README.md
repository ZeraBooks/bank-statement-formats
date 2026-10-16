# Bank statement formats

Reference files for the bank and card download formats people run into when
they need transactions in a spreadsheet or an accounting system: one folder per
format, each with a fictional sample file and notes on how the format behaves
in practice.

| Folder | Format | Guide |
|---|---|---|
| [qfx](qfx/) | Quicken Web Connect (OFX with Intuit's INTU.BID tag) | [What is a QFX file?](https://www.zerabooks.com/what-is-a-qfx-file) |
| [ofx](ofx/) | Open Financial Exchange, 1.x SGML and 2.x XML | [What is an OFX file?](https://www.zerabooks.com/what-is-an-ofx-file) |

Every bank name, account number, payee and amount in these files is made up.

Maintained by [ZeraBooks](https://www.zerabooks.com). ZeraBooks itself reads PDF
statements and writes Excel or CSV checked against each statement's printed
opening and closing balances; it does not read or write QFX or OFX files.
Corrections and additional formats are welcome as pull requests.
