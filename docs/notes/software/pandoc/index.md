---
title: Convert LaTeX to docx using Pandoc
---

## Challenges and solutions

### Format

Prepare a [reference `.docx` file](https://pandoc.org/MANUAL.html#option--reference-doc) and apply the format using the `--reference-doc` command. This can be done by creating a without reference first; tuning the format; then reproducing the `.docx` file.

### Citation references

See relevant sections in [Pandoc User’s Guide](https://pandoc.org/MANUAL.html#citation-rendering). Reference styles are available to download from [Zotero Style Repository](https://www.zotero.org/styles). 

- `--citeproc`
- `--bibliography=xxx.bib`
- `--csl=xxx.csl`

### Cross references

Pandoc does convert the section reference to section numbers, but it does not correctly convert references for tables and figures.

Inspired by the [`xr` package](https://mirrors.rit.edu/CTAN/macros/latex/required/tools/xr.pdf), when the `hyperref` package `.aux` file, the definition starts with `\newlabel`. The regex expression for parsing the `\newlabel` lines are:

```
^\\newlabel{(.+)}{{(.+)}{(.*)}{(.*)}{(.*)}{(.*)}}$
```

Here is an example filter in Python:

```python
#!/usr/bin/env python

import re
from pandocfilters import toJSONFilter
from functools import lru_cache

REF_REGEX = re.compile(r'^\\newlabel{(.+)}{{(.+)}{(.*)}{(.*)}{(.*)}{(.*)}}$')

@lru_cache
def load_aux(fname: str):
    refs = {}
    with open(fname) as fp:
        for line in fp:
            res = REF_REGEX.search(line)
            if res:
                refs[res.group(1)] = res.group(2)
    return refs

def resolveRef(key, value, format, meta):

    refs = load_aux('main.aux')

    if key == "Link":
        try:
            res = re.search(r'^\[(.*)\]$', value[1][0]['c'])
            if res:
                value[1][0]['c'] = refs[res.group(1)]
        except Exception as e:
            pass

if __name__ == "__main__":
    toJSONFilter(resolveRef)
```



### Undefined math command

Some math commands, such as `\tiny`, `\large`, `\text` (from `amsmath`), are not supported by Pandoc. One can also use [filters](https://pandoc.org/filters.html) to strip them away or replace them with alternatives if necessary.

Here is an example filter in Python:

```python
#!/usr/bin/env python

from pandocfilters import toJSONFilter

def replaceCommands(key, value, format, meta):
    if key == "Math":
        for i in range(len(value)):
            if isinstance(value[i], str):
                value[i] = value[i].replace(r"\tiny", "")
                value[i] = value[i].replace(r"\large", "")
                value[i] = value[i].replace(r"\text", "\mathrm")

if __name__ == "__main__":
    toJSONFilter(replaceCommands)
```

## Final command

To put them together, the final command would be:

```bash
pandoc main.tex \
  --citeproc \
  --bibliography=xxx.bib \
  --csl=physical-review-b.csl \
  --reference-doc=main-ref.docx \
  --filter fix-texmath.py \
  --filter resolve-ref.py \
  -t docx -o main-$(date +%Y%m%d%H%M).docx
```



## References

- [jgm/pandocfilters: A python module for writing pandoc filters, with a collection of examples](https://github.com/jgm/pandocfilters)
- [Pandoc - Pandoc User’s Guide](https://pandoc.org/MANUAL.html#citation-rendering)
- [Pandoc - Pandoc filters](https://pandoc.org/filters.html)
- [The xr package - xr.pdf](https://mirrors.rit.edu/CTAN/macros/latex/required/tools/xr.pdf)
- [Zotero Style Repository](https://www.zotero.org/styles)