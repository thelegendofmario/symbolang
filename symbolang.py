import sys, random, time

#source = 'hello.symb'

class Symbolang:
    def __init__(self, arg1, source='none'):
        self.y = 0
        self.x = 0
        self.direction='right'
        self.stack = []
        self.stringmode = False



        self.running = False
        if arg1 == '--run':
            if source != 'none':
                self.file_to_source_code(source)
            else:
                pass
                # while True:
                #     #Repl()
                #     possible_file = input("Symbolang REPL (type source file) >>")
                #     try:
                #         self.file_to_source_code(possible_file)
                #     except FileNotFoundError:
                #         self.throw_error("That's not a valid file!")

        elif arg1 == '--debug':
            if source != 'none':
                self.file_to_source_code(source, debug=True)
            else:
                pass

    def start_run(self, debug=False):
        self.direction = 'right'
        #print(self.cursor['dir'])
        if debug == True:
            self.run_prgm(True)
        else:
            self.run_prgm(False)


    def run_prgm(self, dbg):
        #for i in range(len(self.file_content[0])):

        self.running = True
        while self.running != False:
            try:


                if self.direction == 'right' and self.running == True:
                    self.x += 1
                    self.item_check(self.file_content[self.y][self.x])
                    if dbg == True: print(self.file_content[self.y][self.x]), print(self.stack)                    


                elif self.x >= len(self.file_content[self.y]):
                    self.throw_error('reached end of line. exiting.')        #self.running = False
                    self.running = False

                elif self.direction == 'left' and self.running == True:
                    self.x -= 1
                    self.item_check(self.file_content[self.y][self.x])
                    if dbg == True: print(self.file_content[self.y][self.x])

                elif self.direction == 'down' and self.running == True:
                    self.y += 1
                    self.item_check(self.file_content[self.y][self.x])
                    if dbg == True: print(self.file_content[self.y][self.x])

                elif self.direction == 'up' and self.running == True:
                    self.y -= 1
                    self.item_check(self.file_content[self.y][self.x])
                    if dbg == True: print(self.file_content[self.y][self.x])


                elif self.y == len(self.file_content):
                    self.throw_error('reached end of line. exiting.')        #self.running = False
                    self.running = False
                
                if dbg == True:
                    time.sleep(0.5)
                    print(self.stringmode)
                else:
                    time.sleep(0.05)



            except KeyboardInterrupt:
                self.throw_error('\n\nGot keyboard interrupt, exiting program...')

            else:
                pass


            #for row in range(len(self.file_content)):
            #    for item in self.file_content[row]:
            #        self.item_check(item)
            #    self.running = False


    def item_check(self, item):
        self.item = item
        if self.stringmode == False:
            if self.item == '>':
                self.direction = 'right'
                #print(self.direction, end=' ')

            elif self.item == 'v':
                self.direction = 'down'
                #print(self.direction, end=' ')

            elif self.item == '<':
                self.direction = 'left'
                # print(self.direction, end=' ')

            elif self.item == '^':
                self.direction = 'up'
                #print(self.direction, end=' ')

            elif self.item == '?':
                self.direction = random.choice(['up','down','left','right'])

            elif self.item == ' ':
                #print('next-char', end=' ')
                pass

            elif self.item == 'h':
                if self.stack_pop() == 0:
                    self.direction = 'right'
                else:
                    self.direction = 'left'

            elif self.item == ',':
                #sys.stdout.write(chr(self.stack_pop()))
                print(chr(self.stack_pop()), end='', flush=True)
                #print(self.stack)

            elif self.item == '.':
                print(self.stack_pop())

            elif self.item == '"':
                self.stringmode = True
        

        #elif self.item == ',n':
            #print(self.stack_pop(), end='')


        ### NUMBERS
        #I have to do it manually b/c idk how to automate it lol
            elif self.item == '0':
                #print(1, end=" ")
                self.stack_push(0)

            elif self.item == '1':
                #print(1, end=" ")
                self.stack_push(1)

            elif self.item == '2':
                #print(1, end=" ")
                self.stack_push(2)

            elif self.item == '3':
                #print(1, end=" ")
                self.stack_push(3)

            elif self.item == '4':
                #print(1, end=" ")
                self.stack_push(4)

            elif self.item == '5':
                #print(1, end=" ")
                self.stack_push(5)

            elif self.item == '6':
                #print(1, end=" ")
                self.stack_push(6)

            elif self.item == '7':
                #print(1, end=" ")
                self.stack_push(7)

            elif self.item == '8':
                #print(1, end=" ")
                self.stack_push(8)

            elif self.item == '9':
                #print(1, end=" ")
                self.stack_push(9)

            ## Math

            elif self.item == '+':
                a = self.stack_pop()
                b = self.stack_pop()
                self.stack_push(a+b)

            elif self.item == '-':
                a = self.stack_pop()
                b = self.stack_pop()
                self.stack_push(a-b)

            elif self.item == '*':
                a = self.stack_pop()
                b = self.stack_pop()
                self.stack_push(a*b)

            elif self.item == '/':
                a = self.stack_pop()
                b = self.stack_pop()
                self.stack_push(a/b)

            elif self.item == 'I':
                a = input()
                try:
                    self.stack_push(int(a))
                except ValueError:
                    try:
                        self.stack_push(ord(a))
                    except TypeError:
                        self.throw_error(f'sorry, only one character input, please. (error at {self.x}, {self.y})')

            elif self.item == '@':
                self.throw_error('exiting...')

            else:
                self.throw_error(f'ERROR! Unrecognised character! at char {self.x+1} and line {self.y+1}')
        else: 
            if self.item == '"':
                self.stringmode = False
            
            elif self.item == ' ':
                self.stack_push(ord(' '))
            else:
                self.stack_push(ord(self.item))

    def throw_error(self, error):
        print(error)
        quit()



    def file_to_source_code(self, file, debug=False):
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
            self.file_content.append(list(line))#.append('\n'))
            
        #print(self.file_content)

        if debug == True:
            self.start_run(debug=True)
        else:
            self.start_run()
        #print(self.file_content)

    def stack_push(self, value):
        self.stack.append(value)

    def stack_pop(self):
        return self.stack.pop()


if __name__ == '__main__':
    try:
        Symbolang(sys.argv[1], sys.argv[2])
    except IndexError:
        print('You have to specify a file to open!! and some arguments!!')
        quit()
    except ZeroDivisionError:
        print("lol don't divide by zero")
        quit()
