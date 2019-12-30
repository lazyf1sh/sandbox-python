import subprocess

encoding = 'latin1'
p = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

p.stdin.write("echo 123\n".encode())
print(p.stdout.read())
p.stdin.write("echo 345\n".encode())
p.stdin.close()
print(p.stdout.read())