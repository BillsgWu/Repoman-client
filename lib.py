from settings import *
from requests import get,post
from PyQt5.QtWidgets import QMessageBox

def decodedata(data:str):
    return eval(data)

def add(window,db="goods",tip=True,**data):
    res = post(f"{SCHEME}://{SERVERHOST}:{SERVERPORT}/api/add",data,params={"db":db}).json()
    if res["status"] != "OK":
        if tip:
            QMessageBox.critical(window,"致命错误","添加失败，错误代号：%s"%res["status"])
            window.close()
        return
def query(window,db="goods",tip=True,**data):
    res = get(f"{SCHEME}://{SERVERHOST}:{SERVERPORT}/api/query",{"db":db,**data}).json()
    if res["status"] != "OK":
        if tip:
            QMessageBox.critical(window,"致命错误","查询失败，错误代号：%s"%res["status"])
            window.close()
        return []
    return decodedata(res["data"])
def delete(window,db="goods",tip=True,id=...):
    res = get(f"{SCHEME}://{SERVERHOST}:{SERVERPORT}/api/delete",{"db":db,"id":id}).json()
    if res["status"] != "OK":
        if tip:
            QMessageBox.critical(window,"致命错误","查询失败，错误代号：%s"%res["status"])
            window.close()
        return
def modify(window,db="goods",tip=True,**data):
    res = post(f"{SCHEME}://{SERVERHOST}:{SERVERPORT}/api/modify",data,params={"db":db}).json()
    if res["status"] != "OK":
        if tip:
            QMessageBox.critical(window,"致命错误","添加失败，错误代号：%s"%res["status"])
            window.close()
        return
def set_limit(window,id,tip=True,llimit=-1,rlimit=2147483647):
    res = post(f"{SCHEME}://{SERVERHOST}:{SERVERPORT}/api/setlimit",{"id":id,"llimit":llimit,"rlimit":rlimit}).json()
    if res["status"] != "OK":
        if tip:
            QMessageBox.critical(window,"致命错误","越界设置失败，错误代号：%s"%res["status"])
            window.close()
        return