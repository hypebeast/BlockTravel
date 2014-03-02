# BlockTravel

BlockTravel is a Sublime Text 3 plugin that adds commands to move your cursor
back and forward to the next block or select a block of text. It uses empty lines
to find blocks.

It's inspired by [Block Travel](https://github.com/leejarvis/block-travel) for [Atom](https://atom.io).

![screenshot BlockTravel](http://sebastianruml.com/downloads/projects/block_travel/block_travel.gif)

## Installation

 * recommended is to use [Sublime Package
   Manager](http://wbond.net/sublime_packages/package_control#Features)
 * press `Ctrl+Shift+P` then `Package Control: Install Package`
 * look for `BlockTravel` and install it.


## Usage

The LineJumper package adds four new commands to Sublime Text with the following default keybindings:

 * `ctrl-up` to move the cursor up to the next empty line
 * `ctrl-down` to move the cursor down to the next empty line
 * `ctrl-shift-up` to select up to the next empty line
 * `ctrl-shift-down` to select down to the next empty line

These commands are also available through the Command Palette. Press `Ctrl+Shift+P`
and then select from one of the following commands:

 * `BlockTravel: Move up lines`
 * `BlockTravel: Move down lines`
 * `BlockTravel: Select up lines`
 * `BlockTravel: Select down lines`


## Configuration

You can change the keybindings:

 * press `Ctrl+Shift+P` then `Preferences: BlockJumper Key Bindings – User`
 * and add a line like this:
   `{ "keys": ["ctrl+down"], "command": "block_travel", "args": { "cmd": "down" } },`
 * open the default keybindings `Preferences: BlockJumper Key Bindings – Default` to see all available commands


## License

Copyright (c) 2014 Sebastian Ruml <sebastian.ruml@gmail.com>

Released under The MIT License.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

