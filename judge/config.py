import os

basedir = os.path.abspath(os.path.dirname(__file__))

JUDGE_BIN_PATH = os.path.join(basedir, 'run')

DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://localhost/galaxyoj_dev')

# compile time limit in seconds
COMPILE_TIME_LIMIT = 10

# compiler options
COMPILER_CNT = 4
COMPILER_LIST = ["g++", "gcc", "fpc", "g++", "ghc"]
COMPILER_NAME_LIST = ["G++ 5.3.0", "GCC 5.3.0", "Free Pascal 3.0.0", "G++ C++11 5.3.0", "Haskell GHC 7.10.3"]
COMPILER_OPTION_LIST = [
        ["-o", "a.out", "-O2", "-Wall", "-lm", "--static", "-DONLINE_JUDGE"],
        ["-o", "a.out", "-O2", "-Wall", "-lm", "--static", "-std=c99", "-DONLINE_JUDGE"],
        ["-oa.out", "-O1", "-Co", "-Cr", "-Ct", "-Ci"],
        ["-o", "a.out", "-O2", "-Wall", "-lm", "-std=c++11", "--static", "-DONLINE_JUDGE"],
        ["-o", "a.out", "--make", "-O"],
]
COMPILER_FILEEXT_LIST = [".cpp", ".c", ".pas", ".cpp", ".hs"]
