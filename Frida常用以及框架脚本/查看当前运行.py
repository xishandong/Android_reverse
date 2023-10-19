import frida

rdev = frida.get_remote_device()
print(rdev)

processes = rdev.enumerate_processes()
for process in processes:
    print(process)

front_app = rdev.get_frontmost_application()
print(front_app)