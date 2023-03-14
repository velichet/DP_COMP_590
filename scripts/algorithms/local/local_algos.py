import math
import numpy as np
from bitstring import BitArray

def encode(num):
    bits = int(max(8, math.log(num, 2)+1))
    return [1 if num & (1 << (bits-1-n)) else 0 for n in range(bits)]

def perturb(encoded_response):
    return [perturb_bit(b) for b in encoded_response]

def perturb_bit(bit):
    p = .8
    q = .05

    sample = np.random.random()
    if bit == 1:
        if sample <= p:
            return 1
        else:
            return 0
    elif bit == 0:
        if sample <= q:
            return 1
        else: 
            return 0
        
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
nums_dp = []
for age in nums:
    nums_dp.append(BitArray(perturb(encode(age))).uint)

print(sum(nums)/len(nums))
print(sum(nums_dp)/len(nums_dp))