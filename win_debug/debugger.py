from ctypes import *
from win_debug.debug_def import *

kernel32 = windll.kernel32


class debugger():
    def __init__(self):
        pass

    def load(self, path_to_exe):
        # dwCreation flag determines how to create the process
        # set create_flags = CREATE_NEW_CONSOLE if you want
        # to see the calculator GUI
        creation_flags = DEBUG_PROCESS

        # instantiate the structs
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        # The following two options allow the started process
        # to be shown as a separate window. This also illustrates
        # how different settings in the STARTUPINFO struct can affect
        # the debuggee.
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        # Initialize the cb variable in the STARTUPINFO struct which
        # is just the size of the struct itself
        startupinfo.cb = sizeof(startupinfo)

        # kernel32.CreateProcessA if Python < 3
        if kernel32.CreateProcessW(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)
                                   ):
            print("[*] Successfully launched the process!")
            print("[*] PID: {}".format(process_information.dwProcessId))

        else:
            print("[*] Error 0x{0:08x}.".format(kernel32.GetLastError()))
