#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 02:58:58 2020

@author: kimurayuudai
"""

import numpy as np
import matplotlib.pyplot as plt
from PyEMD import EMD
import ht


load1 = np.loadtxt('swing0701.txt')
load2 = np.loadtxt('swing1.txt')

N = load1.shape[0]
M = load1.shape[1]
fs = 120
t = np.linspace(0, N/fs, N)
dt = t[1] - t[0]

#swing1.txtからデータの取り出し
#swing_load = load[:,0]

# Execute EMD on signal
from MEMD_all import memd
imf1 = memd(load1)
imf2 = memd(load2)
result1 = imf1[:,0,:] #imf corresponding to 1st component
result2 = imf2[:,0,:]
#result = EMD().emd(a[:,0],t)


swing_N = result1.shape[0]-1
swing_M = result1.shape[1]
t2 = np.zeros((swing_M, swing_N))

for i in range(swing_N):
  t2[:,i] = np.linspace(0, swing_M/fs, swing_M)
'''
#EMD
swing_EMD = EMD().emd(swing_load, t)
swing_N = swing_EMD.shape[0]-1
swing_M = swing_EMD.shape[1]
t2 = np.zeros((swing_M, swing_N))

for i in range(swing_N):
  t2[:,i] = np.linspace(0, swing_M/fs, swing_M)
'''

#ヒルベルトファン変換
freq1,amp1 = ht.FAhilbert(result1,dt)

freq1_1 = freq1[int(1+fs/2):int(N-fs/2),:]
amp1_1 = amp1[int(1+fs/2):int(N-fs/2),:]

freq2,amp2 = ht.FAhilbert(result2, dt)

freq2_2 = freq2[int(1+fs/2):int(N-fs/2),:]
amp2_2 = amp2[int(1+fs/2):int(N-fs/2),:]

num=5
#plt.scatter(t2,freq,s=50,c=amp[0:swing_M,:],cmap='Blues')
#plt.scatter(t2[int(1+fs/2):int(N-fs/2)],freq2,s=50,c=amp2[0:swing_M,:],cmap='Blues')
#plt.scatter(t2[int(1+fs/2):int(N-fs/2)], freq1_1, s=50, c=amp1_1, cmap='Blues')
#plt.scatter(t2[int(1+fs/2):int(N-fs/2)], freq2_2, s=50, c=amp2_2, cmap='Reds')

plt.scatter(t2[int(1+fs/2):int(N-fs/2),num],freq1_1[:,num],s=50,c=amp1_1[:,num],cmap='Blues')
plt.scatter(t2[int(1+fs/2):int(N-fs/2),num],freq2_2[:,num],s=50,c=amp2_2[:,num],cmap='Reds')

#plt.scatter(t2[int(1+fs/2):int(N-fs/2)], freq2_2, s=50, c=amp2_2, cmap='Reds')
#plt.title('hip_Xpotation color -> amplitude')
plt.ylim(0,10)
#plt.xlabel('time[s]')
#plt.ylabel('freqency')

plt.colorbar()
