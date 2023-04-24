# Ingester
Ingester is a tool for transferring product master data to MaxCarton

## Installation
1. Clone repo from [here] (https://github.com/b0uncer52/Ingester.git)
2. Install python 3.11 from [here] (https://www.python.org/downloads/)
3. Install [pip](https://pip.pypa.io/en/stable/) with this command in the console 
```bash
py -m pip install --upgrade pip
```
4. Install [requests] (https://pypi.org/project/requests/) with this command in the console
```bash
pip install requests
```

## Usage 
1. Open command console 
2. Move to directory ~\Ingester
3. Have your csv file with master product data accessible from machine
4. Enter command 
```bash
py ingester.py
```
5. Follow prompts to map the file columns and send data to MaxCarton API