from enum import IntEnum
from sys import stderr, stdout
from datetime import datetime

class Level(IntEnum):
    OFF = 0
    FATAL = 1
    ERROR = 2
    WARN = 3
    INFO = 4
    DEBUG = 5
    ALL = 6

class Log:
    def __init__(self):
        self.level = Level.WARN
        self.fn = {}
        self.fn[Level.INFO] = self.info
        self.fn[Level.WARN] = self.warn
        self.fn[Level.ERROR] = self.error
        self.fn[Level.FATAL] = self.fatal
        self.fn[Level.DEBUG] = self.debug

    def setLevel(self, level: Level):
        self.level = level

    def info(self, m):
        if self.level >= Level.INFO:
            self.__print(m, Level.INFO)

    def warn(self, m):
        if self.level >= Level.WARN:
            self.__print(m, Level.WARN)

    def error(self, m):
        if self.level >= Level.ERROR:
            self.__print(m, Level.ERROR)

    def fatal(self, m):
        if self.level >= Level.FATAL:
            self.__print(m, Level.FATAL)

    def debug(self, m):
        if self.level >= Level.DEBUG:
            self.__print(m, Level.DEBUG)

    def log(self, m, level: Level):
        self.fn[level](m)

    def __print(self, m, level: Level):
        d = datetime.today()

        print("[{}]\t[{}/{:02d}/{:02d}] [{:02d}:{:02d}:{:02d}] ".format(level.name, d.year, d.month, d.day, d.hour, d.minute, d.second) + m,
        file=level < Level.WARN and stdout or stderr)