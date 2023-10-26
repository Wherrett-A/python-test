import sys, args

argsStart = args.Start(sys.argv)
argsStart.add_arg(['-name', '-n'], help='input name')
argsStart.add_arg(['-age', '-a'], help='input age')
argsStart.process()