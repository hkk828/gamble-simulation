import subprocess

files = subprocess.run(['ls', 'utils'], capture_output=True, text=True)
files = files.stdout.split()

__all__ = [file.rstrip('.py') for file in files if not file.startswith('__')]