# Ingester
Ingester is a tool for transferring product master data to MaxCarton

## Installation
Clone repo from [here] (https://github.com/b0uncer52/Ingester.git)
Install python 3.11 from [here] (https://www.python.org/downloads/)
Install [pip](https://pip.pypa.io/en/stable/) with this command in the console 
```bash
py -m pip install --upgrade pip
```
Install [requests] (https://pypi.org/project/requests/) with this command in the console
```bash
pip install requests
```

## Usage 
Open command console 
Move to directory ~\Ingester
Have your csv file with master product data accessible from machine
Enter command 
```bash
py ingester.py
```
Follow prompts to map the file columns and send data to MaxCarton API