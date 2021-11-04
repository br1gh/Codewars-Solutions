#codewars.com/kata/54b72c16cd7f5154e9000457/python
import re
def decodeBits(bits):
    bits = bits.strip('0')
    u = len(min(re.findall('0+|1+', bits),key=len))
    for i,j in zip([u*3*'1',u*'1'],['-','.']): bits = re.sub(i,j,bits)
    return [[j.replace('0'*u,'') for j in i] for i in [k.split(u*3*'0') for k in bits.split(u*7*'0')]] 

def decodeMorse(morseCode):
    return ' '.join([''.join([MORSE_CODE[j] for j in i if j in MORSE_CODE]) for i in morseCode])
