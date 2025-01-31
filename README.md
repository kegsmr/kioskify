# Kioskify
A Python script frozen with PyInstaller that enables any Windows executable to be used as a "Kiosk" app in-place of the Windows shell.

## Usage
* Install the necessary requirements on PIP.
```
pip install -r requirements.text
```
* Run `setup.py` to freeze the Python script into a Windows executable with PyInstaller.
* Copy the Kioskify executable to the target machine; `C:\kioskify.exe` works.
* Log into the user you would like to function as a kiosk.
* Open `regedit.exe` and navigate to `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`.
* Replace the value of the `shell` key with `<kioskify path> <target path>`; the value `C:\kioskify.exe C:\Windows\System32\mstsc.exe` will target the Windows Remote Desktop client for example.
* Now the user should be configured as a Kiosk, and the target application should launch on logon instead of the Windows shell. When the target application closes, you will be logged out automatically. You can still use Task Manager to run any application, including `explorer.exe` or `regedit.exe` if you would like to restore the original Windows shell.
