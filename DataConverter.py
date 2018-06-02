# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:21:29 2018

@author: DST_AI
"""

filename = r"C:\Users\DST_AI\Desktop\Test_Data\test_and_diagnosis_output.CSV"
outfilename=r"C:\Users\DST_AI\Desktop\Test_Data\diagnosis_result.CSV"


def patGen(l):
    out=''
    for s in l:
        if s=='present' or s=='normal':
            out=out+'1.0'+','
        elif s=='absent' or s=='abnormal':
            out=out+'0.0'+','
        elif s=='total_loss':
            out=out+'0.0'+','
        elif s=='red-green_loss':
            out=out+'0.25'+','
        elif s=='blue-yellow_loss':
            out=out+'0.75'+','
        elif s=='wasting'or s=='wasted':
            out=out+'0.5,'
        elif s=='right':
            out=out+'0.75,'
        elif s=='left':
            out=out+'0.25,'
        elif s=='none':
            out=out+'0.0,'
        elif s=='100':
            out=out+'1.0,'
        elif s=='50':
            out=out+'0.5,'
        elif s=='central':
            out=out+'0.5,'
        elif s=='flattened':
            out=out+'0.0,'
        elif s=='deviated_to_right':
            out=out+'0.75,'
        elif s=='deviated_to_left':
            out=out+'0.25,'
        elif s=='weak':
            out=out+'0.5,'
        elif s=='to_right':
            out=out+'0.75,'
        elif s=='to_left':
            out=out+'0.25,'
        elif s=='increased':
            out=out+'0.75,'
        elif s=='decreased':
            out=out+'0.25,'
        elif s=='NA':
            out=out+'0.5,'
        elif s=='1+'or s=='1':
            out=out+'0.6'+','
        elif s=='2+'or s=='2':
            out=out+'0.7,'
        elif s=='3+'or s=='3':
            out=out+'0.8,'
        elif s=='4+'or s=='4':
            out=out+'0.9,'
        elif s=='6/6':
            out=out+'1.0,'
        elif s=='0/6':
            out=out+'0.0,'
        elif s=='6/12'or s=='6/18'or s=='6/9'or s=='6/36'or s=='6/60':
            out=out+'0.8,'
        elif s=='2/6'or s=='3/6'or s=='5/6':
            out=out+'0.5,'
        elif s=='AC_>_BC':
            out=out+'1.0,'
        elif s=='BC_>_AC':
            out=out+'0.0,'
        elif s=='midline':
            out=out+'1.0,'
        elif s=='lateralised_to_left':
            out=out+'0.25,'
        elif s=='lateralised_to_right':
            out=out+'0.75,'
        elif s=='5':
            out=out+'1.0,'
        elif s=='0':
            out=out+'0.0,'
        else:
            out=out+'0.0'+','
    return out


def outDataGen(lout):
    outdata=''
    for s1 in lout:
         if s1=='olfaction normal':
            outdata=outdata+'1.0,1.0,'
         elif s1=='abnormal':
            outdata=outdata+'0.0,'
         elif s1=='bilateral olfaction absent':
            outdata=outdata+'0.0,0.0,'
         elif s1=='left olfaction absent':
            outdata=outdata+'0.0,1.0,'
         elif s1=='right olfaction absent':
            outdata=outdata+'1.0,0.0,'
         elif s1=='visual acuity normal':
            outdata=outdata+'1.0,1.0,'
         elif s1=='bilateral vision absent':
            outdata=outdata+'0.0,0.0,'
         elif s1=='visual acuity decreased':
            outdata=outdata+'0.0,0.0,'
         elif s1=='right visual acuity decreased':
            outdata=outdata+'0.0,0.5,'
         elif s1=='left visual acuity decreased':
            outdata=outdata+'0.5,0.0,'
         elif s1=='bilateral visual acuity decreased':
            outdata=outdata+'0.5,0.5,'
         elif s1=='right vision absent':
            outdata=outdata+'1.0,0.0,'
         elif s1=='left vision absent':
            outdata=outdata+'0.0,1.0,'
         elif s1=='visual field normal':
            outdata=outdata+'1.0,1.0,'
         elif s1=='left vision absent':
            outdata=outdata+'0.0,1.0,'
         elif s1=='right vision absent':
            outdata=outdata+'1.0,0.0,'
         elif s1=='right nasal field defect':
            outdata=outdata+'0.5,0.0,'
         elif s1=='right temporal field defect':
            outdata=outdata+'1.0,0.5,'
         elif s1=='left nasal field defect':
            outdata=outdata+'0.5,0.0,'
         elif s1=='left temporal field defect':
            outdata=outdata+'0.5,1.0,'
         elif s1=='right homonymous hemianopia':
            outdata=outdata+'1.0,0.25,'
         elif s1=='left homonymous hemianopia':
            outdata=outdata+'0.25,1.0,'
         elif s1=='bitemporal hemianopia':
            outdata=outdata+'0.25,0.25,'
         elif s1=='binasal hemianopia':
            outdata=outdata+'0.75,0.75,'
         elif s1=='right homonymous quadrantanopia':
            outdata=outdata+'0.0,0.25,'
         elif s1=='left homonymous quadrantanopia':
            outdata=outdata+'0.25,0.0,'
         elif s1=='insufficient data':
            outdata=outdata+'0.5,0.5,'
         elif s1=='normal viii nerve':
            outdata=outdata+'1.0,1.0,'
         elif s1=='right sensorineural deafness':
            outdata=outdata+'1.0,0.0,'
         elif s1=='left sensorineural deafness':
            outdata=outdata+'0.0,1.0,'
         elif s1=='right conductive deafness':
            outdata=outdata+'1.0,0.5,'
         elif s1=='left conductive deafness':
            outdata=outdata+'0.5,1.0,'
         else:
             outdata=outdata+s1+','
    return outdata


# =============================================================================
# elif s1=='craniopharyngioma':
#             outdata=outdata+'0.0,0.0,1.0,'
#          elif s1=='left vestibular schwannoma':
#             outdata=outdata+'0.1,0.0,1.0,'
#          elif s1=='right vestibular schwannoma':
#             outdata=outdata+'0.1,0.0,1.0,'
# =============================================================================

inputfile = open('converteddata.csv','w')
with open(filename) as f:
     for line in f:
         i=0
         dict1={}
         ##mylist.append([n for n in line.strip().split(',')])
         mylist = []
         mylist=line.split(",")
         if len(mylist)!=1:
             formno=mylist[1]
             l = mylist[3::2]
             s1=patGen(l)
             inputfile.write(formno+','+s1+'\n')
             print(formno)
             print(len(mylist))

 # =============================================================================
 #         st=len(mylist)
 #         print('length',len(mylist))
 #         while i<st-1:
 #             dict2={mylist[i]:mylist[i+1]}
 #             dict1.update(dict2)
 #             i=i+2
 #             
 #             
 #             
 # =============================================================================
inputfile.close()



outfile = open('int_outdata.csv','w')
with open(outfilename) as fo:
     for line in fo:
         mylist = []
         lin=line.lower()
         mylist=lin.split(",")
         ##mylist.append([n for n in line.strip().split(',')])
         if len(mylist)!=1:         
             s1=outDataGen(mylist)
             
             outfile.write(s1)
           #  outfile.write('\n')
           
               
outfile.close()
  


# =============================================================================
# def diagDataGen(lout):
#          outdata=''
#          s1=lout
#          if s1=='C7-D1 traumatic subluxation':
#             return '0,0,0,0,0,0'
#          elif s1=='D11-12 fracture subluxation' or s1=='D11-12 subluxation':
#             return '0,0,0,0,0,1'
#          elif s1=='SCIWORA D12-L1':
#             return '0,0,0,0,1,0'
#          elif s1=='C7-D1 grade IV traumatic subluxation':
#             return '0,0,0,0,1,1'
#          elif s1=='CVJ anamoly':
#             return '0,0,0,1,0,0'
#          elif s1=='L1-L4 ependymoma':
#             return '0,0,0,1,0,1'
#          elif s1=='L1 burst fracture':
#             return '0,0,0,1,1,0'
#          elif s1=='C6-7 grade II subluxation':
#             return '0,0,0,1,1,1'
#          elif s1=='C5-6 traumatic subluxation' or s1=='C5-6 subluxation':
#             return '0,0,1,0,0,0'
#          elif s1=='L4-5PIVD':
#             return '0,0,1,0,0,1'
#          elif s1=='C5 injury':
#             return '0,0,1,0,1,0'
#          elif s1=='D12 Fracture':
#             return '0,0,1,0,1,1'
#          elif s1=='High Cervical Whiplash':
#             return '0,0,1,1,0,0'
#          elif s1=='C3 Fracture':
#             return '0,0,1,1,0,1'
#          elif s1=='Craniopharyngioma' or s1=='craniopharyngioma' or s1=='craniopharyngiona' or s1=='craniopharyngioma\'':
#             return '0,0,1,1,1,0'
#          elif s1=='Pitutary Macroadenoma':
#             return '0,0,1,1,1,1'
#          elif s1=='Right spenopetroclival meningioma':
#             return '0,1,0,0,0,0'
#          elif s1=='Right CP angle lesion':
#             return '0,1,0,0,0,1'
#          elif s1=='D10 burst fracture':
#             return '0,1,0,0,1,0'
#          elif s1=='L2 burst fracture':
#             return '0,1,0,0,1,1'
#          elif s1=='L2 vertebral body fracture':
#             return '0,1,0,1,0,0'
#          elif s1=='D12 fracture':
#             return '0,1,0,1,0,1'
#          elif s1=='D2-3 subluxation traumatic':
#             return '0,1,0,1,1,0'
#          elif s1=='D11 burst fracture':
#             return '0,1,0,1,1,1'
#          elif s1=='C6 subluxation':
#             return '0,1,1,0,0,0'
#          elif s1=='C5-6 subluxation':
#             return '0,1,1,0,0,1'
#          elif s1=='L2 compression fracture':
#             return '0,1,1,0,1,0'
#          elif s1=='C5-6 anterior subluxation':
#             return '0,1,1,0,1,1'
#          elif s1=='L2 vertebral body fracture':
#             return '0,1,1,1,0,0'
#          elif s1=='C4-5 suluxation':
#             return '0,1,1,1,0,1'
#          elif s1=='C4-5 compression':
#             return '0,1,1,1,1,0'
#          elif s1=='C2-4 OPLL':
#             return '0,1,1,1,1,1'
#          elif s1=='C3-4 subluxation':
#             return '1,0,0,0,0,0'
#          elif s1=='C6-7 subluxation':
#             return '1,0,0,0,0,1'
#          elif s1=='Left vestibular schwannoma' or s1=='Left Vestibular schwannoma' or s1=='Left Vestibular Schwannoma':
#             return '1,0,0,0,1,0'
#          elif s1=='NF2':
#             return '1,0,0,0,1,1'
#          elif s1=='Right cavarnous sinus lesion':
#             return '1,0,0,1,0,0'
#          elif s1=='Residual vestibular schwannoma':
#             return '1,0,0,1,0,1'
#          elif s1=='Right vestibular schwannoma' or s1=='right vestibular schwannoma':
#             return '1,0,0,1,1,0'
#          elif s1=='Left glomus tumour':
#             return'1,0,0,1,1,1'
#          elif s1=='Atlanto axial dislocation and basilar invagination and Atlanto occipital dislocation':
#             return '1,0,1,0,0,0'
#          elif s1=='Non-Functioning Pituitary Macro-Adenoma ' or s1=='Non-Functioning Pituitary Macro-Adenoma' or s1=='NON FUNCTIONING PITUITARY ADENOMA':
#             return '1,0,1,0,0,1'
#          elif s1=='C4 burst fracture' or s1=='C4 burst fracture ':
#             return '1,0,1,0,1,0'
#          else:
#             return s1
# =============================================================================




# =============================================================================
# outfile1 = open('diagnosisencode.csv','w')
# with open(outfilename) as fo:
#      for line in fo:
#          mylist = []
#          lin=line
#         # lin=line.lower()
#          mylist=lin.split(",")
#          ##mylist.append([n for n in line.strip().split(',')])
#          if len(mylist)!=1:         
#              s2=diagDataGen(mylist[1])
#              print('myList',mylist[1])
#              print(s2)
#              outfile1.write(s2)
#              outfile1.write('\n')
#          
#              
# outfile1.close()
# =============================================================================
