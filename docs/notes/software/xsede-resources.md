---
title: XSEDE Resources List
---

| Name                                                         | Host                               | Check usage                                                  |
| ------------------------------------------------------------ | ---------------------------------- | ------------------------------------------------------------ |
| XSEDE SSO                                                    | `login.xsede.org`                  |                                                              |
| [PSC Bridges-2](https://www.psc.edu/resources/bridges-2/user-guide-2-2/) | `br014.bridges2.psc.edu`           | [`projects`](https://www.psc.edu/resources/bridges-2/user-guide-2-2/#monitor-your-usage), `my_quotas` |
| [TACC-Stampede2](https://portal.tacc.utexas.edu/user-guides/stampede2) | `login1.stampede2.tacc.utexas.edu` |                                                              |
| [Anvil-GPU](https://www.rcac.purdue.edu/knowledge/anvil)     | `login02.anvil.rcac.purdue.edu`    | [`mybalance`](https://www.rcac.purdue.edu/knowledge/anvil/access/usage), `myquota` |
| [SDSC Expanse](https://www.sdsc.edu/support/user_guides/expanse.html) | `login01.expanse.sdsc.edu`         | `expanse-client` (from `sdsc` module)                        |
| [NCSA Delta](https://wiki.ncsa.illinois.edu/display/DSC/Delta+User+Guide) | `dt-login01.delta.ncsa.illinois.edu`         | `accounts`                        |

- For a list of login names see [XSEDE User Portal | Accounts](https://portal.xsede.org/group/xup/accounts).
- Using SSH Public-Private Key Pairs on PSC Computers needs to be manually [submitted and verified](https://www.psc.edu/types-of-ssh-authentication/).
- Expanse: to avoid `numpy` from conda getting stuck on login node, use `export OMP_NUM_THREADS=1`. 
- See allocation usage on [ACCESS Allocations](https://allocations.access-ci.org/allocations/summary).
- NCSA Delta does not allow login with ssh key pairs for general use.
