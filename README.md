# Java Environment Management Tool

A tool for managing Java environments on Windows systems, capable of automatically detecting, installing, uninstalling, and switching Java versions.

zh_CN 简体中文 (Java_environment_choose/blob/main/README_CN.md)
## Usage Restrictions

### Scope of Use
- This tool is for personal learning and communication purposes only
- Commercial use is strictly prohibited
- Use in production environments is strictly prohibited
- Use in any environment that may pose system risks is strictly prohibited

### Legal Risk Notice
- Using this tool may involve system environment variable modifications, posing system stability risks
- Installing third-party Java distributions may involve license compliance issues
- Use in non-personal learning environments may violate relevant license agreements
- Users are solely responsible for any legal disputes arising from the use of this tool

## Legal Notices

### Trademark Notice
- Java is a registered trademark of Oracle and/or its affiliates
- OpenJDK is a trademark of Oracle and/or its affiliates
- Amazon Corretto is a trademark of Amazon.com, Inc. or its affiliates
- Eclipse Temurin is a trademark of Eclipse Foundation
- Windows is a registered trademark of Microsoft Corporation

### License Notice
- This tool itself is released under the GNU General Public License v3.0 (GPL-3.0)
- Java distributions installed through this tool are subject to their respective vendors' license terms
- If you modify and distribute the source code of this tool, you must:
  - Use the same GPL v3 license
  - Provide the modified source code
  - Retain the original copyright notice

### Third-Party Software Licenses
This tool uses the following third-party libraries:
- PyInstaller: GPL v2
- requests: Apache License 2.0
- Other dependencies can be found in requirements.txt

### Privacy Policy
- This tool does not collect, store, or transmit any user data
- Network connections are only used for downloading Java installation packages and verifying version information
- All downloads are directly connected to official sources, without intermediate servers
- No user operation logs or system information are recorded

### Disclaimer
- This tool is provided solely as a Java environment management utility
- No guarantees are provided for the functionality, security, or compatibility of Java distributions installed through this tool
- Users are advised to download Java distributions directly from official channels
- Users assume all risks associated with using this tool
- No responsibility is taken for system issues, data loss, or business interruptions caused by using this tool
- Compatibility with all Windows versions is not guaranteed
- The right to modify or terminate the service is reserved

## Features

- Automatic detection of installed Java versions
- Support for installing multiple Java versions (8/11/17/21)
- Support for multiple Java distributions (OpenJDK/Amazon Corretto/Eclipse Temurin)
- Automatic environment variable configuration
- Support for Java uninstallation
- Support for switching between Java versions

## Usage

1. Download and run `Java Environment Management Tool.exe`
2. Select the desired operation from the menu:
   - 1: Detect installed Java versions
   - 2: Install new Java version
   - 3: Uninstall Java
   - 4: Switch Java version
   - 5: Exit program

## Important Notes

1. Run the program with administrator privileges
2. Administrator rights are required for Java installation/uninstallation
3. Restart the command prompt after switching Java versions
4. It is recommended to check currently installed Java versions before installing new ones

## System Requirements

- Windows 10 or later
- Administrator privileges
- At least 2GB of available disk space

## Developer Information

To modify or repackage the program:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the build script:
```bash
python build.py
```

The packaged program will be located in the `dist` directory.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

The complete license text can be found in the [LICENSE](LICENSE) file.

### License Summary

- You are free to run, copy, distribute, study, modify, and improve the software
- You must retain the original copyright notice and license
- If you distribute modified versions, you must use the same license
- The software is provided "as is" without any warranty

For more information, visit the [GNU GPL v3 Official Website](https://www.gnu.org/licenses/gpl-3.0.html) 
