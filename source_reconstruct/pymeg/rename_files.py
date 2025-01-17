import os
from os import rename
from glob import glob

path = '/home/pmurphy/Surprise_drug/Analysis/MEG/Conv2mne_induced/'

subjects = {'CMC': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'CPG': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'CTG': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'CYK': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,5,'r2')],
            'EJG': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'FDC': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,2,'r1'), (2,3,'r1'), (2,4,'r2'), (2,5,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'FLW': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'FNC': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'GHT': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'HFK': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'HOG': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'ICD': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'JPK': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'LOK': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'MDC': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'MJQ': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'MLC': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'NDT': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'OIG': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'QLW': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'RGT': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'ROW': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'RPC': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'TMW': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,2,'r1'), (3,3,'r1'), (3,4,'r2'), (3,5,'r2')],
            'UDK': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'UOC': [(1,1,'r1'), (1,3,'r1'), (1,4,'r2'), (1,5,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'URG': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'UXQ': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'VTQ': [(1,1,'r1'), (1,2,'r1'), (1,3,'r1'), (1,4,'r2'), (1,5,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')],
            'XUE': [(1,1,'r1'), (1,2,'r1'), (1,3,'r2'), (1,4,'r2'), (2,1,'r1'), (2,2,'r1'), (2,3,'r2'), (2,4,'r2'), (3,1,'r1'), (3,2,'r1'), (3,3,'r2'), (3,4,'r2')]}


for subject, tasks in subjects.items():
    for session, recording, run in tasks:
        globstring = '%s%s-SESS%i-%i-*.hdf' % (path, subject, session, recording)  # retrieve filenames of all files for this subj/session/recording (all signal types & chunks)
        filename = glob(globstring)
        for src in filename:
            dst = src[0:70] + run + '-' + src[70:]
            os.rename(src, dst)
            #print(src)
            #print(dst)
            #print('')
        