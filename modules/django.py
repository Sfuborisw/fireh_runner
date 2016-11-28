import os
import shlex
from argh import add_commands

class Plugin(object):

    config = None
    helper = None

    def __init__(self, config, helper):
        self.config = config
        self.helper = helper


    def setup_django_settings(self, project, variant):
        os.environ['DJANGO_SETTINGS_MODULE'] = project + '.settings'


    def django_admin(self, project=None, variant=None, *args):
        if len(args) == 1:
            args = shlex.split(args[0])

        self.helper.setup_virtualenv()

        project, variant = self.helper.setup_project_env(project, variant)
        os.chdir(os.path.join(self.config['work_dir'], project))

        binargs = ['django-admin'] + list(args)
        os.execvp(binargs[0], binargs)


    def django_manage(self, project=None, variant=None, *args):
        if len(args) == 1:
            args = shlex.split(args[0])

        self.helper.setup_virtualenv()

        project, variant = self.helper.setup_project_env(project, variant)
        os.chdir(os.path.join(self.config['work_dir'], project))

        binargs = ['python', 'manage.py'] + list(args)
        os.execvp(binargs[0], binargs)


    def django_script(self, project=None, variant=None, *args):
        if len(args) == 1:
            args = shlex.split(args[0])

        self.helper.setup_virtualenv()

        project, variant = self.helper.setup_project_env(project, variant)
        os.chdir(os.path.join(self.config['work_dir'], project))
        self.setup_django_settings(project, variant)

        binargs = ['python'] + list(args)
        os.execvp(binargs[0], binargs)


def initialize(config, argparser, helper):
    mod = Plugin(config, helper)
    add_commands(
        argparser,
        [
            mod.django_script,
        ])
