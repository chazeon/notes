---
title: Fix Zsh's missing compinit
---

On HPCs (e.g., TACC's Stampede2, Purdue's Anvil), the prompt is usually broken, and you are notified of the missing `compinit`. For example,

```
/home/user/.oh-my-zsh/oh-my-zsh.sh:124: compinit: function definition file not found
```

This is likely because Zsh's function lookup path `fpath`, [collides with a predefined `FPATH` in `Lmod`](https://github.com/TACC/Lmod/issues/555).

This can be fixed by manually setting the `fpath` in `.zshrc`. For example:

```zsh
fpath=(
  /usr/share/zsh/5.5.1/functions
  /usr/share/zsh-completions
  /usr/share/zsh/site-functions
)
```

## References

- [FPATH gets carried to ZSH when using bash, even when SUPPORT_KSH is set to "no" · Issue #555 · TACC/Lmod (github.com)](https://github.com/TACC/Lmod/issues/555)
- [zsh-completions require compinit in the .zshrc file? · Issue #277 · zsh-users/zsh-completions (github.com)](https://github.com/zsh-users/zsh-completions/issues/277)