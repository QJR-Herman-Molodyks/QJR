
import os
import json

class FileTag:
    def __init__(self, home):
        self.version = "1.0"
        self.home_pos = home

    def initialize(self):
        try:
            with open(f"{self.home_pos}/db/tags.qjr", "r") as f:
                self.tags = json.load(f)

        except FileNotFoundError:
            print("\033[31mTag configuration file not found!\033[0m")
            print("Trying to recreate...")
            with open(f"{self.home_pos}/db/tags.qjr", "w") as f:
                f.write("{}")
                self.tags = {}

        except Exception as e:
            print(f"\033[31mError occurred while loading file tags > {e}\033[0m")
            self.tags = {}


    def save_tag(self, home, tags_db):
        with open(f"{home}/db/tags.qjr", "w") as f:
            json.dump(tags_db, f, indent=4)
    #
    # def help_tag(self):
    #     print(f"""==== Q-J-R Tagging System v{self.version} ====""")


    def add_tag(self, file_path, color):
        if color.lower() in ["red", "green", "blue", "yellow", "magenta"]:
            if os.path.exists(file_path):
                self.tags[os.path.abspath(file_path)] = color.lower()
                self.save_tag(self.home_pos, self.tags)
            else:
                print("\033[31mFile not found!\033[0m")

        else:
            print("\033[31mInvalid color!\033[0m")

    def del_tag(self, file_path):
        try:
            del self.tags[os.path.abspath(file_path)]
            self.save_tag(self.home_pos, self.tags)

        except KeyError:
            print("\033[31mTag not found!\033[0m")

    def clean_all_tags(self):
        self.tags.clear()
        self.save_tag(self.home_pos, self.tags)

    def clean_tags(self, target_color):
        self.tags_cop
        for file_path, tag_color in self.tags.items():
            if tag_color == target_color:
                del self.tags[os.path.abspath(file_path)]



    def show_tag(self, target_tag):
        target_tag = target_tag.lower()

        if target_tag in ["@all", "all"]:
            self.show_all_tags()
            return

        if target_tag in ["red", "green", "blue", "yellow", "magenta"]:
            found = False

            for file_path, tag in self.tags.items():
                if tag == target_tag:
                    found = True

                    if tag == "red":
                        print(f"\033[91m█\033[0m -> {file_path}")
                    elif tag == "green":
                        print(f"\033[92m█\033[0m -> {file_path}")
                    elif tag == "blue":
                        print(f"\033[94m█\033[0m -> {file_path}")
                    elif tag == "yellow":
                        print(f"\033[93m█\033[0m -> {file_path}")
                    elif tag == "magenta":
                        print(f"\033[95m█\033[0m -> {file_path}")

            if not found:
                print("\033[31mTag not found.\033[0m")

        else:
            print("\033[31mInvalid target tag!\033[0m")
    def show_all_tags(self):
        for file_path, tag in self.tags.items():
            if tag == "red":
                print(f"\033[91m█\033[0m -> {file_path}")
            elif tag == "green":
                print(f"\033[92m█\033[0m -> {file_path}")
            elif tag == "blue":
                print(f"\033[94m█\033[0m -> {file_path}")
            elif tag == "yellow":
                print(f"\033[93m█\033[0m -> {file_path}")
            elif tag == "magenta":
                print(f"\033[95m█\033[0m -> {file_path}")


    def identify_tag(self, file_path):
        if os.path.exists(file_path) and file_path in self.tags:
            file_tag = self.tags[file_path]

            if file_tag == "red":
                return "\033[91m█\033[0m"
            elif file_tag == "green":
                return "\033[92m█\033[0m"
            elif file_tag == "blue":
                return "\033[94m█\033[0m"
            elif file_tag == "yellow":
                return "\033[93m█\033[0m"
            elif file_tag == "magenta":
                return "\033[95m█\033[0m"
        else:
            return " "



# TESTING
if __name__ == "__main__":
    FileTag("/Users/Apple/PycharmProjects/Work/Projects/Q-J-R/6.7.0/RC 2/Q-J-R 6.7.0/system").show_tag("red")
    FileTag("/Users/Apple/PycharmProjects/Work/Projects/Q-J-R/6.7.0/RC 2/Q-J-R 6.7.0/system").show_tag("yellow")
    FileTag("/Users/Apple/PycharmProjects/Work/Projects/Q-J-R/6.7.0/RC 2/Q-J-R 6.7.0/system").show_all_tags()
