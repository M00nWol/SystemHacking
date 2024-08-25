import sys
from ctypes import *

def usage():
    print("\n # Get Function Address v1.0 by M00nWol # \n")
    print("Usage: %s [dll] [proc]" % sys.argv[0])
    sys.exit()

if len(sys.argv) < 3:
    usage()

target_dll = sys.argv[1]
target_function = sys.argv[2].encode('utf-8')  # 함수명을 바이트 문자열로 변환

dll = windll.LoadLibrary(target_dll)
kernel32 = windll.kernel32

# GetProcAddress의 인수 타입을 명시적으로 지정
kernel32.GetProcAddress.argtypes = [c_void_p, c_char_p]
kernel32.GetProcAddress.restype = c_void_p

# dll._handle을 c_void_p로 캐스팅하여 전달
function = kernel32.GetProcAddress(c_void_p(dll._handle), target_function)

if function:
    print("[##] Find Address %s(%s): 0x%08X" % (target_dll, sys.argv[2], cast(function, c_void_p).value))
else:
    print("[!!] Function %s not found in %s" % (sys.argv[2], target_dll))
