import re
import xml.etree.ElementTree as ET
import csv
import numpy as np


def eKeySig(keys):
    e_root = ET.Element('KeySig')
    e_acc = ET.SubElement(e_root, 'accidental')
    e_acc.text = str(keys)
    return e_root

def splitMeasure(measure):
    if measure == 'C':
        return ('4', '4', '1')
    sigN, sigD = measure.split('/')
    return (sigN, sigD, False)
    
def eTimeSig(measure):
    sigN, sigD, subtype = splitMeasure(measure)

    e_root = ET.Element('TimeSig')

    if re.search('[^0-9]', sigN):
        textN = sigN
        ET.SubElement(e_root, 'textN').text = textN
        ET.SubElement(e_root, 'textD').text = sigD
        sigN = str(sum(list(map(int, re.split(r"[^0-9]+", sigN)))))
        print({'M': measure, 'TN': textN, 'SN': sigN, 'SD': sigD})
    
    if subtype:
        ET.SubElement(e_root, 'subtype').text = subtype

    ET.SubElement(e_root, 'sigN').text = sigN
    ET.SubElement(e_root, 'sigD').text = sigD
    return e_root

def eRest(measure):
    sigN, sigD, subtype = splitMeasure(measure)

    e_root = ET.Element('Rest')
    ET.SubElement(e_root, 'durationType').text = 'measure'
    sigN = str(sum(list(map(int, re.split(r"[^0-9]+", sigN)))))
    ET.SubElement(e_root, 'duration').text = '/'.join((sigN, sigD))
    return e_root


def eVbox(maakond, kogujad):
    e_root = ET.Element('VBox')
    e_composer = ET.SubElement(e_root, 'Text')
    ET.SubElement(e_composer, 'style').text = 'Composer'
    ET.SubElement(e_composer, 'text').text = str(kogujad)
    e_lyricist = ET.SubElement(e_root, 'Text')
    ET.SubElement(e_lyricist, 'style').text = 'Lyricist'
    ET.SubElement(e_lyricist, 'text').text = str(maakond)
    return e_root

def mxml(takte, eeltakt, mõõt, maakond, kogujad, tekst):
    takte = int(takte)
    measures = re.split(r" +", mõõt)
    measures = (measures * (takte // len(measures) + 1))[:takte]
    root = ET.parse('template.mscx').getroot()

    e_staff = root.find('Score').find('Staff')
    e_staff.clear()
    e_staff.insert(0, eVbox(maakond, kogujad))


    ks = eKeySig(1)
    firstmeasure = True
    prevmeasure = False
    for measure in measures:
        e_measure = ET.Element('Measure')
        e_voice = ET.SubElement(e_measure, 'voice')
        if firstmeasure:
            firstmeasure = False
            e_voice.append(ks)
            
        if measure != prevmeasure:
            print({measure})
            ts = eTimeSig(measure)
            e_voice.append(ts)
        
        prevmeasure = measure

        rest = eRest(measure)
        e_voice.append(rest)
        e_staff.append(e_measure)

        print(measure)


    return root

# set the stage
# ID,takte,eeltakt,mõõt,maakond,kogujad,tekst
with open('runoviisid - export.csv', newline='') as csvfile:
    for row in csv.DictReader(csvfile, delimiter=',', quotechar='"'):
        # if not row['tekst']:
            #continue

        print(row)
        e_mxml = mxml(row['takte'],row['eeltakt'],row['mõõt'],row['maakond'],row['kogujad'],row['tekst'])
        # continue
        print(ET.tostring(e_mxml, encoding='utf8'))
        with open('out/'+row['ID']+'.mscx', 'wb') as f:
            f.write(ET.tostring(e_mxml, encoding='utf8'))

