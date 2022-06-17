import os
import access2thematrix
import numpy as np

#order -> datum, endung, expirementnummer, bildnummer_start, bildnummer_ende 
#traces vorwärts/rückwerts, hoch/runter
#bildnummer 01_01 bis 01_100 oder 100_01
#
#Script soll mit den oberen argumenten gestarted werden, einen neuen Ordner erstellen, die zu nutzenden daten plus den .mtrx header dorthin kopieren.
#Die benötigten Daten werden durch das Datum (input), Expiriment Nummer(Input) und Bildnummern eindeutig indentifiziert
#Aus den Daten soll ein 3D gwy Brick erstellt und als .gwy gespeichert werden. Das Tracing gibt dabei an welche daten an welcher stelle stehen sollen Metadaten ebenfalls 

#eventuell bildnummer array, wäre aber eher die ausnahme 

#neuer ordner mit kopierten rohdaten und gwy file
#.mtrx header mit kopieren
os.chdir(r"C:\Users\henni\Documents\GitHub\gwyfile_nrrd\tests\mtrxfiles")
slice_count = 37
brick_data = np.array()

mtrx_data = access2thematrix.MtrxData()
for i in range(slice_count,0,-1):

    data_file = r'2D_slices\20220307-161629_Ag(111)+PTCDA-5K-AFM_NonContact_QPlus_AtomManipulation_AuxChannels--192_%d.I_mtrx' %i
    traces, message = mtrx_data.open(data_file)

    im, message = mtrx_data.select_image(traces[0])

   
