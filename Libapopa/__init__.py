"""
Apopa TE+ LibApopa Framework.

This is framework for ApopaTE+'s applications.
.api module: Apis for system.
"""

import json
import Apps.ApopaPermissionManager as permissionManager
from typing import Any

class ConfigController:
    def __init__(self,config_path:str,configs:dict = {}):
        self.config_path = config_path
        self.configs = configs
    
    def loads(self):
        self.configs = json.load(open(self.config_path,"r"))
    
    def write(self,newConfig:dict):
        self.configs.update(newConfig)
        with open(self.config_path, 'w') as outfile:
            json.dump(self.configs, outfile)
    
    def change(self,configKey:str,configValue:str):
        self.configs[configKey] = configValue
        json.dump(self.configs,open(self.config_path,"w"))
    
    def get(self,configKey:str):
        return self.configs[configKey]

class FileController:
    def __init__(self,appname:str,fp:str,mode:str,buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None):
        """
        FileController of Apopa TE

        看到这里，你们可能想问，直接用python系统的open函数不就行了？为什么要套一层？
        因为 权限管理。你要知道 Apopa TE 是一个权限管理很严格的系统，在操作这方面上不允许出一点差错。
        所以，我们在这里套了一层，对文件的操作都必须通过这个类来完成。
        当然 Apopa TE 系统是不用这个的，这个是 Libapopa，面向开发者。
        否则你提交的py文件一定审核不通过。
        """
        self.buffer = open(fp,mode,buffering,encoding,errors,newline,closefd,opener)
        self.agreed = False
        self.appname = appname
    
    def write(self,data:str):
        if self.agreed:
            self.buffer.write(data)
            return True
        else:
            self.tryRequests()
            if self.agreed == False:
                return False
            
            self.buffer.write(data)
            return True
    
    def read(self):
        if self.agreed:
            return self.buffer.read()
        else:
            self.tryRequests()
            if self.agreed == False:
                return ""
            else:
                return self.buffer.read()
    
    def close(self):
        if self.agreed:
            self.buffer.close()
            return True
        else:
            self.tryRequests()
            if self.agreed == False:
                return False
            else:
                self.buffer.close()
                return True
    
    def tryRequests(self):
        pm = permissionManager.PermissionManager(self.appname,["I/O.Write","I/O.Read"])
        if pm.requestsUser():
            self.agreed = True
            return True
        else:
            return False