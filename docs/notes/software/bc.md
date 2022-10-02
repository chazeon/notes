---
title: "bc: the scientific calculator"
---

`bc` is an command-line scientific calculator. It is shipped with most unix-like systems.

## Important variables

### `scale`

Due to `bc` behaves like arbitrary-precision calculator, the precision must be set. `scale` is the special variable that controls the precision, its default value is `0`. The command `scale=4` to set it to `4` and `scale` output the current setting.

## Comparisons

`dc` is predesssor to `bc` is succesor to , but it uses a Polish (prefix) notation. `bc` used to be built on top of `dc` but it was later rewritten and became independent.

`hoc` can be consider as a succsor to `bc` that developed as a part of the Plan 9 project. From a calculation perspective, `hoc` is like `bc` but it  is more convenient than `bc` because behaves more like a modern programming language (e.g., use `1.2E5` instead of `1.2*10^5` for scientific representation of $1.2\times10^5$); but it is unfortunately usually not built into unix-like distributions and are less accessible.

## Installations

In Windows, `bc` comes with `scoop` package [`unxutils`](https://sourceforge.net/projects/unxutils/).

## Additional notes

Lorinda Cherry, a female developer who worked with Robert Morris to develop `bc` in Bell labs, passed away in Feb. 2022.

## See also

- [X-Bc - a GUI to bc, a scientific calculator](https://x-bc.sourceforge.net/index.html)
- [bc Command Manual](https://www.gnu.org/software/bc/manual/html_mono/bc.html)