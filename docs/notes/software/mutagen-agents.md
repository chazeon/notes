---
title: Mutagen agent manual setup
---

[Mutagen](https://mutagen.io/) is a useful tool for remote development since it provide very fast file sync. But sometimes it fails to install its agent due to platform complexity. Don't just stop there, you can actually set it up manually on your own. Here is how to do that.

If you have successfully installed Mutagen on your local computer, the precompiled agents exists at `0.xx.x/libexec/mutagen-agents.tar.gz`. For example, on macOS, if Mutagen is installed through Homebrew, then  will be located at:


```bash
tar -xvf $HOMEBREW_CELLAR/mutagen/0.15.0/libexec/mutagen-agents.tar.gz
```

You need to copy the executable for your platform to your remote machine so that executing `.mutagen/agents/0.15.0/mutagen-agent -h` works. This means:

- For Windows, you need to give it an `.exe` extension, and move it to `.mutagen/agents/0.15.0/mutagen-agent.exe`.
- For Unix-like platform, you will need to give it executable permission using `chmod`.

After a "successful" installation, the command `.mutagen/agents/0.15.0/mutagen-agent -h`  should give you the following prompt after you login through SSH:


```
-> % .mutagen/agents/0.15.0/mutagen-agent -h
The Mutagen agent should not be invoked by human beings

Usage:
  mutagen-agent [flags]
  mutagen-agent [command]

Available Commands:
  install      Perform agent installation
  synchronizer Run the agent in synchronizer mode
  forwarder    Run the agent in forwarder mode
  version      Show version information
  legal        Show legal information
  help         Help about any command
  completion   Generate the autocompletion script for the specified shell

Flags:
  -h, --help      Show help information
  -v, --version   version for mutagen-agent

Use "mutagen-agent [command] --help" for more information about a command.
```

Then retry `mutagen sync create`, it likely will be working now.
