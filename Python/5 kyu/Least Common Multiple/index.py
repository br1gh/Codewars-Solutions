#codewars.com/kata/5259acb16021e9d8a60010af/python
def lcm(*args):
  if 0 in args: return 0
  args,mx = sorted(set(args)),1
  for i in args: mx *= i
  for i in range(min(args)*max(args),mx,max(args)):
      if all(not i%j for j in args): return i
  return mx
