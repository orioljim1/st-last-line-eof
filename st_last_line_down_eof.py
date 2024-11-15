import sublime
import sublime_plugin

class SmartDownCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cursor = self.view.sel()[0]
        cursor_row, _ = self.view.rowcol(cursor.begin())
        last_row = self.view.rowcol(self.view.size())[0]
        if cursor_row == last_row:
            self.view.run_command("move_to", {"to": "eof"})
        else:
            self.view.run_command("move", {"by": "lines", "forward": True})

class SmartDownListener(sublime_plugin.EventListener):
    def on_text_command(self, view, command_name, args):
        if command_name == "move" and args == {"by": "lines", "forward": True}:
            return ("smart_down", {})