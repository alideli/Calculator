# Calculator

A simple Python calculator that supports basic arithmetic operations and allows the user to set the number of decimal places for the result.

## Features
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Power (**)
- Percentage (a % b calculates 'a percent of b')
- User-defined decimal places for result display

## How to Use
1. Run the program.
2. Enter the first number (integer or decimal).
3. Enter the operator: one of "+ - * / ** %".
4. Enter the second number.
5. Enter the number of decimal places you want for the result (e.g., 2 or 4). If you enter nothing or an invalid value, the default is 4.
6. The result will be displayed.

### Example
```
Please enter first number: 12.5
You can use "+ - * / ** %"
Please enter your operate: *
Please enter second number: 3
Please enter decimal value (default: 4): 2
12.5 * 3.0 = 37.50
```

## Notes
- If you enter an invalid decimal value, the default (4) will be used.
- For percentage, the first number is calculated as a percent of the second number.

## Run
To run the program, use the following command in your terminal:

```
python Calculator.py
```

## Author
- alideli