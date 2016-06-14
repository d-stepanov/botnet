import os
import socket
from ...signals import on_exception
from .. import BaseResponder


def random_line(filename):
    """Gets a random line from file."""
    return random.choice(list(open(filename)))


class Toast(BaseResponder):
    config_namespace = 'botnet'
    config_name = 'toast'

    def get_all_commands(self):
        rw = super(Toast, self).get_all_commands()
        try:
            for command in self.config['module_config'][self.config_namespace][self.config_name].keys():
                rw.append(command)
        except:
            pass
        return rw

    def handle_privmsg(self, msg):
        if self.is_command(msg):
            command = (str(msg).split('!')[-1])
            print('got command: %s' % command)
            self.respond(msg, command + ' ok!')

    def dudos(self, host = '127.0.0.1', port = 8080, times = 1000):
        for x in range(times):
            sock = socket.socket()
            sock.connect((host, port))
            sock.send(b'hello')

mod = Toast
