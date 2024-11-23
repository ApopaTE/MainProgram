"""
Apopa TE+ Libapopa Framework

This is Api module for applications.
"""

import user_api as uapi
from Apps import ApopaPermissionManager as perm
from Apps import AppGet as apt
from rich import print as rprint
from rich.live import Live
from rich.console import Console

class UserPermission:
    def __init__(self, name: str):
        if name == "usr":
            self.perm = "USER"
        elif self.perm == "spmnmgr":
            self.perm = "SUPERMANAGER"
    
    def getPerm(self):
        return self.perm
    
class SystemAPI:
    class User:
        def create(self, username: str, password: str, permission: UserPermission):
            uapi.register(username, password, permission.getPerm())
        
        def delete(self, username: str):
            uapi.delete(username)
        
        def check_pwd(self, username: str, password: str):
            return uapi.check(username, password)

        def have(self, username: str):
            return uapi.have(username)
        
        def getpermission(self, username: str):
            return uapi.getpermission(username)
    
    class RequirementsInstaller:
        def __init__(self, app_name: str):
            self.app_name = app_name
            
        def install_require(self, requires: list[str]):
            rprint(f"{self.app_name} 想要安装以下依赖：")
            for require in requires:
                rprint(f"[bold]{require}[/]")
            if input("是否同意？[y/N]").lower() == "y":
                with Live(console=Console()) as live:
                    for require in requires:
                        live.update(f"[green]正在下载[/][bold]{require}[/]")
                        apt.AppGet(require).only_download()
                        rprint(f"[green]已成功安装：{require}。[/]")
                    live.update(f"安装完毕。")
            else:
                rprint("您拒绝了请求。这些依赖将[bold]不会[/]被安装。")

    
    def __init__(self, app_name: str):
        self.perm = perm.PermissionManager(app_name, ["User:Control", "Requirement:Install"])
        self.requirements_installer = self.RequirementsInstaller(app_name)
        self.user = self.User()