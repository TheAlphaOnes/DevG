from mod.MyConsole import terminal
import json

scheam = {
    "name":"",
    "description":"",
    "status":"",
    "command":{
        "build":"",
        "run":"",
        "test":"",
        
    },
    "dependency":{
      "installer-command":""  ,
      "packages":[]
    },
    "todo":{
        "done":[],
        "left":[]
    }
}


installer_commnads = {
    "npm":"npm install <pkg>",
    "pnpm":"pnpn add <pkg>",
    "yarn":"yarn add <pkg>",
    "pip":"pip install <pkg>",
    "go":"go get <pkg>",
}

def create_devg_file():
    name = terminal.ask("[green]Enter Your Project Name[/green]")
    disc = terminal.ask("[green]Description[/green]")
    buildC = terminal.ask("[green]build command[/green]")
    runC = terminal.ask("[green]run command[/green]")
    testC = terminal.ask("[green]test command[/green]")
    
    pkg_manager = terminal.mcq(list(installer_commnads.keys())+['custom'],"what pkg manager to use?")
    if pkg_manager == "custom":
        terminal.show('feed the command and replace the lib name with "<pkg>"')
        pkg_command = terminal.ask("[green]installer command[/green]")
    else:
        pkg_command = installer_commnads.get(pkg_manager)
    
    scheam["name"] = name
    scheam["description"] = disc
    scheam["command"]['build'] = buildC
    scheam["command"]['run'] = runC
    scheam["command"]['test'] = testC
    scheam["dependency"]['installer-command'] = pkg_command
    
    json.dump(scheam,open("devg.json","w",encoding="utf-8"),indent=4)
    
    
def update_devg_file():
    scheam_old = json.load(open("devg.json","r",encoding="utf-8"))
    
    name = terminal.ask("[green]Enter Your Project Name[/green]",default=scheam_old['name'])
    disc = terminal.ask("[green]Description[/green]",default=scheam_old['description'])
    buildC = terminal.ask("[green]build command[/green]",default=scheam_old["command"]['build'])
    runC = terminal.ask("[green]run command[/green]",default=scheam_old["command"]['run'])
    testC = terminal.ask("[green]test command[/green]",default=scheam_old["command"]['test'])
    
    pkg_manager = terminal.mcq(list(installer_commnads.keys())+['custom'],"what pkg manager to use?")
    if pkg_manager == "custom":
        terminal.show('feed the command and replace the lib name with "<pkg>"')
        pkg_command = terminal.ask("[green]installer command[/green]",default=scheam_old["dependency"]['installer-command'])
    else:
        pkg_command = installer_commnads.get(pkg_manager)
    
    scheam_old["name"] = name
    scheam_old["description"] = disc
    scheam_old["command"]['build'] = buildC
    scheam_old["command"]['run'] = runC
    scheam_old["command"]['test'] = testC
    scheam_old["dependency"]['installer-command'] = pkg_command
    
    json.dump(scheam_old,open("devg.json","w",encoding="utf-8"),indent=4)