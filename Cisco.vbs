Set WshShell = WScript.CreateObject("WScript.Shell")

WshShell.Run """%PROGRAMFILES(x86)%\Cisco\Cisco AnyConnect Secure Mobility Client\vpnui.exe"""

WScript.Sleep 1500

WshShell.AppActivate "Cisco AnyConnect Secure Mobility Client"


WshShell.SendKeys "{ENTER}"

WScript.Sleep 10000

WshShell.SendKeys "MDLandJS20{!}5"
WshShell.SendKeys "{ENTER}"