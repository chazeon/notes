---
title: VASP Tips
---

Here are some tips I get from my past experience with VASP. I don't know where to put them so they are here.

1. Use [`LREAL = Auto`](https://www.vasp.at/wiki/index.php/LREAL) for large supercells simulations, I was once warned by VASP:

  > You have a (more or less) 'large supercell' and for larger cells it might be more efficient to use real-space projection operators. Therefore, try `LREAL= Auto` in the INCAR file. Mind: For very accurate calculation, you might also keep the reciprocal projection scheme (i.e. LREAL=.FALSE.). 

2. `POTCAR` is matched to `POSCAR` by ordering, not by atom name. So be careful with the ordering of atoms.
