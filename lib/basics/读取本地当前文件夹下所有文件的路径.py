import os
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.basename(os.path.realpath(__file__)))
print()
def file_path(file_dir):
	for root, dirs, files in os.walk(file_dir):
		return root, files
file_dir = os.path.dirname(os.path.realpath(__file__))
a = file_path(file_dir)
print(str(a[0]))
print(a[1])
print()
for i in range(len(a[1]) - 1):
	print(str(a[0] + '\\' + a[1][i]))

