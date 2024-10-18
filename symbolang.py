

source = 'hello.hi'

class Language:
    def __init__(self, source):
        #
        self.y = 0
        self.x = 0
        self.direction='right'

        self.running = False
        self.source = source
        self.file = open(source, 'r')
        self.file_content = []
        self.line_content = []
        #self.row =

        for line in self.file:
            self.file_content.append(list(line.split()))#.append('\n'))

        self.start_run()
        #print(self.file_content)
        #print(self.cursor['x'])

    def start_run(self):
        self.direction = 'right'
        #print(self.cursor['dir'])
        self.run_prgm()

    def run_prgm(self):
        #for i in range(len(self.file_content[0])):

        self.running = True
        while self.running != False:
            while self.direction == 'right' and self.running == True:
                self.item_check(self.file_content[self.y][self.x])
                print(self.file_content[self.y][self.x])
                self.x += 1
                if self.x >= len(self.file_content[self.y]):
                    print('exiting.')
                    self.running = False
            self.running = False

            #for row in range(len(self.file_content)):
            #    for item in self.file_content[row]:
            #        self.item_check(item)
            #    self.running = False


    def item_check(self, item):
        self.item = item
        if self.item == '>':
            self.direction = 'right'
            print(self.direction)

        elif self.item == 'v':
            self.direction = 'down'
            print(self.direction)

        elif self.item == '<':
            self.direction = 'left'
            print(self.direction)

        elif self.item == '^':
            self.direction = 'up'
            print(self.direction)

        elif self.item == '.':
            print('sassy')

        elif self.item == '1':
            print(1)

        else:
            print('ERROR! Unrecognised character!')
            quit()


Language(source)
