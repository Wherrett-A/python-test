class Start:
    def __init__(self, inputted):
        self.inputted = inputted
        self.args = []
        self.helps = []

    def add_arg(self, arg, help='', ):
        self.args.append(arg)
        self.helps.append(help)

    def output(self):
        for n in range(len(self.args)):
            print(', '.join(self.args[n]), '\t', self.helps[n])

    def process(self):
        for arg in self.inputted:
            match arg:
                case '-h' | '-help':
                    print(f'usage: {self.inputted[0]} <args> \n')
                    print('optional arguments:')
                    print('▔' * 30)
                    for n in range(len(self.args)):
                        print(', '.join(self.args[n]), '\t', self.helps[n])
                    print('▔' * 30)
