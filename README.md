# Symbolang
## intro
this is a 2-dimensional, interpreted, programming language, inspired by [befunge](https://esolangs.org/wiki/Befunge).

The main concept of a Symbolang program is a 'pointer'. the pointer is the
imaginary cursor that executes each character one by one. (right now it
just supports left and right direction for the pointer, but eventually,
it will be able to move up and down too.)
## Syntax
| Symbol | Function |
|---|--------------------------------------------|
| > | Makes the 'pointer' start moving left      |
| < | Makes the 'pointer' start moving right     |
| . | skip, go to the next one                   |
| 1 | Right now, this just prints the number '1' |

## Roadmap
* At some point, it would be AMAZING if this was eventually a
compiled language, but as of right now, it will not be compiled.
  * (or an interpreter written in a more portable
  language, instead of being interpreted to be interpreted.)
* up and down movement of cursor
* interactive REPL would be awesome
* a [tulip](https://tulip.computer) port
