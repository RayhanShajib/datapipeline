class FileHandler:
    #filepath: str # indicated filepath in a class
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        return None
    
    def read(self) -> list[str]:
        rows: list[str] = []
        try:
            filehandle = open(self.filepath, 'r', encoding="UTF-8")
            row = filehandle.readline()
            while row != "":
                rows.append(row.strip('\n'))
                row = filehandle.readline()
            filehandle.close()
        except Exception:
            print("File not found")
            exit(-1)
        return rows