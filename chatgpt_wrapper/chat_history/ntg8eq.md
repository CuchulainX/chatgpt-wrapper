Model: Default (GPT-3.5)

> I would like to install Windows 11 into hardware that is not on the hcl. How do I go about changing the install prefecture so that the hardware checks are skipped
> 
> 1 / 1

It is not recommended to install Windows 11 on hardware that is not on the Hardware Compatibility List (HCL) as it may cause issues with the stability and performance of the operating system.

That being said, if you still want to proceed with the installation, you can try the following steps to bypass the hardware checks:

1.  Create a Windows 11 installation media using the Media Creation Tool or other similar tools.
    
2.  Boot from the installation media and when you get to the "Install now" screen, press Shift+F10 to open a command prompt.
    
3.  Type "regedit" and hit Enter to open the Registry Editor.
    
4.  Navigate to the following key: HKEY\_LOCAL\_MACHINE\\SYSTEM\\Setup
    
5.  Create a new DWORD value named "SkipEula" and set its value to 1.
    
6.  Create a new DWORD value named "SkipHardwareChecks" and set its value to 1.
    
7.  Close the Registry Editor and continue with the installation.
    

Please note that by bypassing the hardware checks, you may encounter issues with the stability and performance of the operating system, as it may not be optimized for your specific hardware configuration. It is also important to note that installing an operating system on hardware that is not on the HCL is not supported by Microsoft, and may void any warranties or support agreements you have in place.

1 / 1

> Cool
> 
> 1 / 1

Glad to hear that! If you have any further questions or if there's anything else I can help you with, just let me know.

1 / 1