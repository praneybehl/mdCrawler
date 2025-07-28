Skip to main content
Claude Code notifications alert you when tasks complete, preventing the need to constantly monitor progress. Set up terminal bell notifications or system sound alternatives for hands-off workflow management.
### How to Use It​
Enable terminal bell notifications globally with the configuration command, then test your system's bell functionality. For Windows WSL environments where standard bells don't work, configure PowerShell system sounds as alternatives.
### Why Use It​
Notifications free me from monitoring Claude Code continuously, allowing multitasking while staying informed about task completion. I use them to maintain focus on other work while Claude handles background operations.
**Benefits:**
  * **Multitasking Freedom** - Work on other tasks while Claude Code runs operations
  * **Immediate Awareness** - Know instantly when Claude completes tasks or needs input
  * **Focus Management** - Avoid constant terminal checking and maintain concentration


I enable notifications because they transform Claude Code from a tool requiring constant attention into a true development partner that works independently and alerts me when needed.
Standard Configuration
Enable terminal bell notifications globally: `claude config set --global preferredNotifChannel terminal_bell`. Test with `echo -e "\a"` to verify your terminal supports bell notifications.
Windows WSL Solution
For Windows WSL environments where standard bells fail, add instructions to your CLAUDE.md telling Claude to execute `powershell.exe -c "[System.Media.SystemSounds]::Question.Play()"` when tasks complete. This provides better audible alerts than the default beep.
##### Hands-Off Development Partner
Notifications transform Claude Code from requiring constant attention into independent operation. PowerShell system sounds provide reliable alternatives when terminal bells fail in Windows WSL.
![Custom image](https://www.claudelog.com/img/discovery/008.png)
**See Also** : Terminal Bell Notifications|Configuration Guide|Windows Installation
  * How to Use It
  * Why Use It


