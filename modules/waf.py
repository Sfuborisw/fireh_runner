"""Waf module.

Website: http://waf.io
"""
import os

def waf(loader, variant=None, *args):
    """Build project."""
    loader.setup_project_env(variant=variant)
    loader.setup_virtualenv()

    binargs = loader.get_binargs('waf', *args)

    os.execvp(binargs[0], binargs)


commands = (waf,)
