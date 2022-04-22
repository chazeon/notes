---
title: Fix ZSH missing compinit
---

On HPCs (e.g., TACC Stampede, Purdue Anvil), when using Zsh as the shell, you usually get the error that `compinit` is missing. For example,

```
/home/user/.oh-my-zsh/oh-my-zsh.sh:124: compinit: function definition file not found
```

This is likely because Zsh's function lookup path `fpath`, collides a predefined `FPATH`.

This can be fixed by manually setting the `fpath` in `.zshrc`. For example:

```zsh
fpath=(
  /usr/share/zsh/5.5.1/functions
  /usr/share/zsh-completions
  /usr/share/zsh/site-functions
)
```

## References

- [zsh-completions require compinit in the .zshrc file? · Issue #277 · zsh-users/zsh-completions (github.com)](https://github.com/zsh-users/zsh-completions/issues/277)

- [FPATH gets carried to ZSH when using bash, even when SUPPORT_KSH is set to "no" - githubhot](https://githubhot.com/repo/TACC/Lmod/issues/555)