import sys
def func(number=10):
    'prints a multipul times'
    for i in range(number):
        print('a')  
try:
	args=sys.argv[1]
except IndexError:
	args=input('number?')
if args.startswith('-'):
	obtion=args.strip('-')
	if obtion=='help':
		print(help(func))
	else:
		print('invailed order')
else:
	func(int(args))

