---
title: code-server over SSH
date: 2022-05-10
---

Visual Studio Code (VSCode) Remote SSH is good, but the instability in establishing the connection due to the communication issue between the local app and remote sidecar program is sometimes a very bad headache.

Recently, I switched to **[code-server](https://github.com/coder/code-server)**, which is an in-browser version of the VSCode. All the program logic runs on the remote server and is only rendered in browser locally, there reduces the complexity.

Similar to the VSCode experience, it not only gives you a editor, but also offers a terminal that allows you to run shell programs. Reading / writing large files without having to transmitting the whole file at first makes it significantly snappier (compared to VSCode with Remote SSH, where if you accidentally click a large binary file, it just get stuck).

## Usage

### Installation

Follow the code-server's [official instruction](https://coder.com/docs/code-server/latest/install), but with `--method standalone` which install the program within the local user's home directory:

```bash
curl -fsSL https://code-server.dev/install.sh | sh -s -- --method standalone
```

### Starting the server with port-forwarding

To start the server, execute the following command from your local shell (replace the login, host, port and password):

```bash
ssh user@example.com \
	-L xxxx:localhost:xxxx 'PORT=xxxx PASSWORD=xxxx code-server'
```

Now the code-server should be up and running on the HPC and avaliable from your browswer at `http://localhost:xxxx`.

### Install the webpage as an app (optional)

Many morden browsers allows you to install a webpage as an app. This gives you the benefit of saving the screen real estate of the tabbar and location bar, and additionally add an icon in your dock (on MacOS). If you are using Microsoft Edge like I do, follow the instruction from "[Install, manage, or uninstall apps in Microsoft Edge](https://support.microsoft.com/en-us/topic/install-manage-or-uninstall-apps-in-microsoft-edge-0c156575-a94a-45e4-a54f-3a84846f6113)".

## Known issues

- Coder's `code-server` does not share [VSCode's Marketplace](https://coder.com/docs/code-server/latest/FAQ#why-cant-code-server-use-microsofts-extension-marketplace) officially. Although you could bring your own VSIX and manually install them.

## Microsoft's `code-server`

Microsoft has recently release [their own version of the `code-server`](https://code.visualstudio.com/docs/remote/vscode-server). What's great is that it works on Windows, which Coder's version does not support. After installation, it can be started from the following command:

```
code-server serve-local -p xxxx --without-connection-token
```

But remember you will need to agree to ToS the first time you start it.
