import math
import numpy as np
##from bitstring import BitArray


"""
We pass a file remove the header 

We have 10 columns 

get the domain range of 10 columns. 

Create a list of array of this. 

match our values and update the numbers. 

prtuern the data. 

"""

##class ue_encode():


def main(domain, response):
       print (domain, response)
       encode_array = np.zeros(len(domain))
       for k in domain:
        if response == k :
            encode_array[domain.index(k)]=1
            a=_peturb (0.25,0.75,encode_array)
            print (a)

def _peturb(p,q,encode_array):
     sanitized_vec = np.zeros(4)
     for bit in range(4):
       sample = np.random.random()
       if encode_array[bit] == 1:
        if sample <= p:
            sanitized_vec[bit] = 1
       else:
        if sample <= q:
            sanitized_vec[bit] = 1
     return sanitized_vec


__name__ == '__main__'

domain =[1,2,3,4]
main(domain,4)


    

"""
    def _peturb(self,p,q, data)
         for index in encode_array:
            if index == 1 and rnd <=p; 
      """         
"""
     
    def aggregate :
         p and q ka vlaue chaiye 



    def elipson_to_p_q(self, elipson):
        # elipson. 


def _encode_(elpsion)
    if; 
    uae. encode. 

__name__= __main__






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

"""