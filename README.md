Pygments Github Custom Lexers
=============================
[![Build Status](https://travis-ci.org/liluo/mime.png)](https://travis-ci.org/liluo/pygments_github_lexers)

This entrypoint is used for adding [Github Custom Lexers](https://github.com/tmm1/pygments.rb/blob/master/vendor/custom_lexers/github.py) to the [Pygments](http://pygments.org/) core. 

### Install

```bash
pip install pygments-github-lexers
```

### Usage Sample

```
from pygments import lexers

lexers.find_lexer_class('dasm16')
lexers.find_lexer_class('Puppet')
lexers.find_lexer_class('Augeas')
lexers.find_lexer_class('TOML')
lexers.find_lexer_class('Slash')
```

### Changelog
__v0.0.2 [2013-11-07]__
* Fix version number 

__v0.0.1 [2013-08-20]__
* Release.

### Thanks

This package is based upon the [Github Custom Lexers](https://github.com/tmm1/pygments.rb/blob/master/vendor/custom_lexers/github.py) of [pygments.rb](https://github.com/tmm1/pygments.rb).
