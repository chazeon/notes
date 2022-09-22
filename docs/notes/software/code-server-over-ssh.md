---
title: code-server over SSH
date: 2022-05-10
---

Visual Studio Code (VSCode) Remote SSH is good, but the instability in establishing the connection due to the communication issue between the local app and the remote sidecar program is sometimes a very bad headache.

Recently, I switched to **[code-server](https://github.com/coder/code-server)**, which is an in-browser version of the VSCode. All the program logic runs on the remote server and is only rendered in the browser locally, there reduces the complexity.

Similar to the VSCode experience, it not only gives you an editor but also offers a terminal that allows you to run shell programs. Reading / writing large files without having to transmit the whole file at first makes it significantly snappier (compared to VSCode with Remote SSH, where if you accidentally click a large binary file, it just gets stuck).

## Usage

### Installation and update

Follow the code-server's [official instruction](https://coder.com/docs/code-server/latest/install), but with `--method standalone` to install `code-server` without root access. It installs the program within the local user's home directory:

```bash
curl -fsSL https://code-server.dev/install.sh | sh -s -- --method standalone
```

The installer will decompress the files to ` ~/.local/lib/code-server-4.x.x` and create a link from `~/.local/bin/code-server` to `~/.local/lib/code-server-4.x.x/bin/code-server`.

### Starting the server with port-forwarding

To start the server, execute the following command from your local shell (replace the login, host, port, and password):

```bash
ssh user@example.com \
	-L xxxx:localhost:xxxx 'PORT=xxxx PASSWORD=xxxx code-server'
```

Now the code-server should be up and running on the HPC and available from your browswer at `http://localhost:xxxx`.

### Install the webpage as an app (optional)

Many modern browsers allow you to install a webpage as an app. This gives you the benefit of saving the screen real estate of the tabbar and location bar, and additionally adds an icon in your dock (on MacOS). If you are using Microsoft Edge as I do, follow the instruction from "[Install, manage, or uninstall apps in Microsoft Edge](https://support.microsoft.com/en-us/topic/install-manage-or-uninstall-apps-in-microsoft-edge-0c156575-a94a-45e4-a54f-3a84846f6113)".

## Additional Notes

### Serving `code-server` from Windows

Coder's `code-server` does not come with a prebuilt windows binary, and you will need to build it yourself. Follow Coder's instructions for [building code-server with npm on Windows](https://coder.com/docs/code-server/latest/npm#windows). Basically, you will need to:

- Install Node 16 via whatever method, (one way is `scoop`→`nvm`).
- Install the [Visual Studio Build Tools](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools) or the [Visual Studio Community Edition](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community) with  "Desktop Development with C++" plugin due to [VSCode's build requirement](https://github.com/Microsoft/vscode/wiki/How-to-Contribute#prerequisites).
- Install `yarn`
- Add `yarn global bin` location to systems' environment variable `PATH`
- Then build, install and run with `yarn`
  ```powershell
  yarn global add code-server
  code-server
  ```

And I use [WinSW](https://github.com/winsw/winsw) to run it as a Windows service.

### Access `code-server` instance from iPadOS

[Ultimate Code Wrapper](https://apps.apple.com/us/app/ucow-ultimate-code-wrapper/id1551344923) (UCoW) provides a better experience for using `code-server` on iPadOS since it has better support for the virtual keyboard on iPadOS.

### Microsoft's `code-server`

Microsoft has recently released [its own version of the `code-server`](https://code.visualstudio.com/docs/remote/vscode-server). What's great is that it works on Windows, which Coder's version does not support. After installation, it can be started from the following command:

```bash
code-server --accept-server-license-terms \
	serve-local --without-connection-token -p xxxx 
```

My experience is that its stability on Windows is very poor. The "extension host" quits often and brings down the whole service after a timeout. I tried it, then soon had to switch to Coder's `code-server` even though I had to build it myself. Not sure if the same problem exists on Linux targets.

## Known issues

- Coder's `code-server` does not share [VSCode's Marketplace](https://coder.com/docs/code-server/latest/FAQ#why-cant-code-server-use-microsofts-extension-marketplace) officially. Although you could bring your own VSIX and manually install them.

