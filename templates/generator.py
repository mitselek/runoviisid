from ast import If
from base64 import encode
from os import EX_PROTOCOL
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


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

def eRest(sigN, sigD):
    sigN = str(sigN)
    sigD = str(sigD)

    e_root = ET.Element('Rest')
    ET.SubElement(e_root, 'durationType').text = 'measure'
    sigN = str(sum(list(map(int, re.split(r"[^0-9]+", sigN)))))
    ET.SubElement(e_root, 'duration').text = '/'.join((sigN, sigD))
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


# set the stage
measures = re.split(r" +", '2/4 3·2·2/8 3/8 3/8 3/8 3/4')
root = ET.parse('template.mscx').getroot()

# for child in root:
#     print(child.tag, child.attrib)


# print(ET.tostring(ks, encoding='utf8'))
# print(ET.tostring(ts, encoding='utf8'))

e_staff = root.find('Score').find('Staff')
e_staff.clear()
e_staff.insert(0, eVbox('Maakond ja nr', 'Kogujad kõik koos'))


ks = eKeySig(-1)
firstmeasure = True
prevmeasure = False
for measure in measures:
    e_measure = ET.Element('Measure')
    e_voice = ET.SubElement(e_measure, 'voice')
    if firstmeasure:
        firstmeasure = False
        e_voice.append(ks)
        
    if measure != prevmeasure:
        sigN, sigD = measure.split('/')
        ts = eTimeSig(sigN, sigD)
        e_voice.append(ts)
    
    prevmeasure = measure

    rest = eRest(sigN, sigD)
    e_voice.append(rest)
    e_staff.append(e_measure)

    print(measure)


def indent(elem, level=0):
    i = "\n" + level*"._"
    j = "\n" + (level-1)*"__"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + ".."
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem        


# save it

print()

with open('out.mscx', 'wb') as f:
    mxml_string = ET.tostring(root, encoding='utf8')
    f.write(mxml_string)
    # soup = BeautifulSoup(mxml_string)
    # f.write(soup.prettify(encoding='utf8'))
