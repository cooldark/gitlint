import subprocess
from locale import getpreferredencoding
DEFAULT_ENCODING = getpreferredencoding() or "UTF-8"


class ShResult:

    exit_code = None
    stdout = None
    stderr = None
    full_cmd = None

    def __init__(self, stdout, stderr='', exitcode=0, args=[]):
        self.exit_code = exitcode
        self.stdout = stdout
        self.stderr = stderr
        self.full_cmd = ' '.join(args)

    def __str__(self):
        return self.stdout

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return str(self) != str(other)


def gitlint(*command_parts, **kwargs):
    args = ['gitlint'] + list(command_parts)
    return _exec(*args, **kwargs)


def echo(*command_parts, **kwargs):
    args = ['echo'] + list(command_parts)
    return _exec(*args, **kwargs)


def touch(*command_parts, **kwargs):
    args = ['touch'] + list(command_parts)
    return _exec(*args, **kwargs)


def rm(*command_parts, **kwargs):
    args = ['rm'] + list(command_parts)
    return _exec(*args, **kwargs)


def git(*command_parts, **kwargs):
    args = ['git'] + list(command_parts)
    return _exec(*args, **kwargs)


def _exec(*args, **kwargs):
    pipe = subprocess.PIPE
    popen_kwargs = {'stdout': pipe, 'stderr': pipe, 'shell': False}
    if '_cwd' in kwargs:
        popen_kwargs['cwd'] = kwargs['_cwd']
    p = subprocess.Popen(args, **popen_kwargs)
    result = p.communicate()
    if p.returncode == 0:
        return result[0].decode(DEFAULT_ENCODING)
    stdout = result[0].decode(DEFAULT_ENCODING)
    stderr = result[1].decode(DEFAULT_ENCODING)
    return ShResult(stdout, stderr, p.returncode, args)
