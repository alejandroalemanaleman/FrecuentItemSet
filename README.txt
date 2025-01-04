# Frequent Itemset

## Prerequisites

Before running the code, ensure you have the following packages installed in your Python environment:

- mrjob (https://pypi.org/project/mrjob/)
- setuptools (https://pypi.org/project/setuptools/)

You can install them by running:

pip install mrjob
pip install setuptools

## How to Run

To execute the script, use the following command.
You can adjust the values of the parameters --min-support and --k as needed:

- python frequent_itemset.py transactions.txt --min-support=2 --k=2