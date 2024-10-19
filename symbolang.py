import sys

#source = 'hello.symb'

class Symbolang:
    def __init__(self, source='none'):
        self.y = 0
        self.x = 0
        self.direction='right'

        self.running = False
        if source != 'none':
            self.file_to_source_code(source)
        else:
            while True:
                #Repl()
                possible_file = input("Symbolang REPL (type source file) >>")
                try:
                    self.file_to_source_code(possible_file)
                except FileNotFoundError:
                    self.throw_error("That's not a valid file!")

    def start_run(self):
        self.direction = 'right'
        #print(self.cursor['dir'])
        self.run_prgm()

    def run_prgm(self):
        #for i in range(len(self.file_content[0])):

        self.running = True
        while self.running != False:
            try:
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

                elif self.direction == 'down' and self.running == True:
                    self.y += 1
                    self.item_check(self.file_content[self.y][self.x])
                    #print(self.file_content[self.y][self.x])

                elif self.direction == 'up' and self.running == True:
                    self.y -= 1
                    self.item_check(self.file_content[self.y][self.x])
                    #print(self.file_content[self.y][self.x])


                elif self.y == len(self.file_content):
                    self.throw_error('reached end of line. exiting.')        #self.running = False
                    self.running = False
            except KeyboardInterrupt:
                self.throw_error('\n\nGot keyboard interrupt, exiting program...')
            #for row in range(len(self.file_content)):
            #    for item in self.file_content[row]:
            #        self.item_check(item)
            #    self.running = False


    def item_check(self, item):
        self.item = item
        if self.item == '>':
            self.direction = 'right'
            #print(self.direction, end=' ')

        elif self.item == 'v':
            self.direction = 'down'
            #print(self.direction, end=' ')

        elif self.item == '<':
            self.direction = 'left'
            #print(self.direction, end=' ')

        elif self.item == '^':
            self.direction = 'up'
            #print(self.direction, end=' ')

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


    def file_to_source_code(self, file):
        self.source = file
        try:
            if list(self.source.split('.'))[1] !=  'symb':
                self.throw_error('invalid file extension')

                #try:
                #    self.file = open(self.source+'.symb', 'r')
                #except FileNotFoundError:
                #    self.throw_error('file not found (try adding a .symb to the end\nas the file extension)')
            elif list(self.source.split('.'))[1] ==  'symb':
                self.file = open(self.source, 'r')
        except IndexError:
            self.throw_error('no file extension')
        self.file_content = []
        self.line_content = []
        #self.row =

        for line in self.file:
            self.file_content.append(list(line.split()))#.append('\n'))

        self.start_run()
        #print(self.file_content)
class Repl(Symbolang):
    pass

if __name__ == '__main__':
    try:
        Symbolang(sys.argv[1])
    except IndexError:
        print('You have to specify a file to open!!')
        quit()
