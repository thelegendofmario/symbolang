# Symbolang
### a 2-dimensional, interpreted, programming language, inspired by [befunge](https://esolangs.org/wiki/Befunge)
## intro

The main concept of a Symbolang program is a 'pointer'. the pointer is the
imaginary cursor that executes each character one by one. (right now it
just supports left and right direction for the pointer, but eventually,
it will be able to move up and down too.)

## Variable scope

This is a stack based language, (at least for now)

There aren't really any variables, but you are able to push and pop values to and from the stack.

## Syntax
| Symbol | Function |
|----------------|------------------------------------------|
| >              | Makes the pointer start moving left |
| <              | Makes the pointer start moving right |
| ^              | Makes the pointer start moving up |
| v              | Makes the pointer start moving down |
| ?              | Random pointer direction |
| p              | go to the next character |
| ,              | pops value from stack and prints ascii character corresponding to that value.     |
| .              | pops value from stack and prints it. |
| 1-9            | pushes corresponding value to stack. |
| /, *, +, or -  | pop two values from stack (a, then b), and then performs the operation on a and b and pushes result to stack.|
| I              | (CAPITAL I) gets a number or character from user, and pushes it to the stack.                                |



Table of functions

## Use
simply clone the repo, `git clone https://github.com/thelegendofmario/symbolang.git`,
then, place your `.symb` file into the directory, and in your terminal, type
`python3 symbolang.py [argument] [your-file-here]`.

### Arguments
available arguments right now are `--run` or `--debug`.
`--debug` runs the program but prints everything under the pointer,
while `--run` just prints the output of the program.

## Changelog
* Made a debug mode :) first real version of Symbolang, I feel like.

## Roadmap
* At some point, it would be AMAZING if this had an interpreter in a compiled
language (instead of being interpreted to be interpreted).
* ~~up and down movement of cursor~~ <- completed
* interactive REPL would be awesome
* a [tulip](https://tulip.computer) port
