import sys;
import ctypes;


def main() -> int:
    kernel32 = ctypes.WinDLL("kernel32");

    kernel32.GetStdHandle.argtypes = [ctypes.c_long];
    kernel32.GetStdHandle.restype = ctypes.c_void_p;

    kernel32.WriteFile.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_ulong,
        ctypes.POINTER(ctypes.c_ulong),
        ctypes.c_void_p
    ];
    kernel32.WriteFile.restype = ctypes.c_int;

    stdout = kernel32.GetStdHandle(-11);

    hello = (ctypes.c_ubyte * 14)(
        104,101,108,108,111,44,32,119,111,114,108,100,10,0
    );

    written = ctypes.c_ulong(0);

    i = 0;
    while 1:
        if hello[i] == 0:
            break;
        kernel32.WriteFile(
            stdout,
            ctypes.byref(hello, i),
            1,
            ctypes.byref(written),
            None
        );
        i += 1;

    return 0;

if __name__ == "__main__":
    sys.exit(main());
