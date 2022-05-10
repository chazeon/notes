---
title: code-server over SSH
date: 2022-05-10
---

Visual Studio Code (VSCode) is good, but the instability due to the network connection is sometimes a very bad headache. Recently, I switched to **[code-server](https://github.com/coder/code-server)**, which is an in-browser version of the VSCode.

### Installation

Follow the code-server's [official instruction](https://coder.com/docs/code-server/latest/install):

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