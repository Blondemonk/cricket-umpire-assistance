import subprocess

file1 = "object-detector/ballTracking.py"
path = "vid.mp4"
action = "0"

print "Switching to virtualenv"
# subprocess.call(["workon", "cv"])
python_bin = "/home/mark/.virtualenvs/cua/bin/python"
# path to the script that must run under the virtualenv

print "Calling ballTracking.py"
subprocess.call([python_bin, file1, "-v", path, "-a", action])

file2 = "object-detector/3d.py"
print "Calling 3d.py"
subprocess.call(["python", file2])
