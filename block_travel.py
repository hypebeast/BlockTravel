import sublime, sublime_plugin

class BlockTravelCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        cmd_args = {}

        if not ('cmd' in args):
            return

        if args['cmd'] == 'up':
            cmd = 'move'
            cmd_args = {'by': 'stops', 'forward': False, 'empty_line': True}
        elif args['cmd'] == 'down':
            cmd = 'move'
            cmd_args = {'by': 'stops', 'forward': True, 'empty_line': True}
        elif args['cmd'] == 'select_up':
            cmd = 'move'
            cmd_args = {'by': 'stops', 'forward': False, 'extend': True, 'empty_line': True}
        elif args['cmd'] == 'select_down':
            cmd = 'move'
            cmd_args = {'by': 'stops', 'forward': True, 'extend': True, 'empty_line': True}

        self.view.run_command(cmd, cmd_args)
