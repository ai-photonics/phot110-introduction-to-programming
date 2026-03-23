# This script showcases command line arguments using argparse

# The argparse package provides more options for handling arguments
import argparse

print("\nStart script")
parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="dividend")
parser.add_argument("m", type=int, help="divisor")
parser.add_argument("-v", "--verbosity", action="count", default=0)
parser.add_argument("-d", "--decimal-result", action="count", help="return a decimal result instead of the integer division", default=False)
args = parser.parse_args()

if args.decimal_result:
    quotient = args.n / args.m
else:
    quotient = args.n // args.m

remainder = args.n % args.m

if (args.verbosity >= 1) and (args.decimal_result is False):
    print(f"{args.n}/{args.m} = {quotient}, with rest = {remainder}")
elif (args.verbosity >= 1) and (args.decimal_result):
    print(f"{args.n}/{args.m} = {quotient} (as a decimal number)")
else:
    print(quotient)
print("End\n")
