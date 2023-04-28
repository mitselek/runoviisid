# -*- coding: utf-8 -*-
# Python 3.7.3

import re
import xml.etree.ElementTree as ET
import csv
import numpy as np

# constants
C_DUR   = A_MOLL   =  0
G_DUR   = E_MOLL   =  1
D_DUR   = B_MOLL   =  2
A_DUR   = Fis_MOLL =  3
E_DUR   = Cis_MOLL =  4
B_DUR   = Gis_MOLL =  5
Fis_DUR = Dis_MOLL =  6
Cis_DUR = As_MOLL  =  7
Cb_DUR  = Ab_MOLL  = -7
Gb_DUR  = Eb_MOLL  = -6
Db_DUR  = Bb_MOLL  = -5
Ab_DUR  = F_MOLL   = -4
Eb_DUR  = C_MOLL   = -3
Bb_DUR  = G_MOLL   = -2
F_DUR   = D_MOLL   = -1


# Create an array of time signatures and yield them one by one.
# The array is repeated as needed.
def timeSigGenerator(timeSigs):
    # timeSigs = "4/4 2/4"
    timeSigs = timeSigs.split(' ')
    n = len(timeSigs)
    i = 0
    while True:
        yield timeSigs[i]
        i = (i + 1) % n

def eKeySig(keys):
    e_root = ET.Element('KeySig')
    e_acc = ET.SubElement(e_root, 'accidental')
    e_acc.text = str(keys)
    return e_root

def eStaffText(line1, line2):
    e_root = ET.Element('StaffText')
    e_text = ET.SubElement(e_root, 'text')
    e_text.text = str(line1) + '\n' + str(line2)
    return e_root

def eLyrics(line):
    e_root = ET.Element('StaffText')
    e_placement = ET.SubElement(e_root, 'placement')
    e_placement.text = 'below'
    e_align = ET.SubElement(e_root, 'align')
    e_align.text = 'left,baseline'
    e_text = ET.SubElement(e_root, 'text')
    e_text.text = str(line)
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

    e_groups = ET.SubElement(e_root, 'Groups')
    n32ths = int(int(sigN) * 32 / int(sigD))
    for i in range(n32ths):
        e_node = ET.SubElement(e_groups, 'Node')
        e_node.set('pos', str(i))
        e_node.set('action', str(273))

    return e_root

def eRest(measure):
    sigN, sigD, subtype = splitMeasure(measure)

    e_root = ET.Element('Rest')
    ET.SubElement(e_root, 'durationType').text = 'measure'
    sigN = str(sum(list(map(int, re.split(r"[^0-9]+", sigN)))))
    ET.SubElement(e_root, 'duration').text = '/'.join((sigN, sigD))
    return e_root

def eLastBarLine():
    e_root = ET.Element('BarLine')
    ET.SubElement(e_root, 'subtype').text = 'end'
    return e_root

def eVbox(maakond, kogujad):
    e_root = ET.Element('VBox')
    ET.SubElement(e_root, 'height').text = '4'
    ET.SubElement(e_root, 'bottomGap').text = '2'
    ET.SubElement(e_root, 'boxAutoSize').text = '0'
    e_composer = ET.SubElement(e_root, 'Text')
    ET.SubElement(e_composer, 'style').text = 'composer'
    ET.SubElement(e_composer, 'text').text = str(kogujad)
    e_poet = ET.SubElement(e_root, 'Text')
    ET.SubElement(e_poet, 'style').text = 'poet'
    ET.SubElement(e_poet, 'text').text = str(maakond)
    return e_root

# set the stage
# ID,takte,eeltakt,mõõt,maakond,kogujad,tekst
# 0017-r,2,,3/4,17. Vändra,Saar (13),"E: Õl--mes hõ-be-kü-ba-ra,"

sourceDir = 'templates/'
with open(sourceDir + 'runoviisid - export.csv', newline='', encoding='utf-8') as csvfile:

    root = ET.parse(sourceDir + 'score_template.xml').getroot()

    e_staff = root.find('Score').find('Staff')
    e_staff.clear()

    e_section_break = ET.Element('LayoutBreak')
    e_subtype = ET.SubElement(e_section_break, 'subtype')
    e_subtype.text = 'section'

    counter = 0
    first, last = (2515, 2584)

    for row in csv.DictReader(csvfile, delimiter=',', quotechar='"'):
        # if not row['tekst']:
        #     continue

        # log the keys and values of row
        # print(row['ID'], row.values())
        
        counter += 1
        if counter < first:
            continue
        if counter > last:
            break

        e_staff.append(eVbox(row['maakond'], row['kogujad']))

        if row['eeltakt']:
            e_measure = ET.Element('Measure')
            e_measure.set('number', '0')
            e_measure.set('len', row['eeltakt'])
            e_staff.append(e_measure)
            e_voice = ET.SubElement(e_measure, 'voice')
            e_voice.append(eKeySig(G_DUR))
            e_voice.append(eLyrics(row['tekst']))
            e_measure.set('ID', row['ID'])
            e_voice.append(eRest(row['eeltakt']))


        timeSigs = timeSigGenerator(row['mõõt'])
        lastTimeSig = None
        takte = int(row['takte'])
        for i in range(takte):
            e_measure = ET.Element('Measure')
            e_measure.set('number', str(i + 1))
            e_staff.append(e_measure)
            e_voice = ET.SubElement(e_measure, 'voice')

            if i == 0 and not row['eeltakt']:
                e_voice.append(eKeySig(G_DUR))
                # e_voice.append(eStaffText(row['maakond'], row['kogujad']))
                e_voice.append(eLyrics(row['tekst']))
                e_measure.set('ID', row['ID'])
            
            if i == takte - 1:
                # print('section break at', row['ID'], i, 'of', takte, 'measures')
                e_measure.append(e_section_break)
                e_measure.set('Last', '1')


            currentTimeSig = next(timeSigs)
            if currentTimeSig != lastTimeSig:
                e_voice.append(eTimeSig(currentTimeSig))
                lastTimeSig = currentTimeSig

            e_voice.append(eRest(currentTimeSig))
        
        e_voice.append(eLastBarLine())


    with open(sourceDir + 'out.mscx', 'wb') as f:
        f.write(ET.tostring(root, encoding='utf8'))
