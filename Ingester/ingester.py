import csv
import time
import requests

endpoint = "https://maxcartonapi.azurewebsites.net/product/new"
def setRowIndex(headerName, headers) :
    index = -1
    try:
        index = headers.index(headerName)
    except ValueError:
        index = input("Please enter column number for " + headerName + ":")
    return int(index)

def verifyYesNo(question) :
    while True :
        response = input(question + " Y/N")
        if response == 'Y' or response == 'y':
            return True
        if response == 'N' or response == 'n':
            print("The program is terminating")
            time.sleep(2)
            quit()
        else :
            print("Invalid input")

def rowToData(row) :
    splitRow = row.split(',')
    name = splitRow[nameRow].strip()
    description = splitRow[descriptionRow].strip()
    color = splitRow[colorRow].strip()
    size = splitRow[sizeRow].strip()
    data = {
        "name": name,
        "description": description,
        "color": color,
        "size": size
    }
    return data

def sendProductData(data) :
    print("Sending: " + data['name'])
    resp = requests.post(endpoint, json = data)
    print(resp)

csvLocation = input("Please enter csv file location: ")

expectedRows = ["name", "description", "color", "size"]

with open(csvLocation, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    firstLine = csvfile.readline()
    differentHeaders = firstLine.split(',')
    newHeaders = []
    i = 0
    for h in differentHeaders:
        newHeaders.append(h.strip())
        i = i + 1

    for index, h in enumerate(newHeaders):
        print(index, h)

    descriptionRow = setRowIndex("description", newHeaders)
    nameRow = setRowIndex('name', newHeaders)
    colorRow = setRowIndex("color", newHeaders)
    sizeRow = setRowIndex("size", newHeaders)

    counter = 1
    secondLine = csvfile.readline()
    secondLineData = rowToData(secondLine)
    print("Name: " + secondLineData['name'])
    print("Description: " + secondLineData['description'])
    print("Color: " + secondLineData['color'])
    print("Size: " + secondLineData['size'])
    verifyYesNo("Is this data correct? ")
    sendProductData(secondLineData)
    while True :
        nextLine = csvfile.readline() 
        if nextLine.strip() == '' :
            print(str(counter) + " products sent")
            break
        lineData = rowToData(nextLine)
        sendProductData(lineData)
        counter = counter + 1
