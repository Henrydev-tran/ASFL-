def Lexer(file):
    lines = file.readlines()
    default_indent = "4"
    tree = {}

    tree["imports"] = {}

    for i in lines:
        import_count = 0
    
    if i.startswith("import") and i[6] == " ":
        names = ""

        for e in range(7, len(i)):

            if i[e] == " ":
                continue

            if not i[e] == ",":
                names += i[e]

            else:
                tree["imports"][str(import_count)] = names
                names = ""
                import_count += 1
        

class MiniPy:
    def __init__(self, project_name: str):
        self.project_name = project_name
    
    def load_main(self, dir, name):
        self.main_dir = f"{dir}/{name}"
        self.main_file = open(f"{self.main_dir}")
        self.main_lines = self.main_file.readlines()

    def get_imports(self):
        pass

    def load_all(self):
        pass