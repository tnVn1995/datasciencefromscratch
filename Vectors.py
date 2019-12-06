# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:27:24 2019

@author: ngu09790
"""

from typing import List
Vector = List[float]

height_weight_age = [70, 170, 40]

grades = [95,80,75,62]

#%%
def add(v:Vector, w:Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    
    return [v_i + w_i for v_i, w_i in zip(v,w)]

assert add([1,2,3],[4,5,6]) == [5,7,9]

#%%

def subtract(v:Vector, w:Vector) -> Vector:
    """Subtracts corresponding elements"""
    
    assert len(v) == len(w), "vectors must be the same length"
    
    return []

#%%
p = (41 + 26 + 32 +28 +39) / (200*5)
sigma = np.sqrt(p*(1-p)/200)