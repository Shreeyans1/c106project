import csv
import numpy as np

def getdata(data):
    size = []
    time = []
    with open(data) as f:
        r1 = csv.DictReader(f)
        for i in r1:
            size.append(float(i["Coffee in ml"]))
            time.append(float(i["sleep in hours"]))

    return{"x":size,"y":time}


def find(source):
    correlation = np.corrcoef(source["x"],source["y"])
    print(correlation[0,1])


def main():
    data = "data4.csv"
    source = getdata(data)
    find(source)


main()
