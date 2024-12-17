# Cocaine machine
An application  where the user input takes in spesific coins to pay the due bill 
A program to insert specific coins to pay a due bill.
Usage : type in the terminal python coke.py,
wait for the prompt then type some integers which is listed.

The application was implemented as an assignment at CS50P
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.<br>
[Demo : Vending Machine](https://cs50.harvard.edu/python/2022/psets/2/coke/)

##  Testing framework
No testing framework used in the project

## Installation
1. Clone the repository:
```sh
git clone https://github.com/krigjo25/console-cocainemachine-py.git
```

2. Navigate to the project directory
```sh
cd console-cocainemachine-py
```

3. Install the requirements
```sh
pip install -r requirements.txt
```
4. Run the file
```sh
python app.py
```

##  Usage
To use the application, run the following command in your terminal

```sh
Usage : type in the terminal python app.py, wait for the prompted message
then type in some names.
python app.py
```
Replace `<Name>` with the desired name, seperate the names with comma to add multiple name

## Example
```sh

python app.py

Amount Due: <5>
Type in a coin: 5

expected output:
Change owed: <0>
```
`Amount due <5>` is replaced with a random integer between 5-1000 
`Type in a coin <5>` replace it with the desired integer
`Change owed <5>` is replaced with the amount the user will retrieve 

## LICENCE

The application is under [The Unlicensed](./LICENCE).

##  Testing framework
The testing framwork for this project is pytest
which is used to test the application. 
To use the application, run the following command in your terminal:
```sh
pytest test_bank.py
```

## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,<br>
@krigjo25
