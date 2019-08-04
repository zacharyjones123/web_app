# web_app
This Python project is mean to be the backend support for the Kara Library application. I have pip installed the mysql and mysql connector

What is an ISBN?

An ISBN is named the International Standard Book Number. ISBN's were 10 digits in length up to the end of 2006, but since the beginning of 2007 they now always consist of 13 digits. ISBNs are calculated using a specific mathematical formula and include a check digit to validate the number.

![github-small](https://www.isbn-international.org/sites/default/files/styles/internal_page/public/what%20is%20an%20ISBN%20%281%29%20English%20revised.png?itok=FdECBknf)

Prefix element - currently this can only be either 978 or 979. It is always 3 digits in length

Registration group element - this identifies the particular country, geographical region, or language area participating in the ISBN system. This element may be between 1 and 5 digits in length

Registrant element - this identifies the particular publisher or imprint. This may be up to 7 digits in length

Publication element - thie identifies the particular edition and format of a specific title. This may be up to 6 digits in length

Check digit - This is always the final single digit that mathematically validate the rest of the number and it is calculated using a Modulus 10 system with alternate weights of 1 and 3

The ISBN is machine-readable in the form of a 13-digit EAN-13 bar code. This is fast and avoids mistakes.

Source: https://www.isbn-international.org/
