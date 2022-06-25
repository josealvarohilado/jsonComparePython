import json

def printKeys(data, str, arr = []):
    arr.append(str)
    arrStr = str.split('.')
    if len(arrStr) > 0:
        useStr = arrStr[len(arrStr) - 1]
    else:
        useStr = str
    if isinstance(data[useStr], dict):
        for key in data[useStr].keys():
            printKey = str + "." + key
            # print(printKey)
            arr = printKeys(data[useStr], printKey, arr)
    return arr

def getValueFromDict(data, arr):
    for key in arr:
        try:
            data = data[key]
        except KeyError:
            print('"' + key + '"' + " field does not exist in data object")
    return data

f1 = open('sample.json')
f2 = open('sample2.json')

data1 = json.load(f1)
data2 = json.load(f2)

if data1 != data2:
    for key in data1.keys():
        keysArr = []
        keysArr = printKeys(data1, key, keysArr)
        # compare with data 2
        for arrStr in keysArr:
            keyInArr = arrStr.split('.')
            value1 = getValueFromDict(data1, keyInArr)
            value2 = getValueFromDict(data2, keyInArr)
            if value1 != value2:    
                if isinstance(value1, list):
                    value1 = ', '.join(value1)

                if isinstance(value2, list):
                    value2 = ', '.join(value2)
                
                if (isinstance(value1, str) and isinstance(value2, str)):
                    print("Values are not the same on the following field: " + arrStr)
                    print( " Value Data 1 > " + value1)
                    print( " Value Data 2 > " + value2)
else:
    print("Both JSON files are the same")