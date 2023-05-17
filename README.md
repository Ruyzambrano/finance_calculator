# Investment and Bond Calculator

This is a Python script that allows users to calculate either investment earnings or bond repayments based on the provided inputs. The user is prompted to choose between "investment" or "bond" calculations and then enters the required information accordingly.

## Requirements

To run this script, you need to have Python installed on your system. The script uses the `math` module, which is a built-in module in Python and does not require any additional installation.

## Usage

1. Open the script in a Python editor or IDE.
2. Run the script.
3. Choose either "investment" or "bond" from the menu presented.
4. Follow the prompts and provide the necessary information as requested.
5. The script will calculate and display the results based on the chosen calculation type.

## Calculation Types

### Investment

If you choose "investment" as the calculation type, the script will prompt you to enter the following information:

- Amount of money you are depositing
- Interest rate (as a percentage)
- Number of years you plan to invest
- Type of interest: "simple" or "compound"

The script will then calculate and display the earnings based on the provided inputs.

### Bond

If you choose "bond" as the calculation type, the script will prompt you to enter the following information:

- Present value of the house
- Interest rate (as a percentage)
- Number of months to repay the bond

The script will then calculate and display the monthly repayments and the total amount paid over the specified period.

## Example

```
Choose either 'investment' or 'bond' from the menu below to proceed:

Investment - to calculate the amount of interest you'll earn on your investment
Bond - to calculate the amount you'll have to pay on a home loan

Input here: investment

You have chosen investment.

How much money in R will you be investing? R5000
What percentage is your interest rate? 5
How many years will you be investing for? 3
Would you like to invest using simple or compound interest? compound

After 3 years, your initial investment of R5000.0 will earn R772.15. At the end of this period, it will be worth R5772.15.
```

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Please refer to the `LICENSE` file for more information.
