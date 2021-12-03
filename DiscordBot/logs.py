import datetime


def get_todays_logs_filename():
    return f"./logs/{datetime.date.today()}.txt"


def logs_format(line: str):
    return datetime.datetime.today().strftime("[%d-%m-%Y <> %H:%M:%S] " + line + "\n")


class Logs:
    def __init__(self, file=get_todays_logs_filename()):
        self.file = open(file, "a+")

    def writelines(self, lines: list[str]):
        _lines = []
        for i in range(len(lines)):
            _lines[i] = logs_format(lines[i])
        self.file.writelines(_lines)
        self.flush()

    def writeline(self, line: str):
        self.file.writelines(line if line == "\n" else logs_format(line))
        self.flush()

    def flush(self):
        self.file.flush()

    def close_file(self):
        self.file.close()
