

import xml.etree.ElementTree as ET
tree = ET.parse('data/country_data.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)
print(root.text)

for child in root:
    print(child.tag, child.attrib, child.get('name'))
    
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

print(root[0][1].text)
    
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)



# Modify XML

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('data/output.xml')

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('data/removed_output.xml')




#########

xml_text = """<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor>
        <name>John Cleese</name>
        <fictional:character>Lancelot</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <fictional:character>Sir Robin</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Commander Clement</fictional:character>
    </actor>
</actors>"""


print(xml_text)

root = ET.fromstring(xml_text)
ns = {
    'real_person':'http://people.example.com',
    'role' : 'http://characters.example.com'
}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print(name.text)
    for char in actor.findall('role:character', ns):
        print('|-->',char.text)

###### Create XML
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)



################### XPath
# Supported XPath Syntax: https://docs.python.org/2/library/xml.etree.elementtree.html#supported-xpath-syntax

root = tree.getroot()

# Top-level elements
print(len(root.findall(".")))
list(map(lambda x: print(x.tag), root.findall(".")))

# All 'neighbor' grand-children of 'country' children of the top-level
# elements

print(len(root.findall("./country/neighbor")))
#list(map(lambda x: print(x.get('name')), root.findall("./country/neighbor")))
list(map(ET.dump, root.findall("./country/neighbor")))
    




# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")


# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")



# For XML with namespaces, use the usual qualified {namespace}tag notation:
root.findall(".//{http://purl.org/dc/elements/1.1/}title")


# ET functions: https://docs.python.org/3.8/library/xml.etree.elementtree.html#functions




import xmltodict, json
print(json.dumps(xmltodict.parse("""
<mydocument has="an attribute">
  <and>
    <many>elements</many>
    <many>more elements</many>
  </and>
  <plus a="complex">
    element as well
  </plus>
</mydocument>
"""), indent=4))
