import typer
from pathlib import Path

from mod.compressor import *
from mod.MyConsole import terminal
from mod.create_devg import create_devg_file
app = typer.Typer()

@app.command("scan")
def scan(dir:Path):
    if dir.is_dir() :
        name_temp = terminal.ask("[green]Enter Your template Name[/green]")
        resp = terminal.mcq(['asd',"asdas"],"ter,asd??")
        create_devg_file()
        print(resp)
    else:
        terminal.error(f"[yellow]{dir}[/yellow] is Not a Directory, Process Aborted")

    

@app.command("init")
def scan(temp:str,name:str):
    print(temp,name)