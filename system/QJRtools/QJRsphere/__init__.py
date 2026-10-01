import json
import os
import tempfile

from ..QJRsphere_verification import save_verification, get_sphere_path

# Sphere Control
class Sphere:
    def __init__(self, home: str, db_path: str):
        # QJRsphere info
        self.SPHERES_VERSION = "v2.6"
        self.SPHERES_NAME = "QJRsphere"

        # Configuration
        self.home = home
        self.db_path = db_path
        self.spheres_db = {}

        # Save backup before overwriting DB
        self.save_backup = False

        # Init
        self.load_db()

    # INFORMATION

    def print_data(self):
        print(f"""{self.SPHERES_NAME} | {self.SPHERES_VERSION}
Home point -> {self.home}
Spheres DB -> {self.spheres_db}
DB path    -> {self.db_path}
Activated Sphere -> {self.return_active()}""")

    def return_active(self):
        for sphere, data in self.spheres_db.items():
            if isinstance(data, dict) and data.get("using") is True:
                return sphere

        return None

    def active(self):
        return self.return_active()

    def check_activated(self, target_sphere: str):
        if target_sphere not in self.spheres_db:
            return None

        return self.spheres_db[target_sphere].get("using", False)

    def check(self, sphere_name: str):
        if sphere_name not in self.spheres_db:
            print(f"Sphere not found -> {sphere_name}")
            return

        print(" --- Sphere Found ---")
        print(f"Name -> {sphere_name}")
        print(f"Status -> {'Active' if self.spheres_db[sphere_name]['using'] else 'Inactive'}")

    # CONFIGURATION

    def change_home(self, new_home: str):
        self.home = new_home

    def change_sphere_db_path(self, new_sphere_db_path: str):
        self.db_path = new_sphere_db_path

    # DATABASE VALIDATION

    def validate_db(self, database):
        if not isinstance(database, dict):
            return False

        active_count = 0

        required_keys = {
            "dimensions_x",
            "dimensions_y",
            "dimensions_z",
            "is_external",
            "using"
        }

        for name, data in database.items():
            if not isinstance(name, str):
                return False

            if not isinstance(data, dict):
                return False

            if not required_keys.issubset(data.keys()):
                return False

            try:
                x = float(data["dimensions_x"])
                y = float(data["dimensions_y"])
                z = float(data["dimensions_z"])
            except (TypeError, ValueError):
                return False

            if x <= 0 or y <= 0 or z <= 0:
                return False

            if not isinstance(data["is_external"], bool):
                return False

            if not isinstance(data["using"], bool):
                return False

            if data["using"]:
                active_count += 1

        if active_count > 1:
            return False

        return True

    # DATABASE LOGIC

    def load_db(self):
        try:
            with open(self.db_path, "r", encoding="utf-8") as json_file:
                database = json.load(json_file)

            if not self.validate_db(database):
                print("\033[31mQJRsphere -> Database structure is invalid!\033[0m")
                self.spheres_db = {}
                return False

            self.spheres_db = database
            return True

        except FileNotFoundError:
            self.spheres_db = {}
            return True

        except json.JSONDecodeError:
            print("\033[31mQJRsphere -> Database is corrupted!\033[0m")
            self.spheres_db = {}
            return False

        except OSError as e:
            print(f"\033[31mQJRsphere -> Database error -> {e}\033[0m")
            return False

        except Exception as e:
            print(f"\033[31mQJRsphere -> Unexpected database error -> {e}\033[0m")
            return False

    def save_backup_db(self):
        """
        Create a temporary backup of the current DB.

        This method is used only when self.save_backup is True.
        """

        if not self.save_backup:
            return True

        if not os.path.exists(self.db_path):
            return True

        try:
            with open(self.db_path, "r", encoding="utf-8") as source:
                database = source.read()

            fd, backup_path = tempfile.mkstemp(
                prefix="qjrsphere_backup_",
                suffix=".qjr"
            )

            with os.fdopen(fd, "w", encoding="utf-8") as backup:
                backup.write(database)

            print(f"QJRsphere -> Temporary DB backup -> {backup_path}")
            return True

        except OSError as e:
            print(f"\033[31mQJRsphere -> Backup error -> {e}\033[0m")
            return False

    def save(self):
        """
        Save the current DB.

        If self.save_backup is True, a temporary backup is created first.
        """

        if self.save_backup:
            if not self.save_backup_db():
                print("\033[31mQJRsphere -> Backup failed. Save cancelled.\033[0m")
                return False

        directory = os.path.dirname(os.path.abspath(self.db_path))

        try:
            os.makedirs(directory, exist_ok=True)

            with open(self.db_path, "w", encoding="utf-8") as outfile:
                json.dump(self.spheres_db, outfile, indent=4, ensure_ascii=False)

            save_verification(get_sphere_path())
            return True


        except OSError as e:
            print(f"\033[31mQJRsphere -> Cannot save database -> {e}\033[0m")
            return False

    def load(self, new_path: str):
        new_path = os.path.expanduser(new_path)

        if not os.path.isfile(new_path):
            print(f"\033[31mQJRsphere -> Database does not exist -> {new_path}\033[0m")
            return False

        try:
            with open(new_path, "r", encoding="utf-8") as json_file:
                new_database = json.load(json_file)

        except json.JSONDecodeError:
            print("\033[31mQJRsphere -> Target database is corrupted!\033[0m")
            return False

        except OSError as e:
            print(f"\033[31mQJRsphere -> Cannot load database -> {e}\033[0m")
            return False

        if not self.validate_db(new_database):
            print("\033[31mQJRsphere -> Target database has invalid structure!\033[0m")
            return False

        if not self.save():
            print("\033[31mQJRsphere -> Current database could not be saved.\033[0m")
            return False

        self.spheres_db = new_database
        self.db_path = new_path

        print(f"QJRsphere -> DB has been loaded -> {self.db_path}")
        return True

    # SPHERE LIST

    def list(self):
        print("N     |           NAME           |   TYPE   | ACTIVE | LENGTH (X) | HEIGHT (Y) | WIDTH  (Z) |     VOLUME     |")

        if not self.spheres_db:
            print("No spheres found.")
            return

        for listing, (name, sphere) in enumerate(self.spheres_db.items(), start=1):
            try:
                x = float(sphere["dimensions_x"])
                y = float(sphere["dimensions_y"])
                z = float(sphere["dimensions_z"])

                sphere_type = "External" if sphere["is_external"] else "Internal"
                active = "Yes" if sphere["using"] else "No"
                volume = x * y * z

                print(f"{listing:<5} | {name:<24} | {sphere_type:<8} | {active:<6} | {x:<9.2f}m | {y:<9.2f}m | {z:<9.2f}m | {volume:<9.2f} m**3 |")

            except (KeyError, TypeError, ValueError) as e:
                print(f"\033[31m{listing:<5} | ERROR in sphere '{name}' -> {e}\033[0m")

    # SPHERE OPERATIONS

    def activate(self, name: str):
        if name not in self.spheres_db:
            print("\033[31mQJRsphere v2.6: Target sphere is not found to activate!\033[0m")
            return False

        for sphere in self.spheres_db.values():
            sphere["using"] = False

        self.spheres_db[name]["using"] = True

        return self.save()

    def deactivate(self):
        changed = False

        for sphere in self.spheres_db.values():
            if sphere["using"]:
                sphere["using"] = False
                changed = True

        if changed:
            return self.save()

        return True

    def add(self, name: str, dmn_x: float, dmn_y: float, dmn_z: float, isexternal: bool, changing_data: bool = False):
        if not name.strip():
            print("\033[31mQJRsphere: Sphere name cannot be empty.\033[0m")
            return False

        if dmn_x <= 0 or dmn_y <= 0 or dmn_z <= 0:
            print("\033[31mQJRsphere: Sphere dimensions must be greater than zero.\033[0m")
            return False

        if name in self.spheres_db and not changing_data:
            print(f"\033[31mQJRsphere v2.6: Target name -> {name} already exists.\033[0m")
            return False

        old_using = False

        if changing_data and name in self.spheres_db:
            old_using = self.spheres_db[name].get("using", False)

        self.spheres_db[name] = {
            "dimensions_x": dmn_x,
            "dimensions_y": dmn_y,
            "dimensions_z": dmn_z,
            "is_external": isexternal,
            "using": old_using
        }

        return self.save()

    def delete(self, name: str, confirmation: bool):
        if name not in self.spheres_db:
            print("\033[31mQJRsphere v2.6: Target sphere does not exist.\033[0m")
            return False

        if not confirmation:
            print("\033[31mOperation is not confirmed -> Cancelled.\033[0m")
            return False

        del self.spheres_db[name]
        return self.save()

    def rename(self, name: str, new_name: str):
        if name not in self.spheres_db:
            print("\033[31mQJRsphere v2.6: Target sphere does not exist.\033[0m")
            return False

        if not new_name.strip():
            print("\033[31mQJRsphere v2.6: New name cannot be empty.\033[0m")
            return False

        if new_name in self.spheres_db:
            print("\033[31mQJRsphere v2.6: Sphere with this name already exists.\033[0m")
            return False

        self.spheres_db[new_name] = self.spheres_db.pop(name)

        return self.save()

    # COMMAND PARSER

    def parse_command(self, command: str):
        """
        Simple QJRsphere command parser.

        Example:
            add "my backpack" 1 2 3 ext

        Returns:
            ["add", "my backpack", "1", "2", "3", "ext"]
        """

        arguments = []
        current = []
        in_quotes = False
        escaped = False

        for char in command.strip():
            if escaped:
                current.append(char)
                escaped = False
                continue

            if char == "\\":
                escaped = True
                continue

            if char == '"':
                in_quotes = not in_quotes
                continue

            if char.isspace() and not in_quotes:
                if current:
                    arguments.append("".join(current))
                    current = []

                continue

            current.append(char)

        if escaped:
            current.append("\\")

        if in_quotes:
            print("\033[31mQJRsphere -> Unclosed quotation mark.\033[0m")
            return None

        if current:
            arguments.append("".join(current))

        return arguments

    # COMMAND EXECUTION

    def execute_command(self, cmd_sphere: str):
        cmd_sphere = cmd_sphere.strip()

        if not cmd_sphere:
            return

        args = self.parse_command(cmd_sphere)

        if args is None or not args:
            return

        command = args[0]
        command_args = args[1:]

        if command == "help":
            print("Available commands: help, exit, example, list, add, del, edit, rename, activate, deactivate, check, chdbpath, load, info")

        elif command == "example":
            print(f"""QJRsphere {self.SPHERES_VERSION} management EXAMPLES
[1] Creating a Sphere: add "backpack" 0.3 0.4 0.35 in
[2] Deleting a Sphere: del "backpack"
[3] Changing Sphere data: edit "backpack" 0.3 0.4 0.35 in
[4] Activating a Sphere: activate "backpack"
[5] Deactivating: deactivate
[6] Renaming a Sphere: rename "backpack" "bag"
[7] Checking if Sphere exists: check "backpack"
[8] Getting list of Spheres: list
[9] Changing DB path: chdbpath "/my_spheres/db.qjr"
[10] Loading Spheres DB: load "~/Downloads/imported_spheres.qjr"
[11] Getting examples: example
[12] Printing QJRsphere information: info
[13] Getting help: help
[14] Exiting: exit
""")

        elif command == "list":
            if command_args:
                print("\033[31mUsage -> list\033[0m")
                return

            self.list()

        elif command == "info":
            if command_args:
                print("\033[31mUsage -> info\033[0m")
                return

            self.print_data()

        elif command == "add" or command == "edit":
            if len(command_args) != 5:
                print(f'\033[31mUsage -> {command} "name" X Y Z in|ext\033[0m')
                return

            name = command_args[0]

            try:
                dimension_x = float(command_args[1])
                dimension_y = float(command_args[2])
                dimension_z = float(command_args[3])
            except ValueError:
                print("\033[31mQJRsphere -> Dimensions must be numbers.\033[0m")
                return

            sphere_type = command_args[4].lower()

            if sphere_type not in ("in", "ext"):
                print("\033[31mQJRsphere -> Sphere type must be 'in' or 'ext'.\033[0m")
                return

            if command == "edit" and name not in self.spheres_db:
                print(f"\033[31mQJRsphere -> Sphere '{name}' does not exist.\033[0m")
                return

            result = self.add(
                name,
                dimension_x,
                dimension_y,
                dimension_z,
                sphere_type == "ext",
                command == "edit"
            )

            if result:
                if command == "edit":
                    print(f"Sphere '{name}' data has been changed!")
                else:
                    print(f"Sphere '{name}' has been added!")

        elif command == "del":
            if len(command_args) != 1:
                print('\033[31mUsage -> del "sphere_name"\033[0m')
                return

            confirmation = input("Do you really want to delete this sphere? (y/N) ")
            self.delete(command_args[0], confirmation.lower() == "y")

        elif command == "activate":
            if len(command_args) != 1:
                print('\033[31mUsage -Ю activate "sphere_name"\033[0m')
                return

            self.activate(command_args[0])

        elif command == "deactivate":
            if command_args:
                print("\033[31mUsage -> deactivate\033[0m")
                return

            self.deactivate()

        elif command == "rename":
            if len(command_args) != 2:
                print('\033[31mUsage -> rename "old_name" "new_name"\033[0m')
                return

            self.rename(command_args[0], command_args[1])

        elif command == "check":
            if len(command_args) != 1:
                print('\033[31mUsage -> check "sphere_name"\033[0m')
                return

            self.check(command_args[0])

        elif command == "load":
            if len(command_args) != 1:
                print('\033[31mUsage -> load "path/to/db.qjr"\033[0m')
                return

            self.load(command_args[0])

        elif command == "chdbpath":
            if len(command_args) != 1:
                print('\033[31mUsage -> chdbpath "path/to/db.qjr"\033[0m')
                return

            new_path = os.path.expanduser(command_args[0])

            if os.path.exists(new_path):
                print("\033[31mQJRsphere -> DB with this path already exists.\033[0m")
                print("Use 'load' to load an existing database.")
                return

            old_path = self.db_path
            self.db_path = new_path

            if self.save():
                print("QJRsphere -> DB path has been changed.")
                print(f"QJRsphere -> New DB path -> {self.db_path}")
            else:
                self.db_path = old_path

        else:
            print(f"\033[31mQJRsphere -> Unknown command '{command}'\033[0m")

    # Sphere UI

    def ui(self):
        print(f"QJRsphere {self.SPHERES_VERSION} management")

        while True:
            try:
                active = self.return_active()
                prompt = f"({active}) " if active is not None else ""

                cmd_sphere = input(f"{prompt}QJRsphere v2.6 > ")

                if cmd_sphere.strip() == "exit":
                    break

                self.execute_command(cmd_sphere)

            except KeyboardInterrupt:
                print("\n\033[33m[interrupted]\033[0m")
                break

            except EOFError:
                print("\n\033[33m[EOF]\033[0m")
                break

            except Exception as e:
                print(f"\033[91mERROR -> {e}\033[0m")


# if __name__ == "__main__":
#     QJRsphere = Sphere(".", "sphere/db.qjr") # Set here your Sphere DB Path
#     QJRsphere.ui()