import xml.etree.ElementTree as ET
import csv

tree = ET.parse("automobiles.xml")
root = tree.getroot()

records = list(root)

def get_paths(elem, parent=""):
    paths = {}
    
    for child in elem:
        new_key = parent + "_" + child.tag if parent else child.tag
        
        if list(child):
            paths.update(get_paths(child, new_key))
        else:
            paths[new_key] = child.text.strip() if child.text else ""
    
    return paths
headers = set()
all_data = []

for record in records:
    data = get_paths(record)
    all_data.append(data)
    headers.update(data.keys())

headers = list(headers)
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(headers)

    for data in all_data:
        row = [data.get(h, "") for h in headers]
        writer.writerow(row)

print(" CSV created!")