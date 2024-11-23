global commandmode
commandmode = False

try:
    import tkinter as tk
    import tkinter.messagebox as msgbox
except ModuleNotFoundError:
    commandmode = True

from rich import print as rprint

class PermissionManager:
    def __init__(self,application:str,permission:list[str]):
        self.application = application
        self.permission = permission
        self.agreed = False
    
    def requestsUser(self):
        if not commandmode:
            window = tk.Tk() #type: ignore
            window.title("Apopa TE 权限请求")
            window.geometry("500x500")

            # 创建提示标签和权限列表
            label = tk.Label(window, text=f"{self.application} 请求以下权限：", font=("Microsoft YaHei",24)) #type: ignore
            label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
            permission_list = tk.Listbox(window, height=5, width=50) #type: ignore
            for permission in self.permission:
                permission_list.insert(tk.END, permission) #type: ignore
                
            permission_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

            # 创建同意和拒绝按钮
            agree_button = tk.Button(window, text="同意", command=lambda: self.agree(window)) #type: ignore
            agree_button.grid(row=2, column=0, padx=10, pady=10)
            
            disagree_button = tk.Button(window, text="拒绝", command=lambda: self.disagree(window)) #type: ignore
            disagree_button.grid(row=2, column=1, padx=10, pady=10)

            window.mainloop()

            return self.agreed
        else:
            rprint(f"[green]{self.application} 请求以下权限：[/]")
            for permission in self.permission:
                rprint(f"[bold blue]{permission}[/]")
            return input("是否同意？(y/N)").lower() == "y"
    
    def agree(self,window):
        msgbox.showinfo("权限请求结果","程序已获得请求的所有权限。") #type: ignore
        window.destroy()
        self.agreed = True

    def disagree(self,window):
        msgbox.showinfo("权限请求结果","程序被拒绝获得请求的所有权限。") #type: ignore
        window.destroy()
        self.agreed = False

def eval(command:str,param:list[str]):
    return "not use"