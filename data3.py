import csv
import numpy as np

def getdata(data):
    size = []
    time = []
    with open(data) as f:
        r1 = csv.DictReader(f)
        for i in r1:
            size.append(float(i["Marks In Percentage"]))
            time.append(float(i["Days Present"]))

    return{"x":size,"y":time}


def find(source):
    correlation = np.corrcoef(source["x"],source["y"])
    print(correlation[0,1])


def main():
    data = "data3.csv"
    source = getdata(data)
    find(source)


main()
