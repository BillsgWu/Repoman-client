import dialogout,dialogin,dialogexist,dialoglog,dialogset,dialogsetextg,dialogsetextt
from requests import get,post
from lib import *
from datetime import datetime
from PyQt5.QtWidgets import QDialog,QMessageBox,QTableWidgetItem
from settings import *
from PyQt5.QtCore import pyqtSlot,QRect
class Din(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = dialogin.Ui_Dialogin()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        data = query(self,"goods")
        self.ui.type.addItems([i[1] for i in data])
    @pyqtSlot()
    def on_OK_clicked(self):
        good = query(self,"goods",name=self.ui.type.currentText())[0]
        good[4] += self.ui.count.value()
        modify(self,"goods",id=good[0],count=good[4])
        add(self,"log",type=0,good_id=good[0],count=self.ui.count.value())
        QMessageBox.information(self,"消息","更改成功")
        self.close()
class Dout(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = dialogout.Ui_Dialogin()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        data = query(self,"goods")
        self.ui.type.addItems([i[1] for i in data])
    @pyqtSlot()
    def on_OK_clicked(self):
        good = query(self,"goods",name=self.ui.type.currentText())[0]
        good[4] -= self.ui.count.value()
        if good[4] < 0:
            QMessageBox.critical(self,"错误","出库量大于库存量，数据库未做更改。")
            self.close()
            return
        modify(self,"goods",id=good[0],count=good[4])
        add(self,"log",type=1,good_id=good[0],count=self.ui.count.value())
        QMessageBox.information(self,"消息","更改成功")
        self.close()
class Dexist(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = dialogexist.Ui_Dialog()
        self.ui.setupUi(self)
        data = query(self,"goods")
        tags = {}
        for i in query(self,"tag"):
            tags[i[0]] = i
        limits = {}
        for i in query(self,"limit",False):
            limits[i[0]] = i
        for row in data:
            rowcount = self.ui.goods.rowCount()
            self.ui.goods.insertRow(rowcount)
            for i in range(len(row)):
                self.ui.goods.setItem(rowcount,i,QTableWidgetItem(str(row[i])))
            self.ui.goods.setItem(rowcount,2,QTableWidgetItem(tags[row[2]][1]))
            self.ui.goods.setItem(rowcount,5,QTableWidgetItem(str(limits[row[0]][1]) if row[0] in limits and limits[row[0]][1] != -1 else "UNLIMITED"))
            self.ui.goods.setItem(rowcount,6,QTableWidgetItem(str(limits[row[0]][2]) if row[0] in limits and limits[row[0]][2] != 2147483647 else "UNLIMITED"))
    def resizeEvent(self,event):
        size = event.size()
        size = [size.width(),size.height()]
        self.ui.goods.setGeometry(0,0,size[0],size[1])
class Dlog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = dialoglog.Ui_Dialog()
        self.ui.setupUi(self)
        self.goods = query(self,"goods")
        self.namemap = {i[0]:i[1] for i in self.goods}
        self.ui.good.addItems([""] + [i[1] for i in self.goods])
        self.ui.bquery.click()
    @pyqtSlot()
    def on_bquery_clicked(self):
        try:
            type = self.ui.type.currentText()
            if self.ui.date.text():
                date = datetime.strptime(self.ui.date.text(),"%Y/%m/%d").strftime("%Y/%m/%d")
            else:
                date = ""
            good = self.ui.good.currentText()
            count = self.ui.count.value()
        except Exception as e:
            QMessageBox.critical(self,"错误",str(e))
        for i in range(self.ui.log.rowCount()):
            self.ui.log.removeRow(0)
        dic = {}
        if type == "进库":
            dic["type"] = 0
        elif type == "出库":
            dic["type"] = 1
        if date:
            dic["date"] = date
        if good:
            for i in self.goods:
                if good == i[1]:
                    dic["good_id"] = i[0]
                    break
        if count:
            dic["count"] = count
        data = query(self,"log",**dic)
        if not data:
            QMessageBox.critical(self,"致命错误","查询失败")
            return
        for row in data:
            rowcount = self.ui.log.rowCount()
            self.ui.log.insertRow(rowcount)
            self.ui.log.setItem(rowcount,0,QTableWidgetItem(str(row[0])))
            self.ui.log.setItem(rowcount,1,QTableWidgetItem("入库" if str(row[1]) == "0" else "出库"))
            self.ui.log.setItem(rowcount,2,QTableWidgetItem(str(row[3])))
            try:
                self.ui.log.setItem(rowcount,3,QTableWidgetItem(self.namemap[row[2]]))
            except KeyError:
                self.ui.log.setItem(rowcount,3,QTableWidgetItem("(已删除的货品)"))
            self.ui.log.setItem(rowcount,4,QTableWidgetItem(str(row[4])))
    def resizeEvent(self,event):
        size = event.size()
        size = [size.width(),size.height()]
        width = (size[0] - 60) // 4
        self.ui.type.setGeometry(QRect(width * 0,size[1] - 30,width,30))
        self.ui.good.setGeometry(QRect(width * 1,size[1] - 30,width,30))
        self.ui.count.setGeometry(QRect(width * 2,size[1] - 30,width,30))
        self.ui.date.setGeometry(QRect(width * 3,size[1] - 30,width,30))
        self.ui.bquery.setGeometry(QRect(width * 4,size[1] - 30,60,30))
        self.ui.log.setGeometry(QRect(0,0,size[0],size[1] - 30))
class Dset(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.ui = dialogset.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.update()
    def update(self):
        self.ui.listgoods.clear()
        goods = query(self,"goods")
        self.ui.listgoods.addItems([i[1] for i in goods])
        self.ui.listtag.clear()
        tags = query(self,"tag")
        self.ui.listtag.addItems([i[1] for i in tags])
    @pyqtSlot()
    def on_bpgoods_clicked(self):
        Dsetextg(self).exec()
        self.update()
    @pyqtSlot()
    def on_bmgoods_clicked(self):
        ctext = self.ui.listgoods.currentItem()
        if ctext:
            ctext = ctext.text()
            good = query(self,"goods",name=ctext)[0]
            delete(self,"goods",id=good[0])
            self.update()
        else:
            QMessageBox.warning(self,"警告","请选择一项进行更改")
    @pyqtSlot()
    def on_bsgoods_clicked(self):
        ctext = self.ui.listgoods.currentItem()
        if ctext:
            ctext = ctext.text()
            good = query(self,"goods",name=ctext)[0]
            Dsetextg(self,{"id":good[0],"name":good[1],"tag":good[2],"company":good[3],"count":good[4]},"modify").exec()
            self.update()
        else:
            QMessageBox.warning(self,"警告","请选择一项进行更改")
    @pyqtSlot()
    def on_bptag_clicked(self):
        Dsetextt(self).exec()
        self.update()
    @pyqtSlot()
    def on_bmtag_clicked(self):
        ctext = self.ui.listtag.currentItem()
        if ctext:
            ctext = ctext.text()
            tag = query(self,"tag",name=ctext)[0]
            if query(self,"goods",False,tag_id=tag[0]):
                QMessageBox.critical(self,"致命错误","有剩余的货物已经打了这个标签")
                return
            delete(self,"tag",id=tag[0])
            self.update()
        else:
            QMessageBox.warning(self,"警告","请选择一项进行更改")
    @pyqtSlot()
    def on_bstag_clicked(self):
        ctext = self.ui.listtag.currentItem()
        if ctext:
            ctext = ctext.text()
            tag = query(self,"tag",name=ctext)[0]
            Dsetextt(self,{"id":tag[0],"name":tag[1]},"modify").exec()
            self.update()
        else:
            QMessageBox.warning(self,"警告","请选择一项进行更改")
class Dsetextg(QDialog):
    def __init__(self,parent=None,initvals={},type="add"):
        super().__init__(parent)
        self.ui = dialogsetextg.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.data = query(self,"tag")
        self.ui.tag.addItems([i[1] for i in self.data])
        if "name" in initvals:
            self.ui.name.setText(initvals["name"])
        if "tag" in initvals:
            for i in self.data:
                if i[0] == initvals["tag"]:
                    self.ui.tag.setCurrentIndex(self.data.index(i))
                    break
        if "company" in initvals:
            self.ui.company.setText(initvals["company"])
        if "count" in initvals:
            self.ui.count.setValue(initvals["count"])
        if "id" in initvals:
            self.id = initvals["id"]
        self.type = type
    @pyqtSlot()
    def on_ok_clicked(self):
        name = self.ui.name.text()
        tag = self.ui.tag.currentText()
        for i in self.data:
            if i[1] == tag:
                tagid = i[0]
                break
        company = self.ui.company.text()
        count = self.ui.count.value()
        llimit = int(self.ui.llimit.text()) if self.ui.llimit.text() else -1
        rlimit = int(self.ui.rlimit.text()) if self.ui.rlimit.text() else 2147483647
        if self.type == "add":
            add(self,"goods",name=name,tag_id=tagid,company=company,count=count)
            set_limit(self,query(self)[-1][0],llimit=llimit,rlimit=rlimit)
        elif self.type == "modify":
            modify(self,"goods",id=self.id,name=name,tag_id=tagid,company=company,count=count)
            set_limit(self,self.id,llimit=llimit,rlimit=rlimit)
        self.close()
class Dsetextt(QDialog):
    def __init__(self,parent=None,initvals={},type="add"):
        super().__init__(parent)
        self.ui = dialogsetextt.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        if "name" in initvals:
            self.ui.name.setText(initvals["name"])
        if "id" in initvals:
            self.id = initvals["id"]
        self.type = type
    @pyqtSlot()
    def on_ok_clicked(self):
        name = self.ui.name.text()
        if self.type == "add":
            add(self,"tag",name=name)
        elif self.type == "modify":
            modify(self,"tag",id=self.id,name=name)
        self.close()