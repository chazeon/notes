---
title: My PowerShell Profile
---

## Tab completion

Here is how to mimic bash and zsh’s tab autocompletion behavior.

```powershell
Set-PSReadlineKeyHandler -Key Tab -Function Complete
```

## Command prompt

I like oh-my-zsh’s [candy](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/candy.zsh-theme) theme. Here is how to recreate it in PowerShell in a very basic form.

```powershell
function Prompt {
    $Time = Get-Date -UFormat %H:%M:%S
    Write-Host "$env:USERNAME@$env:COMPUTERNAME " -ForegroundColor Green -NoNewline
    Write-Host "[$Time] " -ForegroundColor Blue -NoNewline
    Write-Host "[$pwd]"
    Write-Host "-> %" -ForegroundColor Blue -NoNewline
    return " "
}
```