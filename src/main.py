import typer
from typing_extensions import Annotated
from rich import print
from rich.console import Console
from rich.table import Table


app = typer.Typer()
console = Console()
err_console = Console(stderr=True)


@app.command()
def hello(fname: str, lname: str):
    typer.echo(f"hello {fname} {lname}")

@app.command()
def create_vpc(
    size: Annotated[int, typer.Option()],
    subnet_count: Annotated[int, typer.Option()],
    region: Annotated[str, typer.Option()],
    dry_run: Annotated[bool, typer.Option()] = False):

    if dry_run:
        print(f"[bold green]INFO[/bold green] [green]Nothing to see here. Just running dry...[/green]")
        return

    if size > 128:
        err_console.print(f"[bold red]ERROR[/bold red] [orange]VPC size cannot be larger than 128![/orange]")
    else:
        table = Table("Item", "Size", "Subnet_Count", "Region")
        table.add_row("VPC", str(size), str(subnet_count), region)
        console.print(table)


if __name__ == "__main__":
    app()