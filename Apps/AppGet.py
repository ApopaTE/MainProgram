import requests,os
from rich import print as rprint
from rich.progress import Progress, SpinnerColumn

class AppGet:
    def __init__(self, app_name: str):
        self.app_name = app_name
    
    def download(self):
        print("AppGet - 软件安装器")
        rprint(f"即将开始安装：{self.app_name}。")
        url = f'https://apopa.mirror.mcfunfaz.fun/appget/{self.app_name}.py'
        try:
            response = requests.get(url, stream=True)
        except:
            rprint("[red]FALIED[/]: 无法正常访问服务器或该软件不存在。")
            return
        
        rprint("[green]下载中....[/]")
        content = response.text
        rprint("[green bold]下载成功！[/]")
        rprint("[green]写入中....[/]")
        open("./Apps/" + self.app_name + ".py", "w").write(content)
        rprint("[green bold]写入完成。[/]")

    
    def only_download(self):
        url = f'https://apopa.mirror.mcfunfaz.fun/appget/{self.app_name}.py'
        try:
            response = requests.get(url)
        except:
            rprint("[red]FALIED[/]: 无法正常下载 "+self.app_name+"。")
            return
        
        open("./Apps/"+self.app_name+".py", "w").write(response.text)
    
    def remove(self):
        app_name = self.app_name
        print("AppGet - 软件安装器")
        if not os.path.exists("./Apps/"+ app_name + ".py"):
            rprint("[bold red]ERR: [/]您没有安装该软件包。")
            return
        rprint("即将开始[bold red]卸载[/]: " + self.app_name + "。")
        really = input("确认卸载？[y/N]: ").lower() == "y"
        if really:
            rprint("[green]卸载中....[/]")
            os.remove("./Apps/"+ app_name + ".py")
            rprint("[bold green]成功卸载。[/]")
        else:
            rprint("[green]取消了本次卸载。[/]")
        return
    
    def show_list(self):
        print("AppGet - 软件安装器")
        print("您的电脑安装了如下软件包：")
        for app in os.listdir("./Apps"):
            if os.path.isfile("./Apps/" + app):
                rprint(f"[bold]{app.replace(".py", "")}[/]")
        return
    
    
def eval(command: str, params: list[str]):
    if command == "apt":
        if len(params) != 0:
            if params [0] == "install":
                if len(params) != 2:
                    print("AppGet: 无效参数。")
                else:
                    apt = AppGet(params [1])
                    apt.download()
            elif params [0] == "remove":
                if len(params) != 2:
                    print("AppGet: 无效参数")
                else:
                    apt = AppGet(params [1])
                    apt.remove()
            elif params [0] == "list":
                apt = AppGet("")
                apt.show_list()
            else:
                print("AppGet: 无效选项。找不到 " + params [0] + "。")
        else:
            print("AppGet: 请提供参数。")
    return "not use"