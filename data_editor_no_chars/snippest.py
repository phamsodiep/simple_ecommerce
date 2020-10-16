#".QFrame{border: 1px solid black;}"

# import sys
# from PyQt5 import QtWidgets

# app = QtWidgets.QApplication(sys.argv)

# screen = app.primaryScreen()
# print('Screen: %s' % screen.name())
# size = screen.size()
# print('Size: %d x %d' % (size.width(), size.height()))
# rect = screen.availableGeometry()
# print('Available: %d x %d' % (rect.width(), rect.height()))


#https://stackoverflow.com/questions/39488901/change-qsortfilterproxymodel-behaviour-for-multiple-column-filtering


# STEPS
# 0.
#    python -m PyQt5.uic.pyuic -x data_editor_no_chars.ui -o aquarium.py
#
# 1. Copy
#       snippest def changeState(self, state):
#       snippest import urllib.request
#
# 2. Connect
#       self.actionSave.triggered.connect(MainWindow.saveAll)
#       self.actionSave.triggered.connect(self.saveAll)
#
# 3. QTableView: QtWidgets.QTableView(self.mainWidgetContents)
#    self.productData = QtWidgets.QTableView(self.mainWidgetContents)
#                               ProductDataTableView(self.mainWidgetContents)



import urllib.request
import shutil
import sys
import os
from PyQt5.QtSql import *







    def changeState(self, state):
        # self.metaData.hide() # Remove for no_chars version
        self.productData.hide()
        if state == 0:
            self.state = 1
            self.detailsArea.raise_()
        else:
            if state == 1:
                self.productData.show()
                #self.mainArea.setGeometry(QtCore.QRect(260, 10, 574, 651))
                #self.mainWidgetContents.setGeometry(QtCore.QRect(0, 0, 572, 649))
            elif state == 2:
                self.metaData.show()
                self.categoryArea.raise_()
            self.state = state

    def switchDataViewInit(self):
        self.categories.selectionModel().clearSelection()
        self.changeState(0)

    def switchDataViewCat(self, cat):
        self.changeState(1)
        if not(hasattr(self, "productsModel")):
            srcModel = QSqlTableModel(None, self.db)
            proxyModel = QtCore.QSortFilterProxyModel(None)

            #self.productsModel.setTable("products")
            #self.productsModel.select()
            #self.productsModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

            srcModel.setTable("products")
            srcModel.select()
            srcModel.setEditStrategy(QSqlTableModel.OnManualSubmit)

            proxyModel.setSourceModel(srcModel)
            self.productsModel = proxyModel

            self.productData.setModel(self.productsModel)
            self.productData.selectionModel().selectionChanged.connect(self.changeProductData)
            self.productData.setItemDelegateForColumn(0, ReadOnlyDelegate(self.productData))
            for i in [1, 2] + list(range(7, 13)):
                self.productData.hideColumn(i)

            self.productsModel.setFilterKeyColumn(1)
            #self.productsModel.sort(2, QtCore.Qt.DescendingOrder)
            #self.productsModel.sort(0, QtCore.Qt.DescendingOrder) # QtCore.Qt.AscendingOrder
            
            #self.productsModel.sort(0, QtCore.Qt.AscendingOrder)
            #self.productData.setItemDelegateForColumn(0, ReadOnlyDelegate(self.productData))

            headers = {0: "Mã số", 3: "Tên", 4: "Giá 0", 5: "Giá 1", 6: "Liên kết ảnh"}
            for key in headers:
                self.productsModel.setHeaderData(key, QtCore.Qt.Horizontal, headers[key])

            sizes = {0: 60, 3: 120, 4: 60, 5: 60, 6: 240}
            for key in sizes:
                self.productData.setColumnWidth(key, sizes[key])

        self.productsModel.setFilterRegExp(str(cat))

        if self.productsModel.rowCount() == 0:
            srcModel = self.productsModel.sourceModel() 
            rowCount = srcModel.rowCount()
            srcModel.insertRows(rowCount, 1)
            index = srcModel.index(rowCount, 1)
            srcModel.setData(index, cat, QtCore.Qt.EditRole)

            # self.productsModel.insertRows(self.productsModel.rowCount(), 1)
            # index = self.productsModel.index(self.productsModel.rowCount(), 1)
            # self.productsModel.setData(index, cat, QtCore.Qt.EditRole)

            
            #self.productsModel.setSourceModel(self.productsModel2)



        # totalShow = 0
        # for i in range(0, self.productsModel.rowCount()):
            # if (self.productsModel.data(self.productsModel.index(i, 1))) == cat:
                # self.productData.showRow(i)
                # totalShow += 1
            # else:
                # self.productData.hideRow(i)
        # if totalShow == 0:
            # rowId = self.productsModel.rowCount()
            # self.productsModel.insertRows(rowId, 1)
            # index = self.productsModel.index(rowId, 1)
            # self.productsModel.setData(index, cat, QtCore.Qt.EditRole)
            # print("======Themtai======" + str(rowId))

        self.productData.defaultValues = {1: cat}

    def showCropImageDialog(self, o):
        if self.targetProduct != None:
            index = self.targetProduct.siblingAtColumn(8)
            model = self.productsModel
            scale = model.data(index)
            div = 1
            for i in range(0, scale):
                div /= 2.0

            try:
                cropXidx = self.targetProduct.siblingAtColumn(9)
                posX = self.productData.model().data(cropXidx)
                cropYidx = self.targetProduct.siblingAtColumn(10)
                posY = self.productData.model().data(cropYidx)
                posX = int(posX / 2)
                posY = int(posY / 2)
            except:
                posX = 0
                posY = 0

            self.cropImgDialog.openDialog(int(1800 * div), int(1200 * div), posX, posY)
            print(o)

    def setupUiEx(self, MainWindow):
        # Set up on description change
        self.description.textChanged.connect(self.onDescriptionTextChanged)

        #@TODO: move initial to setupUiEx
        #@TODO: pass two param to __init__: self and MainWindow
        self.cropImgDialog = CropImgDialog(MainWindow, self)

        self.dropBriefImg.clicked.connect(self.showCropImageDialog)

        self.tmpImgs = {"cur": 1}
        if os.path.exists("./tmp"):
            shutil.rmtree("./tmp")
        os.makedirs("./tmp")

        self.curMetaDataRow = None
        databaseFileName = "simple-e-commerce.db"
        if not os.path.exists(databaseFileName):
            print("".join(["Không thấy tập tin ", databaseFileName, "."]))
            exit(0)
        catFolder =  os.getcwd() + '/cat'
        if not os.path.exists(catFolder):
            print("Không thấy thư mục 'cat'.")
            exit(0)

        # Decorate MainWindow
        MainWindow.showMaximized()

        # Setup categories GUI
        self.catModel = QtWidgets.QFileSystemModel()
        self.catModel.setRootPath(catFolder)
        self.categories.setModel(self.catModel)
        self.categories.setRootIndex(self.catModel.index(catFolder))
        #self.categories.collapsed.connect(self.oh) #############################
        #self.categories.expanded.connect(self.oh)  #############################
        self.categories.selectionModel().selectionChanged.connect(self.changeCat) #####
        for i in range(1, 4):
            self.categories.setColumnHidden(i, True)


        # # Setup list of values GUI
        # Remove for no_chars version


        # Setup main GUI - characteristics view
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(databaseFileName)
        self.db.open()
        #self.switchCharacteristicsView()
        self.switchDataViewInit()

        # Setup Radio button
        self.targetProduct = None
        self.activeImgLov = [self.prodImg, self.catImg]
        self.briefImgScaleLov = [self.briefFull, self.briefHalf, self.briefQuarter, self.briefMin]
       
        self.prodImg.toggled.connect(lambda:self.onActiveImgChange(self.prodImg))
        self.catImg.toggled.connect(lambda:self.onActiveImgChange(self.catImg))

        self.briefFull.toggled.connect(lambda:self.onBriefImgScaleChange(self.briefFull))
        self.briefHalf.toggled.connect(lambda:self.onBriefImgScaleChange(self.briefHalf))
        self.briefQuarter.toggled.connect(lambda:self.onBriefImgScaleChange(self.briefQuarter))
        self.briefMin.toggled.connect(lambda:self.onBriefImgScaleChange(self.briefMin))

    def onActiveImgChange(self, radio):
        if radio.isChecked():
            try:
                activeImgVal = self.activeImgLov.index(radio)
                if self.targetProduct != None:
                    index = self.targetProduct.siblingAtColumn(7)
                    model = self.productsModel
                    model.setData(index, activeImgVal, QtCore.Qt.EditRole)
            except:
                pass

    def onBriefImgScaleChange(self, radio):
        if radio.isChecked():
            try:
                briefImgScaleVal = self.briefImgScaleLov.index(radio)
                if self.targetProduct != None:
                    index = self.targetProduct.siblingAtColumn(8)
                    model = self.productsModel
                    model.setData(index, briefImgScaleVal, QtCore.Qt.EditRole)
            except Exception:
                pass

    def saveAll(self):
        if hasattr(self, "productsModel"):
            if self.productsModel.sourceModel().submitAll():
                print("self.productsModel.sourceModel().submitAll(): SUCCESS")
            else:
                print("self.productsModel.sourceModel().submitAll(): FAILURE")
            delattr(self, "productsModel")
        #@TODO prevent all other submitAll is commited

    def changeCat(self, cur, pre):
        indexes = cur.indexes()
        if len(indexes) > 0:
            fileName = self.catModel.fileName(indexes[0])
            cat = fileName.split("_")
            if len(cat) > 0:
                cat = int(cat[0])
                if self.state == 1:
                    self.switchDataViewCat(cat)
                elif self.state == 2:
                    #self.switchMetaDataViewCat(cat)
                    pass

    def changeMetaData(self, cur, pre):
        indexes = cur.indexes()
        if len(indexes) == 1:
            self.curMetaDataRow = indexes[0]
            #index = self.curMetaDataRow.siblingAtColumn(2)
            #dataType = self.metaData.model().data(index, QtCore.Qt.DisplayRole)
            #if dataType != "Danh mục":
                #self.curMetaDataRow = None

    def showProductDetail(self, cur):
        self.targetProduct = cur
        # show image
        try:
            imgUrl = self.productsModel.data(cur.siblingAtColumn(6))
            print(imgUrl)
            #if not(hasattr(self.tmpImgs, imgUrl)):
            if not(imgUrl in self.tmpImgs):
                print("*")
                response = urllib.request.urlopen(imgUrl)
                print("*")
                data = response.read()
                print("*")
                fn = "./tmp/" + str(self.tmpImgs["cur"]) + ".jpg"
                self.tmpImgs["cur"] += 1
                self.tmpImgs[imgUrl] = fn
                f = open(fn, "wb")
                print("*")
                f.write(data)
                print("*")
                f.close()
                print("*")
            fn = self.tmpImgs[imgUrl]
            print (fn)
            self.targetProductImgFn = fn
            pixMap = QtGui.QPixmap(fn)
            pixMap = pixMap.scaled(225, 150, QtCore.Qt.KeepAspectRatio)
            self.img.setPixmap(pixMap)
        except:
            pass
        # show image setting value
        activeImg = self.productsModel.data(cur.siblingAtColumn(7))
        briefImgScale = self.productsModel.data(cur.siblingAtColumn(8))
        activeImg = activeImg if isinstance(activeImg, int) else 0
        briefImgScale = briefImgScale if isinstance(briefImgScale, int) else 0
        self.activeImgLov[activeImg].setChecked(True)
        self.briefImgScaleLov[briefImgScale].setChecked(True)
        # show description
        htmlDescription = self.productsModel.data(cur.siblingAtColumn(11))
        self.description.setHtml(htmlDescription)

    def onDescriptionTextChanged(self):
        if self.targetProduct != None:
            idx = self.targetProduct.siblingAtColumn(11)
            data = self.description.toHtml()
            self.productsModel.setData(idx, data, QtCore.Qt.EditRole)

    def changeProductData(self, cur, pre):
        indexes = cur.indexes()
        if len(indexes) == 1:
            curProductData = indexes[0]
            self.showProductDetail(curProductData)

    def changeLov(self, cur, pre):
        if self.curMetaDataRow != None:
            indexes = cur.indexes()
            if len(indexes) > 0:
                fileName = self.catModel.fileName(indexes[0])
                cat = fileName.split("_")
                if len(cat) > 0:
                    cat = int(cat[0])
                    index = self.curMetaDataRow.siblingAtColumn(2)
                    dataType = self.metaData.model().data(index, QtCore.Qt.DisplayRole)
                    if dataType == "Danh mục":
                        index = self.curMetaDataRow.siblingAtColumn(3)
                        self.metaData.model().setData(index, str(cat), QtCore.Qt.EditRole)

    def onCropFinished(self, position):
        if position != None:
            cropXidx = self.targetProduct.siblingAtColumn(9)
            cropYidx = self.targetProduct.siblingAtColumn(10)
            self.productData.model().setData(cropXidx, position.x() * 2, QtCore.Qt.EditRole)
            self.productData.model().setData(cropYidx, position.y() * 2, QtCore.Qt.EditRole)

class ProductDataTableView(QtWidgets.QTableView):
    defaultValues = {}
    def keyPressEvent(self, event):
        if event.key() == 16777220:
            #colCount = self.model().columnCount()
            rowCount = self.model().rowCount()
            index = self.currentIndex()
            rowId = index.row()
            colId = index.column()
            #if colId + 1 < 7:
            if colId < 6:
                try:
                    nextId = {0:3, 3:4, 4:5, 5:6}[colId]
                except:
                    nextId = colId + 1
                self.setCurrentIndex(index.siblingAtColumn(nextId))
            else:
                if rowId + 1 == rowCount:
                    srcModel = self.model().sourceModel()
                    totalRowCount = srcModel.rowCount()
                    srcModel.insertRows(totalRowCount, 1)
                    for key in self.defaultValues:
                        data = self.defaultValues[key]
                        baseIndex = srcModel.index(totalRowCount, key)
                        srcModel.setData(baseIndex, data, QtCore.Qt.EditRole)
                        #print("\tAssign " + str(key) + " with " + str(data))
                self.setCurrentIndex(index.siblingAtRow(rowId + 1).siblingAtColumn(3))
        super(ProductDataTableView, self).keyPressEvent(event)

class SqlQueryModel(QSqlTableModel):
    comboItems=["", "Có/Không", "Khoảng", "Tham khảo", "Danh mục", "Chữ", "Chiều"]
    def flags(self, index):
        fl = QSqlTableModel.flags(self, index)
        fl |= QtCore.Qt.ItemIsEditable
        return fl

    def data(self, index, o):
        #TODO generictized me FIXME
        idx = super().data(index, o)
        if (index.column() == 2):
            if idx in range(0, len(self.comboItems)):
                return self.comboItems[idx]
        return idx

class TypeDelegate(QtWidgets.QItemDelegate):
    # @TODO fix bug: switch combo box type, regular expression of description
    # affection is too late. (need clear & re-enter to make new affection)
    comboItems=["", "Có/Không", "Khoảng", "Tham khảo", "Danh mục", "Chữ", "Chiều"]
    def __init__(self, parent):
        self._parent = parent
        QtWidgets.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        combo = QtWidgets.QComboBox(parent)
        combo.addItems(self.comboItems)
        return combo

    def setModelData(self, combo, model, index):
        model.setData(index, combo.currentIndex())

class IdDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent):
        QtWidgets.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        self.label = QtWidgets.QLabel(parent)
        return self.label

class ReadOnlyDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent):
        QtWidgets.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        self.label = QtWidgets.QLabel(parent)
        return self.label

    def setModelData(self, label, model, index):
        #super().setModelData(label, model, index)
        pass

class DefinitionDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent):
        self.model = parent.model()
        QtWidgets.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        self.text = super().createEditor(parent, option, index)
        cat = self.model.data(index.siblingAtColumn(2), QtCore.Qt.DisplayRole)
        if cat == "Khoảng":
            reg_ex = QtCore.QRegExp("#?-?[0-9]+,\s#?-?[0-9]+,\s.+")
        elif cat == "Danh mục":
            reg_ex = QtCore.QRegExp("[0-9]+n?")
        elif cat == "Chiều":
            reg_ex = QtCore.QRegExp("[0-9]+\s.+")
        else:
            reg_ex = QtCore.QRegExp("^")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.text)
        self.text.setValidator(input_validator)
        return self.text

class CropImgRegion(QtWidgets.QGroupBox):
    def __init__(self, parent):
        self.dropAt = None
        QtWidgets.QDialog.__init__(self, parent)

    def enableDragDrop(self):
        self.allowDragDrop = True

    def disableDragDrop(self):
        self.allowDragDrop = False

    def mousePressEvent(self, event):
        if self.allowDragDrop:
            self.__mousePressPos = None
            self.__mouseMovePos = None
            if event.button() == QtCore.Qt.LeftButton:
                self.__mousePressPos = event.globalPos()
                self.__mouseMovePos = event.globalPos()
        super(CropImgRegion, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.allowDragDrop:
            if event.buttons() == QtCore.Qt.LeftButton:
                # adjust offset from clicked point to origin of widget
                currPos = self.mapToGlobal(self.pos())
                globalPos = event.globalPos()
                diff = globalPos - self.__mouseMovePos
                newPos = self.mapFromGlobal(currPos + diff)
                self.dropAt = newPos
                self.move(newPos)
                self.__mouseMovePos = globalPos
        super(CropImgRegion, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.allowDragDrop:
            if self.__mousePressPos is not None:
                moved = event.globalPos() - self.__mousePressPos 
                if moved.manhattanLength() > 3:
                    event.ignore()
                    return
        super(CropImgRegion, self).mouseReleaseEvent(event)

class CropImgDialog(QtWidgets.QDialog):
    def __init__(self, parent, container):
        QtWidgets.QDialog.__init__(self, parent)
        ##self.resize(900, 600)
        self.imgLabel = QtWidgets.QLabel(self)
        ##self.imgLabel.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.setModal(True)
        self.container = container
        # Init drop rectangle
        self.groupBox = CropImgRegion(self)
        ##self.groupBox.setGeometry(QtCore.QRect(int(900/2) - int(225/2) - 1, int(600/2) - int(150/2) - 1, 225 + 2, 150 + 2))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("QGroupBox { border: 1px solid black;}")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")

    def openDialog(self, width, height, posX, posY):
        if width <= 225 or height <= 150:
            self.groupBox.disableDragDrop()
        else:
            self.groupBox.enableDragDrop()
        dropW = int(225 / 2)
        dropH = int(150 / 2)
        width = int(width / 2)
        height = int(height / 2)
        if (hasattr(self.container, "targetProductImgFn")):
            pixMap = QtGui.QPixmap(self.container.targetProductImgFn)
            pixMap = pixMap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
            self.imgLabel.setPixmap(pixMap)
        self.resize(width, height)
        self.imgLabel.setGeometry(QtCore.QRect(0, 0, width, height))

        self.groupBox.setGeometry(QtCore.QRect(posX, posY, dropW + 2, dropH + 2))
        #self.groupBox.setGeometry(QtCore.QRect(int(width/2) - int(dropW/2) - 1, int(height/2) - int(dropH/2) - 1, dropW + 2, dropH + 2))
        self.exec_()

    def closeEvent(self, event):
        self.container.onCropFinished(self.groupBox.dropAt)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupUiEx(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
