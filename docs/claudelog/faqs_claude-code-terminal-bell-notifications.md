Skip to main content
Setting up audio notifications in Claude Code on Windows can be tricky, especially with WSL. This guide covers all the methods that actually work.
### Standard Configuration​
**Initial Setup** - Enable terminal bell notifications globally:
```
claude config set --global preferredNotifChannel terminal_bell
```

  * **No restart required** : Changes take effect immediately
  * **Test first** : Run `echo -e "\a"` to verify your terminal supports bell notifications
  * **Universal method** : Works across most terminal environments when properly configured


### Windows WSL Solutions​
**Problem** - The standard terminal bell often doesn't work in Windows WSL environments, leaving you without task completion notifications.
**PowerShell Method** - For Windows WSL users where `echo -e "\a"` fails:
  * **Default beep** : `powershell.exe -c "[System.Media.SystemSounds]::Beep.Play()"`
  * **Question sound** : `powershell.exe -c "[System.Media.SystemSounds]::Question.Play()"`
  * **Personal preference** : The Question sound provides better audible distinction


### Implementation Steps​
**Step 1: Test Your System**
```
echo -e "\a"
```

**Step 2: If No Sound** - Test PowerShell alternative:
```
powershell.exe -c "[System.Media.SystemSounds]::Beep.Play()"
```

**Step 3: Configure Claude.md** - Add notification instructions to your CLAUDE.md:
```
## NotificationsWhen tasks complete, notify me using:powershell.exe -c "[System.Media.SystemSounds]::Question.Play()"
```

### Troubleshooting Tips​
**No Sound at All**
  * Verify system volume is enabled
  * Test PowerShell commands directly in terminal
  * Check if your terminal application supports bell notifications


**WSL-Specific Issues**
  * Standard Linux bell commands often fail in WSL
  * PowerShell integration is the most reliable solution
  * Windows system sounds work better than terminal bells


### Why This Matters​
**Productivity Boost** - Audio notifications free you from constantly checking if Claude has completed tasks or needs attention.
**Focus Management** - Work on other tasks while Claude Code handles background operations, knowing you'll be alerted when intervention is needed.
**Workflow Integration** - Proper notifications enable true multitasking with Claude Code as your development partner.
##### Notification Workflow Enhancement
PowerShell system sounds provide reliable notifications when standard terminal bells fail in WSL. Proper notifications enable true multitasking with Claude Code as your development partner.
![Custom image](https://www.claudelog.com/img/discovery/025.png)
**See Also** : Configuration|Windows Installation|CLAUDE.md Supremacy
  * Standard Configuration
  * Windows WSL Solutions
  * Implementation Steps
  * Troubleshooting Tips
  * Why This Matters


