# Symbolang
### a 2-dimensional, interpreted, programming language, inspired by [befunge](https://esolangs.org/wiki/Befunge)
## intro

The main concept of a Symbolang program is a 'pointer'. the pointer is the
imaginary cursor that executes each character one by one. (right now it
just supports left and right direction for the pointer, but eventually,
it will be able to move up and down too.)

## Variable scope

This (will be) a stack based language, (at least for now)

There aren't really any variables, but you are able to push and pop values to and from the stack.

## Syntax
| Symbol | Function |
|---|--------------------------------------------|
| >              | Makes the pointer start moving left      |
| <              | Makes the pointer start moving right     |
| ^              | Makes the pointer start moving up        |
| v              | Makes the pointer start moving down      |
| .              | go to the next character                 |
| ,              | pops value from stack and prints it.     |
| 1-9            | pushes corresponding value to stack      |
| /, *, +, or -  | pop two values from stack (a, then b), and then performs the operation on a and b and pushes result to stack.|
| I              | (CAPITAL I) gets a number or character from user, and pushes it to the stack.                                |

Table of functions
## Roadmap
* At some point, it would be AMAZING if this had an t=interpreter in a compiled
language (instead of being interpreted to be interpreted).
* ~~up and down movement of cursor~~ <- completed
* interactive REPL would be awesome
* a [tulip](https://tulip.computer) port
