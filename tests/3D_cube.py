import access2thematrix
import numpy as np
import struct


mtrx_data = access2thematrix.MtrxData()


output_file = "3Dcube.nhrd.raw"
out_file = open(output_file,"wb")

for i in range(37,0,-1):
    print(i)


    data_file = r'C:\Users\Maximilian\Desktop\3D cube data\2022.03.09 - 3D cube data. 20pm height distance (z coordinate) between successive images starting with plus -20pm z_offset for image 192-1 and -40pm z_offset for 26-2-2 and so on\2D_slices\20220307-161629_Ag(111)+PTCDA-5K-AFM_NonContact_QPlus_AtomManipulation_AuxChannels--192_%d.I_mtrx' %i
    traces, message = mtrx_data.open(data_file)

    traces = {0: 'forward/up', 1: 'backward/up'}
    im, message = mtrx_data.select_image(traces[0])

    
    nestedlist = im.data.tolist()
    flatlist=[]
    for sublist in nestedlist:
        for element in sublist:
            flatlist.append(element)
    s = struct.pack('d'*len(flatlist), *flatlist)
    out_file.write(s)

out_file.close()
    
