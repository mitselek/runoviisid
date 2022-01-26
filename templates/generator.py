from ast import If
import re
import xml.etree.ElementTree as ET


def eKeySig(keys):
    e_root = ET.Element('KeySig')
    e_acc = ET.SubElement(e_root, 'accidental')
    e_acc.text = str(keys)
    return e_root

def eTimeSig(sigN, sigD):
    sigN = str(sigN)
    sigD = str(sigD)

    e_root = ET.Element('TimeSig')

    if re.search('[^0-9]', sigN):
        textN = sigN
        ET.SubElement(e_root, 'textN').text = textN
        ET.SubElement(e_root, 'textD').text = sigD
        sigN = sum(list(map(int, re.split(r"[^0-9]+", sigN))))
    
    ET.SubElement(e_root, 'sigN').text = str(sigN)
    ET.SubElement(e_root, 'sigD').text = str(sigD)
    return e_root

def eVbox(kogujad, maakond):
    e_root = ET.Element('VBox')
    e_composer = ET.SubElement(e_root, 'Text')
    ET.SubElement(e_composer, 'style').text = 'Composer'
    ET.SubElement(e_composer, 'text').text = str(kogujad)
    e_lyricist = ET.SubElement(e_root, 'Text')
    ET.SubElement(e_lyricist, 'style').text = 'Lyricist'
    ET.SubElement(e_lyricist, 'text').text = str(maakond)
    return e_root


tree = ET.parse('template.mscx')

root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

ks = eKeySig(-1)
ts = eTimeSig('3·2·2', '4')

print(ET.tostring(ks, encoding='utf8'))
print(ET.tostring(ts, encoding='utf8'))

e_staff = root.find('Score').find('Staff')
e_vbox = e_staff.find('VBox')
e_staff.remove(e_vbox)
e_staff.insert(0, eVbox('Maakond ja nr', 'Kogujad kõik koos'))

print(ET.tostring(e_staff, encoding='utf8'))
