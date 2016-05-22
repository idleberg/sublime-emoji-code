# emoji-code

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/Emoji%20Code.svg?style=flat-square)](https://packagecontrol.io/packages/Emoji%20Code)
[![GitHub release](https://img.shields.io/github/release/idleberg/sublime-emoji-code.svg?style=flat-square)](https://github.com/idleberg/sublime-emoji-code/releases)
[![Travis](https://img.shields.io/travis/idleberg/sublime-emoji-code.svg?style=flat-square)](https://travis-ci.org/idleberg/sublime-emoji-code)
[![Gitter](https://img.shields.io/badge/chat-Gitter-ff69b4.svg?style=flat-square)](https://gitter.im/NSIS-Dev/SublimeText)

Sublime Text completions to insert escaped Emoji code into HTML, CSS, JavaScript and Ruby.

![Screenshot](https://raw.github.com/idleberg/sublime-emoji-code/master/screenshot.gif)

*Screenshot nicked from the [Atom package](https://atom.io/packages/emoji-code), sorry!*

## Usage

All emojis are prefixed with `ji`, following the string of the official [Unicode terminology](unicode.org/emoji/charts/full-emoji-list.html).

**Examples:**

Let's say, you want to insert the 😄 emoji

* HTML: `ji:grinning-face` becomes `&#x1F600;`
* CSS: `ji:grinning-face` becomes `content: '\1F600';`
* JavaScript: `ji:grinning-face` becomes `u\1F600`
* Ruby: `ji:grinning-face` becomes `\u{1F600}`

Keep in mind that Sublime Text supports fuzzy completion, inviting you to use abbreviation of your preference.

## Installation

### Package Control

1. Make sure you already have [Package Control](https://packagecontrol.io/) installed
2. Choose *“Install Package”* from the Command Palette (<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>)
3. Type *“Emoji Code”* and press <kbd>Enter</kbd>

With [auto_upgrade](http://wbond.net/sublime_packages/package_control/settings/) enabled, Package Control will keep all installed packages up-to-date!

There's also a collection of [Sublime Text Packages](https://github.com/NSIS-Dev/Sublime-Text-Packages) available as a Windows installer.

### GitHub

1. Change to your Sublime Text `Packages` directory
2. Clone repository `git clone https://github.com/idleberg/sublime-emoji-code.git 'Emoji Code'`

## Cheatsheet

 Take note of this list of [all supported emoji codes](cheatsheet.md).

## License

This work is licensed under the [The MIT License](LICENSE.md).

## Donate

You are welcome support this project using [Flattr](https://flattr.com/submit/auto?user_id=idleberg&url=https://github.com/idleberg/sublime-emoji-code) or Bitcoin `17CXJuPsmhuTzFV2k4RKYwpEHVjskJktRd`