#!/usr/bin/env python
"""
 " Copyright (c) 2012 Fabien Cazenave, Mozilla.
 "
 " Permission is hereby granted, free of charge, to any person obtaining a copy
 " of this software and associated documentation files (the "Software"), to
 " deal in the Software without restriction, including without limitation the
 " rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 " sell copies of the Software, and to permit persons to whom the Software is
 " furnished to do so, subject to the following conditions:
 "
 " The above copyright notice and this permission notice shall be included in
 " all copies or substantial portions of the Software.
 "
 " THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 " IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 " FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 " AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 " LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 " FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 " IN THE SOFTWARE.
"""

import re
import os
import sys

gSupportedLocales = ['ar', 'ca', 'de', 'el', 'es', 'fr', 'it', 'nb-NO', 'pt-BR', 'ru', 'tr', 'zh-TW']
gDefaultLocale = 'en-US'

def loadDictionary(dictPath):
  l10nDict = {}
  lines = open(dictPath, 'r').readlines()

  for line in lines:
    tmp = re.split('\s*=\s*', line)
    if len(tmp) > 1:
      key = tmp[0]
      value = tmp[1]
      l10nDict[key] = value

  return l10nDict

# check app l10n resources
def normalize(localeDir, appName):
  defaultPath = os.path.join(localeDir, appName + '.en-US.properties')

  for lang in gSupportedLocales:
    l10nPath = os.path.join(localeDir, appName + '.' + lang + '.properties')

    if os.path.exists(l10nPath):
      l10nDict = loadDictionary(l10nPath)
      dest = open(l10nPath, 'wb')
      default = open(defaultPath, 'r')

      lines = default.readlines()
      for line in lines:
        m = re.match('^([^#\s]+)(\s*=\s*)(.+)$', line)
        if m:
          key = m.group(1)
          value = m.group(3)
          if key in l10nDict:
            value = l10nDict[key]
          else:
            key = '#TODO: ' + key
            value = value + '\n'
          dest.write(key + m.group(2) + value)
        else:
          dest.write(line)

      dest.close()
      default.close()

# main
def main():
  if not len(sys.argv) == 2:
    print('Usage: ' + sys.argv[0] + ' [applicationDirectory]')
    exit()
  baseDir = os.path.realpath(os.path.dirname(sys.argv[0]))
  appName = sys.argv[1]
  localeDir = os.path.join(baseDir, 'apps', appName, 'locales')
  print(localeDir)
  normalize(localeDir, appName)

# startup
if __name__ == "__main__":
  main()

