"""
GAVIP Example AVIS: Simple AVI

An example AVI pipeline is defined here, consisting of three tasks:

- DummyTask - demonstrates dependencies, but does nothing
- DownloadData - uses services.gacs.GacsQuery to run ADQL queries in GACS(-dev)
- ProcessData - generates a simple scatter plot with Bokeh from the downloaded data
@req: REQ-0006
@comp: AVI Web System
"""
import os
from django.conf import settings
# Class used for creating pipeline tasks
from pipeline.classes import (
    AviTask,
    AviParameter, AviLocalTarget,
)

inputFile = AviParameter()

def list_2(inputFile):
    with open(inputFile) as f:
        mylist = list(f)
        list_result=mylist[0]
        
    a=list_result.split()
    b=a[(len(a)-1)]
    c=b.split(']')
    d=c[0]
    a[(len(a)-1)] = d
    
    b=a[0]
    c=b.split('[')
    d=c[(len(c)-1)]
    a[0] = d
    
    new_list=[]
    for i in a:
        m=float(i)
        n=int(m)
        y=n+5
        new_list.append(y)

    b = str(new_list)
    a = b.encode('utf-8')
    return a


class AddNum(AviTask):

    inputFile = AviParameter()

    def output(self):
        return AviLocalTarget(os.path.join(
            settings.OUTPUT_PATH,
            "list_2.txt"
        ))

    def input(self):
        return AviLocalTarget(os.path.join(
            '/user_space/avi1_avi1/data/output', self.inputFile
        ))

    def run(self):
        list_result_2 = list_2(self.input().path)
        with open(self.output().path, 'wb') as out:
            print(list_result_2)
            out.write(list_result_2)

