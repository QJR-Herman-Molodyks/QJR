import os
import fileTagging
from globals import home

def recognizeFileType(fileDetailed, FileTag=None):
    # fileDetailed = fileDetailed.lower()

    if FileTag is None:
        f_tag = "  "
    else:
        f_tag = FileTag.identify_tag(os.path.abspath(fileDetailed))

    # prefix = "\033[33m > \033[0m"
    prefix = " > "

    try:
        actualFileSize = os.path.getsize(fileDetailed)

        if actualFileSize < 2000:
            fileSize = f"{actualFileSize} bytes"

        elif actualFileSize < 2000000:
            fileSize = f"{actualFileSize/1000} KB"

        elif actualFileSize < 2000000000:
            fileSize = f"{actualFileSize/1000000} MB"

        elif actualFileSize < 2000000000000:
            fileSize = f"{actualFileSize/1000000000} GB"

        elif actualFileSize < 2000000000000000:
            fileSize = f"{actualFileSize/1000000000000} TB"

        elif actualFileSize < 2000000000000000000:
            fileSize = f"{actualFileSize/1000000000000000} PB"

        elif actualFileSize < 2000000000000000000000:
            fileSize = f"{actualFileSize/1000000000000000000} EB"

        else:
            fileSize = f"{actualFileSize/1000000000000000000000} ZB"

    except OSError as e:
        fileSize = f"{e}"
    except Exception as e:
        print(f"\033[31mError > {e} \033[0m")

    # types_db = {
    #     ".py": {
    #             "description": " 🐍 Python File",
    #             "icon": " 📄"},
    #     ".txt": {
    #             "description": " 📝 Text File",
    #             "icon": " 📄"},
    #     ".cfg": {
    #             "description": " ⚙️ Configuration File",
    #             "icon": " ⚙️"
    #             },
    #     ".conf": {
    #             "description": " ⚙️ Configuration File",
    #             "icon": " ⚙️"},
    #     ".config": {
    #             "description": " ⚙️ Configuration File",
    #             "icon": " ⚙️"
    #             },
    #     ".qjr": {
    #             "description": " ⚙️ Q-J-R File",
    #             "icon": " ⚙️"
    #             },
    #     ".json": {
    #             "description": " 📝 JSON Dictionary File",
    #             "icon": " 📄"
    #             },
    #     ".log": {
    #             "description": " 📝 Log",
    #             "icon": " 📝"
    #             },
    #     ".syslog": {
    #             "description": " ⚙️ System Log",
    #             "icon": " ⚙️"
    #             },
    #     ".bin": {
    #             "description": " 📟 Binary File",
    #             "icon": " 📟"
    #             },
    #     ".csv": {
    #             "description": " 📝 CSV Dictionary File",
    #             "icon": " 📝"
    #             },
    #     ".xml": {
    #             "description": " 📝 XML File",
    #             "icon": " 📝"
    #             },
    #     ".md": {
    #             "description": " 📝 Markdown File",
    #             "icon": " 📝"
    #             },
    #     ".yml": {
    #             "description": " 📝 YAML File",
    #             "icon": " 📝"
    #             },
    #     ".ini": {
    #             "description": " ⚙️ INI Configuration File",
    #             "icon": " ⚙️"
    #             },
    #     ".yaml": {
    #             "description": " 📝 YAML File",
    #             "icon": " 📝"
    #             },
    #     ".logtxt": {
    #             "description": " 📝 Log Text File",
    #             "icon": " 📝"
    #             },
    #     ".toml": {
    #             "description": " 📝 TOML File",
    #             "icon": " 📝"
    #             },
    #     ".pyc": {
    #             "description": " 🐍 Python Cache File",
    #             "icon": " 🐍"
    #             },
    #     ".ld": {
    #             "description": " ⚙️ Linker Script File",
    #             "icon": " ⚙️"
    #             }
    # }


    if fileDetailed.lower().endswith(".py"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🐍 Python File")
    elif fileDetailed.lower().endswith(".txt"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 Text File")
    elif fileDetailed.lower().endswith(".cfg"):
        print(f"{prefix} ⚙️  {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ⚙️  Configuration File")
    elif fileDetailed.lower().endswith(".conf"):
        print(f"{prefix} ⚙️  {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ⚙️ Configuration File")
    elif fileDetailed.lower().endswith(".config"):
        print(f"{prefix} ⚙️  {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ⚙️ Configuration File")
    elif fileDetailed.lower().endswith(".qjr"):
        print(f"{prefix} ⚙️  {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ⚙️ Q-J-R File")
    elif fileDetailed.lower().endswith(".json"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 JSON Dictionary File")
    elif fileDetailed.lower().endswith(".log"):
        print(f"{prefix} 📝 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 Log")
    elif fileDetailed.lower().endswith(".syslog"):
        print(f"{prefix} 📝 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ⚙️ System Log")
    elif fileDetailed.lower().endswith(".bin"):
        print(f"{prefix} 📟 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📟 Binary File")

    elif fileDetailed.lower().endswith(".csv"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 CSV Dictionary File")
    elif fileDetailed.lower().endswith(".xml"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 XML File")
    elif fileDetailed.lower().endswith(".md"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 Markdown File")
    elif fileDetailed.lower().endswith(".yml"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 YAML File")
    elif fileDetailed.lower().endswith(".ini"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ⚙️ INI Configuration File")
    elif fileDetailed.lower().endswith(".yaml"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 YAML File")
    elif fileDetailed.lower().endswith(".logtxt"):
        print(f"{prefix} 📝 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 Log Text File")
    elif fileDetailed.lower().endswith(".toml"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 TOML File")

    elif fileDetailed.lower().endswith(".pyc"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🐍 Python Cache File")

    elif fileDetailed.lower().endswith(".ld"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📝 Linker Script File")

    elif fileDetailed.lower().endswith(".zip"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 Zip-Archive")

    elif fileDetailed.lower().endswith(".tar"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 Tar-Archive")
    elif fileDetailed.lower().endswith(".tar.gz"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 Gzipped Tar-Archive")
    elif fileDetailed.lower().endswith(".gz"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 GZip-Archive")
    elif fileDetailed.lower().endswith(".xz"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 XZip-Archive")
    elif fileDetailed.lower().endswith(".7z"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 7-Zip Archive")
    elif fileDetailed.lower().endswith(".rar"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 WinRAR-Archive")
    elif fileDetailed.lower().endswith(".zstd"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 ZSTD-Archive")
    elif fileDetailed.lower().endswith(".a"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 A UNIX Archive")
    elif fileDetailed.lower().endswith(".ar"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 AR UNIX Archive")
    elif fileDetailed.endswith(".br"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 Brotli Archive")
    elif fileDetailed.endswith(".lz"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 LZip Archive")
    elif fileDetailed.endswith(".tar.bz2"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 Bzipped Tar-Archive")
    elif fileDetailed.endswith(".zipx"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 ZipX Archive")
    elif fileDetailed.endswith(".lz4"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 LZip-4 Archive")

    elif fileDetailed.endswith("."):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📄 Unknown File Type")

    elif fileDetailed.endswith(".deb"):
        print(f"{prefix} 📥 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📥 Debian Package Installer")
    elif fileDetailed.endswith(".rpm"):
        print(f"{prefix} 📥 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📥 RPM Package Installer")
    elif fileDetailed.endswith(".apk"):
        print(f"{prefix} 📱 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📱 Android Package Installer")
    elif fileDetailed.endswith(".ipa"):
        print(f"{prefix} 📱 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📱 iOS App Store Package")

    elif fileDetailed.endswith(".png"):
        print(f"{prefix} 🌠 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🌠 PNG-Image")
    elif fileDetailed.endswith(".heic"):
        print(f"{prefix} 📸 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🌠 Heic / HEIF-Image")
    elif fileDetailed.endswith(".jpg"):
        print(f"{prefix} 🌠 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🌠 JPG-Image")
    elif fileDetailed.endswith(".jpeg"):
        print(f"{prefix} 🌠 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🌠 JPEG-Image")
    elif fileDetailed.endswith(".webp"):
        print(f"{prefix} 📷 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📷 WEBP-media")

    elif fileDetailed.endswith(".mp4"):
        print(f"{prefix} 🎥 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🎥 MP4-VIDEO")
    elif fileDetailed.endswith(".mov"):
        print(f"{prefix} 🎬 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🎬 MOV-VIDEO")
    elif fileDetailed.endswith(".avi"):
        print(f"{prefix} 📼 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📼 AVI-VIDEO")
    elif fileDetailed.endswith(".mkv"):
        print(f"{prefix} 📽️ {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📽️ MKV-VIDEO")
    elif fileDetailed.endswith(".wmv"):
        print(f"{prefix} 📽️ {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📽️ WMV-VIDEO")

    elif fileDetailed.endswith(".mp3"):
        print(f"{prefix} 🔊 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🔊 MP3-AUDIO")
    elif fileDetailed.endswith(".wav"):
        print(f"{prefix} 🔊 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🔊 WAV-AUDIO")
    elif fileDetailed.endswith(".aiff"):
        print(f"{prefix} 🔊 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🔊 AIFF-AUDIO")

    elif fileDetailed.endswith(".iso"):
        print(f"{prefix} 💿 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 💿 ISO DISK IMAGE")
    elif fileDetailed.endswith(".dmg"):
        print(f"{prefix} 💾 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 💾 DISK IMAGE")
    elif fileDetailed.endswith(".img"):
        print(f"{prefix} 💾 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 💾 DISK IMAGE")
    elif fileDetailed.endswith(".ima"):
        print(f"{prefix} 💾 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 💾 DISK IMAGE")

    elif fileDetailed.endswith(".out"):
        print(f"{prefix} 💡 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 💡 Output Executable File")

    elif fileDetailed.endswith(".exe"):
        print(f"{prefix} 🔌 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🔌 Windows Executable File")
    elif fileDetailed.endswith(".msi"):
        print(f"{prefix} ⬇️ {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ⬇️ Windows MSI-Installer")
    elif fileDetailed.endswith(".dll"):
        print(f"{prefix} ⚙️ {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ⚙️ Windows DLL")
    elif fileDetailed.endswith(".sys"):
        print(f"{prefix} ⚙️ {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ⚙️ System File")
    elif fileDetailed.endswith(".bat"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️ Batch Script")
    elif fileDetailed.endswith(".cmd"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️ CMD Script")
    elif fileDetailed.endswith(".drv"):
        print(f"{prefix} 🛟 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🛟 Device Driver")

    elif fileDetailed.endswith(".html"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🌐 HTML File")
    elif fileDetailed.endswith(".css"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🎨 CSS File")
    elif fileDetailed.endswith(".js"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ⚙️ JavaScript File")


    # Classic Mac OS

    elif fileDetailed.endswith(".sit"):
        print(f" > 📦 {fileDetailed:<32} {f_tag:<2} - {os.path.getsize(fileDetailed)} bytes - 📦 StuffIt Archive")

    elif fileDetailed.endswith(".hqx"):
        print(f" > 📦 {fileDetailed:<32} {f_tag:<2} - {os.path.getsize(fileDetailed)} bytes - 📦 BinHex Archive")

    elif fileDetailed.endswith(".sitx"):
        print(f" > 📦 {fileDetailed:<32} {f_tag:<2} - {os.path.getsize(fileDetailed)} bytes - 📦 StuffIt X Archive")

    # Programming languages, scripts, UNIX and Linux

    elif fileDetailed.endswith(".sh"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️ Shell script")

    elif fileDetailed.endswith(".c"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ C script")

    elif fileDetailed.endswith(".h"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ C / C++ header")

    elif fileDetailed.endswith(".cpp"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ C++ script")

    elif fileDetailed.endswith(".asm"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ Assembly script")

    elif fileDetailed.endswith(".ps1"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ PowerShell script")

    elif fileDetailed.endswith(".rb"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️ 💎 Ruby script")

    elif fileDetailed.endswith(".go"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️ Go script")

    elif fileDetailed.endswith(".f90"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ Fortran script")

    elif fileDetailed.endswith(".rs"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ Rust script")

    elif fileDetailed.endswith(".php"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ PHP script")

    elif fileDetailed.endswith(".pl"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ Perl script")

    elif fileDetailed.endswith(".fs"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ F# script")

    elif fileDetailed.endswith(".swift"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ Swift script")

    elif fileDetailed.endswith(".kt"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ Kotlin script")

    elif fileDetailed.endswith(".lua"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ Lua script")

    elif fileDetailed.endswith(".dart"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ Dart script")

    elif fileDetailed.endswith(".r"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ R script")

    elif fileDetailed.endswith(".jl"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ Julia script")

    elif fileDetailed.endswith(".m"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ MATLAB script")

    elif fileDetailed.endswith(".vbs"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ VBScript file")

    elif fileDetailed.endswith(".vb"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ Visual Basic script")

    elif fileDetailed.endswith(".dox"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ DoX script")

    elif fileDetailed.endswith(".cxx"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ C++ script")

    elif fileDetailed.endswith(".cp"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕹️️ C++ script")

    elif fileDetailed.endswith(".jar"):
        print(f"{prefix} ☕️ {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ☕️ Java Archive Executable File")

    elif fileDetailed.endswith(".class"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ☕️ Java Class File")

    elif fileDetailed.endswith(".java"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - ☕️ Java File")

    elif fileDetailed.endswith(".ts"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🌐 TypeScript File")

    elif fileDetailed.endswith(".jsx"):
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🌐 JSX File")

    # SQLite and DBs

    elif fileDetailed.endswith(".db"):
        print(f"{prefix} 🗃️ {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🗃️ Database File")

    elif fileDetailed.endswith(".sqlite"):
        print(f"{prefix} 🗃️ {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🗃️ SQLite Database File")

    # QEMU and VMs

    elif fileDetailed.endswith(".utm"):
        print(f"{prefix} 🖥️ {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🖥️ UTM Virtual Machine File")

    elif fileDetailed.endswith(".qcow2"):
        print(f"{prefix} 💾 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 💾 QEMU disk image")

    elif fileDetailed.endswith(".qcow"):
        print(f"{prefix} 💾 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 💾 QEMU disk image")


    # macOS

    elif fileDetailed.endswith(".app"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 macOS Application")

    elif fileDetailed.endswith(".plist"):
        print(f"{prefix} 🖊️ {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🖊️ macOS Property List")

    elif fileDetailed.endswith(".pkg"):
        print(f"{prefix} 📦 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📦 macOS Package (Installer)")

    # Q-J-R Executables and Low-Level format files

    elif fileDetailed.endswith(".qjrexc"):
        print(f"{prefix} 📟 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📟 Q-J-R Executable File")

    elif fileDetailed.endswith(".qjrelf"):
        print(f"{prefix} 🔗 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🔗 QJR Executable Linkable File")

    elif fileDetailed.endswith(".qjro"):
        print(f"{prefix} 🔘 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🔘Q-J-R Object File")


    # Special Personalized

    elif fileDetailed == "makefile" or fileDetailed == "Makefile":
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🧱 Makefile")

    elif fileDetailed == "README" or fileDetailed == "README.md" or fileDetailed == "README.txt":
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📖 Read-Me")

    elif fileDetailed == "Dockerfile" or fileDetailed == "dockerfile":
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🐳 Docker Configuration File")

    elif fileDetailed.lower() == "license" or fileDetailed.lower() == "license.txt":
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📖 License File")

    elif fileDetailed.lower() == "docs" or fileDetailed.lower() == "docs.md":
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📚 Documentation file")

    # Git

    elif fileDetailed.lower() == "docs" or fileDetailed.lower() == "docs.md":
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📚 Documentation file")

    elif fileDetailed.lower() == ".gitignore":
        print(f"{prefix} 🚫 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 🕵️ Git Ignore File")

    # Else

    else:
        print(f"{prefix} 📄 {fileDetailed:<32} {f_tag:<2} - {fileSize:<12} - 📄 File")