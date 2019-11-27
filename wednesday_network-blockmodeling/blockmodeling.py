"""
This module contains some functions useful for indirect blockmodeling.

"""
import scipy as sc
import numpy as np
from scipy.stats.stats import pearsonr

def indirectSEhamming(mat):
  return indirectSE(mat,method='hamming')

def indirectSEcorr(mat):
  return indirectSE(mat,method='corr')

def indirectSE(mat,method):
  # Get size of matrix
  n=mat.shape[0]
  # Create target distance matrix	
  d = np.empty(shape=(n,n),dtype=float)
  for a1 in range(n):
    for a2 in range(n):
      if a1<=a2:
        # Initialize list with 2-tuples for checks
        v1=[]
        v2=[]
        for i in range(n):
          if i!=a1 and i!=a2:
            v1.extend([mat[a1,i],mat[i,a1]])
            v2.extend([mat[a2,i],mat[i,a2]])
          else:
            v1.append(mat[a1,a2])
            v2.append(mat[a2,a1])
        if method=='corr':
          val=pearsonr(v1,v2)[0]
        elif method=='hamming':
          val=0
          for i in range(len(v1)):
            if v1[i]!=v2[i]:
              val=val+1
        d[a1,a2]=val
        d[a2,a1]=val
  return d

def corr2dist(mat):
  return np.around((1-mat)/2,decimals=4)

def createBlockdict(partition):
  blockdict={}
  for i in np.unique(partition):
    blockdict[i]=[]
  for i in range(len(partition)):
    blockdict[partition[i]].append(i)
  return blockdict

def displayBlockdict(blockdict,nodelabels):
  for key,actors in blockdict.items():
    line="Position "+str(key)+":"
    vals=[]
    for i in actors:
      vals.append(nodelabels[i])
    line="Position "+str(key)+": "+", ".join(vals)
    print(line)
  
def displaySociomatrix(mat,nodelabels):
  n=len(nodelabels)
  for i in range(n):
    line=nodelabels[i]
    vals=[]
    for j in range(n):
      vals.append(mat[i,j])
    line=" ".join(str(x) for x in vals)+"\t"+nodelabels[i]
    print(line)

def displayBlockmodel(mat,blockdict,nodelabels):
  for rpos,rposactors in blockdict.items():
    for ractor in rposactors:
      #line=str(rpos)+" "+str(ractor)+"\t"
      line=""
      for cpos,cposactors in blockdict.items():
        vals=[]
        for cactor in cposactors:
          vals.append(mat[ractor,cactor])
        line=line+" ".join(str(x) for x in vals)+"|"
      width=len(line)
      line=line+" "+str(rpos)+" "+nodelabels[ractor]+" ("+str(ractor)+")"        
      #line=str(rpos)+" "+str(ractor)+nodelabels[ractor]+"\t"+" ".join(str(x) for x in vals)
      #line=" ".join(str(x) for x in vals)+" "+str(rpos)+" "+nodelabels[ractor]+" ("+str(ractor)+")"
      print(line)
    print ("-"*width)

def calcDensityBlockimage(mat,blockdict):
  n=len(blockdict)
  dbi=np.empty(shape=(n,n),dtype=float)
  for rpos in blockdict:
    for cpos in blockdict:
      count=0
      sum=0
      for ractor in blockdict[rpos]:
        for cactor in blockdict[cpos]:
          if ractor!=cactor:
            count=count+1
            sum=sum+mat[ractor,cactor]
      dbi[rpos-1,cpos-1]=sum/count
  return(dbi)