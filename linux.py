import sys;
import ctypes;

SYS_write = 1;
STDOUT_FILENO = 1;


def main() -> int:
    libc = ctypes.CDLL(None);

    libc.syscall.argtypes = [
        ctypes.c_long,
        ctypes.c_long,
        ctypes.c_void_p,
        ctypes.c_long,
    ];
    libc.syscall.restype = ctypes.c_long;

    hello: ctypes.Array[ctypes.c_ubyte] = (ctypes.c_ubyte * 14)(104,101,108,108,111,44,32,119,111,114,108,100,10,0);

    i = 0;
    while 1:
        if hello[i] == 0:
            break;
        libc.syscall(SYS_write, STDOUT_FILENO, ctypes.byref(hello, i), 1);
        i += 1;

    return 0;


if __name__ == "__main__":
    sys.exit(main());
