import os
import json
import shutil

PKG_DIR = "qjr_packages"
INSTALLED_DB = "installed.json"


def load_installed():
    if not os.path.exists(INSTALLED_DB):
        return {}
    with open(INSTALLED_DB, "r") as f:
        return json.load(f)


def save_installed(data):
    with open(INSTALLED_DB, "w") as f:
        json.dump(data, f, indent=4)


def install(pkg_path):
    meta_path = os.path.join(pkg_path, "package.json")

    if not os.path.exists(meta_path):
        print("No package.json found")
        return

    with open(meta_path, "r") as f:
        meta = json.load(f)

    name = meta["name"]

    target = os.path.join(PKG_DIR, name)

    if os.path.exists(target):
        print("Package already installed")
        return

    shutil.copytree(pkg_path, target)

    installed = load_installed()
    installed[name] = meta
    save_installed(installed)

    print(f"Installed {name}")


def remove(name):
    target = os.path.join(PKG_DIR, name)

    if os.path.exists(target):
        shutil.rmtree(target)

    installed = load_installed()

    if name in installed:
        del installed[name]
        save_installed(installed)

    print(f"Removed {name}")


def list_packages():
    installed = load_installed()
    for name, meta in installed.items():
        print(f"{name} - {meta.get('version')}")


def info(name):
    installed = load_installed()
    if name in installed:
        print(json.dumps(installed[name], indent=4))
    else:
        print("Not installed")

