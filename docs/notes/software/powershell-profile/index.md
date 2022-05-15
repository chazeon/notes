---
title: My PowerShell Profile
---

Moving from Zsh, which is easily configurable by [Oh My Zsh](https://ohmyz.sh/), the PowerShell on Windows always feels pitiably basic. PowerShell does not enjoy the privilege of Oh My Zsh, unfortunately. Although there is a [Oh My Posh](https://ohmyposh.dev/) project that claims to be inspired by Oh My Zsh, it is, in my mind, overly fancy.

In this note, we try to custom PowerShell with a very simple PowerShell profile. It will allow your PowerShell to mimic your favorite shell’s behavior, at least to some extent.

![After customization, my PowerShell have Oh My Zsh’s candy-like command prompt.](candy-like.png){width=480px, .rounded}

## PowerShell’s profile

The `.bashrc`’s equivalent in PowerShell is called *profile*, stored at `$PROFILE`. PowerShell will load this script upon startup.

To open this file with Notepad, open a PowerShell window and enter the following command:

```powershell
notepad.exe $PROFILE
```

If its parent folder does not exist, you might need to create the parent folder to be able to save this file. Edit, and save this file, and start a new PowerShell window, you will see the changes taking effect.

## PowerShell’s execution policy

If you have not changed the execution policy, the loading of your PowerShell’s profile might be blocked because of the execution policy. You can change it by

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
```

Please refer to PowerShell’s official document [Set-ExecutionPolicy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.2) for a more detailed description of this command.

## Command prompt

I like Oh My Zsh’s [candy](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/candy.zsh-theme) theme. Here is how to recreate this prompt in PowerShell in a very basic form.

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

## Tab completion

Here is how to mimic bash and zsh’s tab autocompletion behavior.

```powershell
Set-PSReadlineKeyHandler -Key Tab -Function Complete
```

## OpenSSH Server

Install the OpenSSH server by enable it in [Windows Settings's Optional Features](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse#install-openssh-using-windows-settings), then start and enable the service.

### Set Powershell as the login shell

According to [OpenSSH Server configuration for Windows](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_server_configuration):

```powershell
New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force
```

### Public-private key authorization

See [Setting up OpenSSH for Windows using public key authentication - Stack Overflow](https://stackoverflow.com/questions/16212816/setting-up-openssh-for-windows-using-public-key-authentication).

## Package manager & coreutils

For CLI tools, use [Scoop](https://scoop.sh/) (compared to [Chocolatey](https://chocolatey.org/), aka `choco`, Scoop is more focused on CLI tools).

Install `scoop` via the following command:

```powershell
Invoke-WebRequest get.scoop.sh | Invoke-Expression
```

Then install the coreutils, vim, etc.:

```powershell
scoop install coreutils vim # ...
```

