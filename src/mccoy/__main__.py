"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """mccoy."""


if __name__ == "__main__":
    main(prog_name="mccoy")  # pragma: no cover
