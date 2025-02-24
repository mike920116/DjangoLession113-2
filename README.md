# DjangoLession113-2
二技一年級下學期資料庫管理系統實作，Django的實作課程
# 建立虛擬環境序流程 虛擬環境建立在目錄以外的地方 因為檔案很大
1.python -V ：確認python當前版本 project-name(命名虛擬環境名稱)

2.python -m venv project-name：建立虛擬環境

3.project-name\Scripts\activate.bat：進入虛擬環境

# 進入虛擬環境後 建立mysite資料檔案的操作順序
4.python -m pip install Django==4.2：在虛擬環境裡面下載Django並且版本為4.2

5.cd (dir)：你想要將網頁在哪個目錄執行，不要在虛擬環境的目錄裡面

6.mkdir (dir)：建立專案名稱

7.cd (dir)：進到專案目錄

8.django-admin startproject mysie：使用django管理員身分建立名稱為mysite的資料檔案
