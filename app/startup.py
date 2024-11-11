import os
import sys

def add_to_startup():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\Windows\Start Menu\Programs\Startup')
    script_name = os.path.basename(sys.argv[0])
    shortcut_path = os.path.join(startup_folder, f"{script_name}.lnk")
    
    if not os.path.exists(shortcut_path):
        import win32com.client

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = sys.executable
        shortcut.Arguments = f'"{sys.argv[0]}"'
        shortcut.WorkingDirectory = os.path.dirname(os.path.abspath(sys.argv[0]))
        shortcut.save()
        print("Приложение добавлено в автозапуск.")
    else:
        print("Приложение уже добавлено в автозапуск.")
