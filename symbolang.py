

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
            if self.direction == 'right' and self.running == True:
                self.x += 1
                self.item_check(self.file_content[self.y][self.x])
                #print(self.file_content[self.y][self.x])


            elif self.x >= len(self.file_content[self.y]):
                self.throw_error('reached end of line. exiting.')        #self.running = False
                self.running = False

            elif self.direction == 'left' and self.running == True:
                self.x -= 1
                self.item_check(self.file_content[self.y][self.x])
                #print(self.file_content[self.y][self.x])


            #for row in range(len(self.file_content)):
            #    for item in self.file_content[row]:
            #        self.item_check(item)
            #    self.running = False


    def item_check(self, item):
        self.item = item
        if self.item == '>':
            self.direction = 'right'
            print(self.direction, end=' ')

        elif self.item == 'v':
            self.direction = 'down'
            print(self.direction, end=' ')

        elif self.item == '<':
            self.direction = 'left'
            print(self.direction, end=' ')

        elif self.item == '^':
            self.direction = 'up'
            print(self.direction, end=' ')

        elif self.item == '.':
            print('next-char', end=' ')

        elif self.item == '1':
            print(1, end=" ")

        elif self.item == 'e':
            self.throw_error('Reached end of program.')

        else:
            self.throw_error(f'ERROR! Unrecognised character! at char {self.x+1} and line {self.y+1}')


    def throw_error(self, error):
        print(error)
        quit()

Language(source)
