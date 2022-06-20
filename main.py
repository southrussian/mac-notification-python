import subprocess


def notify(title, text, sound):
    command = '''
    on run argv 
        display notification (item 2 of argv) with title (item 1 of argv) sound name (item 3 of argv)
    end run
    '''

    subprocess.call(['osascript', '-e', command, title, text, sound])


if __name__ == '__main__':
    notify('Sample Title', f"This is the result {10}", 'Glass')
