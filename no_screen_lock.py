print('While this window is open, screen will not lock')
import ctypes, time
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
time.sleep(4294967)
