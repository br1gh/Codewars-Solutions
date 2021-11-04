#codewars.com/kata/52763db7cffbc6fe8c0007f8/python
def tongues(code):
    a = 'aiyeoubkxznhdcwgpvjqtsrlmfAIYEOUBKXZNHDCWGPVJQTSRLMF'
    b = 'eouaiypvjqtsrlmfbkxznhdcwgEOUAIYPVJQTSRLMFBKXZNHDCWG'
    return ''.join([b[a.index(code[i])] if code[i] in a else code[i] for i in range(len(code))])
