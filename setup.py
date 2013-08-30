#!/usr/bin/python

from setuptools import setup
from pygments_github_lexers import VERSION


setup(name='pygments-github-lexers',
      version=VERSION,
      description='Pygments Github custom lexers.',
      keywords='pygments github lexer',
      license='BSD',

      author='Liluo',
      author_email='i@liluo.org',

      url='https://github.com/liluo/pygments-github-lexers',

      packages=['pygments_github_lexers'],
      install_requires=['pygments>=1.6'],

      entry_points='''[pygments.lexers]
                      Dasm16Lexer=pygments_github_lexers:Dasm16Lexer
                      PuppetLexer=pygments_github_lexers:PuppetLexer
                      AugeasLexer=pygments_github_lexers:AugeasLexer
                      TOMLLexer=pygments_github_lexers:TOMLLexer
                      SlashLexer=pygments_github_lexers:SlashLexer''',

      classifiers=[
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
