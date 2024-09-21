import subprocess
import os

full_path = os.path.abspath(__file__)
folder_name = os.path.basename(os.path.dirname(full_path))

if folder_name == 'work-with-data':
    dumpdata_path = r'dumpdata.ps1'
else:
    dumpdata_path = r'work-with-data\dumpdata.ps1'

powershell_path = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'

result = subprocess.run([powershell_path, '-File', dumpdata_path], capture_output=True, text=True)

if result.returncode == 0:
    print("Команда выполнена успешно.")
else:
    print("Произошла ошибка при выполнении команды.")
    print("Стандартный вывод (stdout):", result.stdout)
    print("Стандартный поток ошибок (stderr):", result.stderr)
