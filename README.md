# Symbolang
### a 2-dimensional, interpreted, programming language, inspired by [befunge](https://esolangs.org/wiki/Befunge)

## intro

The main concept of a Symbolang program is the 'pointer'. the pointer is the
imaginary cursor that executes each character one by one.

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
| h              | horizontal if statement; pops value from stack, if value is 0, set direction to right, if it's anything else set it to left. |
| "              | toggles stringmode. if on, every character's ascii value will be pushed to the stack. |
|                | (single space) go to the next character |
| ,              | pops value from stack and prints ascii character corresponding to that value.     |
| .              | pops value from stack and prints it. |
| 1-9            | pushes corresponding value to stack. |
| /, *, +, or -  | pop two values from stack (a, then b), and then performs the operation on a and b and pushes result to stack.|
| I              | (CAPITAL I) gets a number or character from user, and pushes it to the stack.                                |

### Example Program
```
>" !dlroW ,olleH"v
^ ,,,,,,,,,,,,,, <
```

Table of functions

## Use
simply clone the repo, `git clone https://github.com/thelegendofmario/symbolang.git`,
then, place your `.symb` file into the directory, and in your terminal, type
`symbolang [argument] [your-file-here]`.

### Arguments
if you run it with `--debug`, it will print debug info. docs on what it displays coming soon!

## Changelog
* v0.1.0
    * Made a debug mode. I feel like this is the first real version
* v0.1.2
    * HUGE quality of life upgrade :)
    * programs usually looked like this: `> 0 . 0 <`, but now they look like this: `>0.0<`
* v0.1.3
    * now this can be run as an actual CLI app.

## Roadmap
* At some point, it would be AMAZING if this had an interpreter in a compiled
language (instead of being interpreted to be interpreted).
* ~~up and down movement of cursor~~ <- completed
* interactive REPL would be awesome
* a [tulip](https://tulip.computer) port
