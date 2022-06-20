import subprocess


def notify(title, text, sound):
    command = '''
    on run argv 
        display notification (item 2 of argv) with title (item 1 of argv) sound name (item 3 of argv)
    end run
    '''

    subprocess.call(['osascript', '-e', command, title, text, sound])


if __name__ == '__main__':
    notify('Уведомление', "Не кусай яблоко", 'Blow')

# sound names: Basso, Blow, Bottle, Frog, Glass, Hero, Morse, Ping, Pop, Purr, Sosumi, Submarine, Tink
