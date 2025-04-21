import sys, random, time, argparse

class Symbolang:
    def __init__(self, arg1, source=None):
        self.y = 0
        self.x = 0
        self.direction='right'
        self.stack = []
        self.stringmode = False



        self.running = False
        if arg1:
            if source:
                self.file_to_source_code(source, arg1)
        else:
            if source:
                self.file_to_source_code(source)

    def start_run(self, debug=False):
        if debug == True:
            self.run_prgm(True)
        else:
            self.run_prgm(False)


    def run_prgm(self, dbg):
        self.item_check(self.file_content[self.y][self.x])
        self.running = True
        while self.running != False:
            try:


                if self.direction == 'right' and self.running == True:
                    self.x += 1
                    self.item_check(self.file_content[self.y][self.x])
                    if dbg == True: print(self.file_content[self.y][self.x]), print(self.stack)                    


                elif self.x >= len(self.file_content[self.y]):
                    self.throw_error('reached end of line. exiting.')
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
                    self.throw_error('reached end of line. exiting.')
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

    def item_check(self, item):
        self.item = item
        if self.stringmode == False:
            if self.item == '>':
                self.direction = 'right'

            elif self.item == 'v':
                self.direction = 'down'

            elif self.item == '<':
                self.direction = 'left'

            elif self.item == '^':
                self.direction = 'up'

            elif self.item == '?':
                self.direction = random.choice(['up','down','left','right'])

            elif self.item == ' ':
                pass

            elif self.item == 'h':
                if self.stack_pop() == 0:
                    self.direction = 'right'
                else:
                    self.direction = 'left'

            elif self.item == ',':
                print(chr(self.stack_pop()), end='', flush=True)

            elif self.item == '.':
                print(self.stack_pop())

            elif self.item == '"':
                self.stringmode = True
        
        ###############
        ### NUMBERS
        # I have to do it manually b/c idk how to automate it lol ;)
        ##############

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
            
            ###########
            ## Math
            ###########

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

            elif list(self.source.split('.'))[1] ==  'symb':
                self.file = open(self.source, 'r')

        except IndexError:
            self.throw_error('no file extension')
        self.file_content = []
        self.line_content = []

        for line in self.file:
            self.file_content.append(list(line))
            

        if debug == True:
            self.start_run(debug=True)
        else:
            self.start_run()

    def stack_push(self, value):
        self.stack.append(value)

    def stack_pop(self):
        return self.stack.pop()



def run(a):
    try:
        print("does this work?")
        Symbolang(a.debug, a.filename)
    except IndexError:
        print('You have to specify a file to open!! and some arguments!!')
        quit()
    except ZeroDivisionError:
        print("lol don't divide by zero")
        quit()

if __name__ == '__main__':
    run()
