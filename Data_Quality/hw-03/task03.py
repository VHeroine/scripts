#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser(description='Solving a polynomial.')
parser.add_argument('-a', nargs='+', type=float, dest='a', default=[0.0])
parser.add_argument('-x', nargs='?', type=float, dest='x', default=0.0)
parser.add_argument('-v', '--verbose', action="store_true", help='Increase output verbosity.')
args = parser.parse_args()

sum = 0
j = 0
for i in args.a:
   sum = sum + i * args.x**(len(args.a)-1-j)
   j+=1
j = 0

if not args.verbose:
   print(sum)
else:
   for i in range(len(args.a)-1):
      print(f'{args.a[i]}*{args.x**(len(args.a)-1-i)}+', end='')
   print(f'{args.a[len(args.a)-1]}*{args.x**(len(args.a)-1)}={sum}')