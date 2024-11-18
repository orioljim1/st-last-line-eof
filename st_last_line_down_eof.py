import sublime
import sublime_plugin

class SmartVerticalNavigationCommand(sublime_plugin.TextCommand):
    def run(self, edit, direction="down"):
        cursor = self.view.sel()[0]
        cursor_row, _ = self.view.rowcol(cursor.begin())
        
        last_row = self.view.rowcol(self.view.size())[0]
        
        if direction == "down" and cursor_row == last_row:
            self.view.run_command("move_to", {"to": "eof"})
        elif direction == "up" and cursor_row == 0:
            self.view.run_command("move_to", {"to": "bof"})
        else:
            self.view.run_command("move", {
                "by": "lines",
                "forward": direction == "down"
            })

class SmartNavigationListener(sublime_plugin.EventListener):
    def on_text_command(self, view, command_name, args):
        if command_name == "move":
            if args == {"by": "lines", "forward": True}:
                return ("smart_vertical_navigation", {"direction": "down"})
            elif args == {"by": "lines", "forward": False}:
                return ("smart_vertical_navigation", {"direction": "up"})