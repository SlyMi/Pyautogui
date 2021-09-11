from pywinauto import mouse
from pywinauto.application import Application

def_AppName = "ITE_WinECU_I2EC_v2.2.15.exe"
main_child_window = ""


def open_app(self=None) -> main_child_window:
    app = Application(backend="uia").start(def_AppName)
    win_main_Dialog = app.window(class_name='TForm1')
    return win_main_Dialog


def open_stream_ITE(win_main_Dialog):
    child = win_main_Dialog.window(class_name='TTabControl')
    win_main_Dialog.draw_outline(colour='red')
    child = win_main_Dialog.child_window(class_name='TTabControl')
    # child.print_control_identifiers(depth=None, filename=None)
    child.__getattribute__("Edit3").type_keys('^a').type_keys('6E', with_spaces=True)
    child.__getattribute__("Edit2").type_keys('^a').type_keys('6F', with_spaces=True)
    child.__getattribute__("Set").click_input()
    win_main = win_main_Dialog.rectangle()
    rec = child.__getattribute__("Slider").rectangle()
    cy = int((rec.top + rec.bottom) / 2)
    refreshx = int((rec.right + win_main.right) / 2)
    mouse.click(button='left', coords=(refreshx, cy))


def ec_log(win_main_Dialog):
    try:
        menu = win_main_Dialog.child_window(title="Application", auto_id="MenuBar", control_type="MenuBar")
    except Exception as e:
        print("env is not EN")
    else:
        menu = win_main_Dialog.child_window(title="应用程序", auto_id="MenuBar", control_type="MenuBar")

    log_window = menu.child_window(title="Log", control_type="MenuItem")
    rec = log_window.rectangle()
    cx = int((rec.left + rec.right) / 2)
    cy = int((rec.top + rec.bottom) / 2)
    item_h = int(rec.bottom - rec.top)
    mouse.click(button='left', coords=(cx, cy))
    mouse.click(button='left', coords=(cx, cy + item_h))
    return menu


def quit_EC(menu):
    quit = menu.child_window(title="Quit", control_type="MenuItem")
    rec = quit.rectangle()
    cx = int((rec.left + rec.right) / 2)
    cy = int((rec.top + rec.bottom) / 2)
    mouse.click(button='left', coords=(cx, cy))


def main():
    win_main_Dialog = open_app()
    open_stream_ITE(win_main_Dialog)
    menu = ec_log(win_main_Dialog)
    quit_EC(menu)


if __name__ == '__main__':
    main()
