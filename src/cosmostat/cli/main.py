import pathlib

import click

from .chi_square_fit import chi_square_fit
from .chi_square_grid import chi_square_grid
from .describe_fit import describe_fit
from .describe_fit_legacy import describe_fit_legacy
from .info import info

COMMANDS = {
    "chi-square-fit": chi_square_fit,
    "chi-square-grid": chi_square_grid,
    "describe-fit": describe_fit,
    "describe-fit-legacy": describe_fit_legacy,
    "info": info,
}

file_dir = pathlib.Path(__file__).parent


class CLI(click.MultiCommand):
    """Gather the commands for different tasks."""

    def list_commands(self, ctx):
        """Return the list of commands."""
        return sorted(COMMANDS)

    def get_command(self, ctx, cmd_name: str):
        """Return the commands."""
        return COMMANDS.get(cmd_name, None)


@click.command(cls=CLI)
def main():
    """CLI of cosmostat library."""
    pass
