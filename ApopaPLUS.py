import Core.UserController as user
from Core.CallableController import *
from getpass import getpass as pwdg
import subprocess,sys,io,importlib,os
from typing import Any
import Apps.AppGet as apt
from rich import print as rprint

try:
    import requests
except ModuleNotFoundError:
    print("正在安装 Requests...")
    subprocess.run([sys.executable, "-m", "pip", "install", "requests"])
    import requests
    clear()
import os

print("欢迎回到 Apopa TE+!")
print("")
if not len(os.listdir("./Core/Users/")) != 0:
    clear()
    print("Apopa TE+ 安装向导")
    print("")
    rprint("[green]欢迎使用 Apopa TE+ 安装向导![/]")
    rprint("[green]>> 按回车键继续[/]")
    input()
    clear()
    print("Apopa TE+ 安装向导")
    print("")
    print("您账户的用户名：")
    username = input(">> ")
    print("您账户的密码(不会显示)：")
    password = pwdg(">> ")
    user.register(username, password, user.SUPERMANAGER)
    rprint("[green]注册成功。[/]")
    clear()
    print("Apopa TE+ 安装向导")
    print("")
    rprint("[green]> 请求 Apopa Mirror AppGet 服务器[/]")
    try:
        if not requests.get("https://apopa.mirror.mcfunfaz.fun/").status_code == 200:
            rprint("[bold red]ERR: 请求失败，请检查您的网络连接。[/]")
            exit(1)
    except requests.exceptions.ConnectionError:
        print("[bold red]ERR: 请求失败，请检查您的网络连接。[/]")
        exit(1)
    rprint("[bold green]网络可用。[/]")
    rprint("[green]>> 按回车键重新启动 Apopa PLUS[/]")
    exit()

def cls():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def ci(command:str) -> tuple[str,list[str]]:
    """
    Command Interpeter
    :param Command
    :return tuple(str,list[str])
    """
    params = command.replace(command.split(" ")[0]," ").split(" ")
    for i in range(len(params)):
        try:
            params.remove("")
        except:
            break
    return (command.split(" ")[0],params)

def var(vars:dict,name:str, value:Any):
    vars.update({name:value})

def gbk_to_utf8(source_file, target_file):
    with io.open(source_file, 'r', encoding='gbk') as file:
        content = file.read()
        with io.open(target_file, 'w', encoding='utf-8') as new_file:
            new_file.write(content)


def mkdir(path):
    os.makedirs(path, exist_ok=True)
    print(f"创建目录: {path}")

def main(username:str):
    cls()
    print("Apopa Terminal Emulator+")
    print("Version [2.0.1.00001] PLUS")
    print("")
    try:
        vars = {}
        showparam = False
        canBrowseDadSystem = False
        nowDirectory = "./"
        lastDirectory = "./"
    except Exception as ex:
        rprint("[red]panic: "+str(ex)+"[/]")
        exit()
    while True:
        try:
            rprint(f"[green]{username}[/]@apopa: [green]{nowDirectory}[/]>>   ", end="")
            cmd = input()
            ct:tuple[str,list[str]] = ci(cmd)
        except Exception as ex:
            rprint("[bold red]运行时错误 (Runtime Error):\n\n"+str(ex)+"\n\n请联系作者。[/]")
        except KeyboardInterrupt:
            print("\n再见。")
            exit()
        else:
            try:
                command = ct [0].lower()
                param = ct [1]

                if showparam:
                    print("命令 : "+command)
                    print("参数 : "+str(param))
                
                if command == "help":
                    rprint("[green]Apopa Terminal Emulator 帮助[/]")
                    print("")
                    rprint("[bold]命令 :[/]")
                    print("cls: 清除屏幕")
                    print("exit: 退出终端")
                    print("help: 显示帮助")
                    print("#: 注释符")
                    print("echo: 输出内容。可配合 > 使用于编辑文件。")
                    print(">: 重定向符。可配合 echo 使用。")
                    print("var: 变量定义符。格式：var [name] [value(可空)]")
                    print("dd: 类似于 Linux 的 dd 命令。用法：dd InputFile OutputFile")
                    print("reboot: 重新加载 Apopa 终端")
                    print("apt: AppGet 应用程序管理器")
                    print("cd: 更改路径")
                    print("mkdir: 创建文件夹")
                    print("ls: 列出当前目录下的文件")
                    print("apopaver: 显示 Apopa+ 终端版本")
                    print("deluser: 删除用户")
                    print("cat: 查看文件")
                    print("")
                elif command == "exit":
                    print("再见。")
                    break
                elif command  == "cls":
                    cls()
                elif command == "echo":
                    if len(param) == 1:
                        print(param[0])
                    elif param [1] == ">":
                        with open(param[2],"w") as f:
                            f.write(param[0])
                            print("已填充 1 项到文件 "+param[2]+" 。")
                    else:
                        print("echo: 无效的参数。")
                elif command == "#":
                    pass
                elif command == ">":
                    print(">: 无效的 I/O 操作。")
                elif command == "var":
                    if param [0] != " ":
                        try:
                            var(vars,param[0],param[1])
                        except BaseException:
                            var(vars,param[0],"")
                        print(f"var: 已定义变量 {param[0]} 为 {param[1]}")
                    else:
                        print("var: 无效的参数。")
                elif command == "dd":
                    if len(param) == 2:
                        with open(param[1],"wb") as f:
                            f.write(open(param[0], "r").read().encode("utf-8"))
                        print("已填充 1 项到文件 "+param[2]+" 。")
                    else:
                        print("dd: 无效的参数。")
                elif command == "showparam":
                    showparam = True
                elif command == "reboot":
                    try:
                        os.system(f'"{__file__}"')
                    except:
                        exit()
                elif command == "cd":
                    try:
                        if not os.path.isabs(param[0]) and param [0] != ".." or param [0] != ".":
                            lastDirectory = nowDirectory
                            nowDirectory = os.path.join(nowDirectory, param[0])
                        elif param [0] == "..":
                            lastDirectory = nowDirectory
                            nowDirectory = os.path.dirname(nowDirectory)
                    except:
                        print("cd: 无效的参数。")
                    else:
                        if not os.path.exists(nowDirectory) or not os.path.isdir(nowDirectory):
                            print("cd: 没有那个文件或目录")
                            nowDirectory = lastDirectory
                elif "<" in cmd:
                    goto = cmd.replace("<","").split(" ")
                    if len(goto) == 2:
                        if goto [0] in vars.keys():
                            vars [goto[0]] = goto [1]
                            print("已将变量 "+goto[0]+" 赋值为 "+goto[1])
                        else:
                            print("未找到变量 "+goto[0]+"。")
                    else:
                        print("无效的参数。")
                elif command == "mkdir":
                    try:
                        mkdir(param[0])
                    except:
                        print("mkdir: 无效的参数。")
                elif command == "ls":
                    for file in os.listdir(nowDirectory):
                        if os.path.isfile(file):
                            rprint("[blue]文件 "+file+"[/]")
                        else:
                            rprint("[blue]目录 "+file+"[/]")
                elif command == "apopaver":
                    print("Apopa+ 版本：V2.0.1.PLUS.00001")
                elif command == "deluser":
                    if user.have(param[0]):
                        if user.getpermission(username) == user.SUPERMANAGER:
                            print("deluser: 成功删除 "+param[0]+"。")
                            user.delete(param [0])
                        else:
                            print("deluser: Permission denied.")
                    else:
                        print("deluser: 用户不存在。")
                elif command == "adduser":
                    if user.have(param[0]):
                        print("adduser: 该用户已存在")
                    else:
                        if len(param) == 3:
                            if user.getpermission(username) == user.SUPERMANAGER:
                                user.register(param [0], param [1], param [2])
                            else:
                                print("adduser: Permission denied.")
                        else:
                            print("adduser: Params not vaild.")
                elif command == "cat":
                    file = param [0]
                    if not os.path.exists(file):
                        print("cat: 没有那个文件")
                        continue
                    print(open(file, "r").read())
                else:
                    successRun = False
                    for app in os.listdir("./Apps"):
                        if app.endswith(".py"):
                            # 使用 importlib.util.spec_from_file_location() 和 importlib.util.module_from_spec() 动态加载模块
                            """
                            spec = importlib.util.spec_from_file_location("Apps." + app, os.path.join("./Apps", app))
                            module = importlib.util.module_from_spec(spec) # type: ignore
                            spec.loader.exec_module(module) # type: ignore
                            """
                            # 下面跑不了就换上面的
                            module = importlib.import_module("Apps." + app.replace(".py",""))
                            #type ignore 主要是为了过类型检测

                            returnValue = module.eval(command, param)
                            if returnValue != "not use":
                                successRun = True

                            # 你们可能觉得这是个奇怪的写法，但是因为我们的 Apopa 需要有扩展性，不需要 eval 的可以直接用以下格式：
                            # def eval(command:str,param:list[str]):return "not use";
                            # 这样，Apopa 虽然执行了，但是执行了个寂寞。
                            # 还有他会判断返回值，这样就不会出现调用成功了但还是提示 "没有找到命令：xxx"

                    if not successRun:
                        print("没有找到命令："+command)
            except Exception as ex:
                print("运行时错误 (Runtime Error):\n"+ex.__str__()+"\n请联系作者。")

while True:
    print("您账户的用户名：")
    username = input(">> ")
    print("您账户的密码(不会显示)：")
    password = pwdg(">> ")
    if user.check(username, password):
        clear()
        rprint("[bold green]欢迎回来 "+username+"![/]")
        main(username)
        break
    else:
        rprint("[bold red]用户名或密码错误。[/]")