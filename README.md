# DjangoLession113-2
二技一年級下學期資料庫管理系統實作，Django的實作課程

# 啟動伺服器：
python manage.py runserver 
(用瀏覽器訪問 http://127.0.0.1:8000)


# 從建立到進入虛擬環境
python -V 

**確認python當前版本 project-name(命名虛擬環境名稱)**

python -m venv project-name

**建立虛擬環境**

project-name(2025虛擬環境)\Scripts\activate.bat(.bat可省略不打)

**進入虛擬環境(project-name為剛才建立的虛擬環境名稱)**

# 建立課本2-03的目錄底下所有檔案
python -m pip install Django==4.2

**在虛擬環境裡面下載Django並且版本為4.2**

django-admin startproject mblog

**使用django管理員身分建立名稱為mblog的資料夾檔案**

cd mblog

**進到mblog目錄**

python manage.py startapp mysite

**創建一個新的 Django 應用（app），名稱為 mysite。**

python manage.py makemigrations

**依照 models.py 產生 migrations 檔案**

python manage.py migrate

**依照 migrations 建立資料庫**

python manage.py showmigrations

**顯示目前migrations的狀態**

# 建立mysite資料檔案的操作順序
python -m pip install Django==4.2

**在虛擬環境裡面下載Django並且版本為4.2**

cd (dir)

**你想要將網頁在哪個目錄執行，不要在虛擬環境的目錄裡面**

mkdir (dir)

**建立專案名稱**

cd (dir)

**進到專案目錄**

django-admin startproject mysie

**使用django管理員身分建立名稱為mysite的資料檔案**

python manage.py createsuperuser

**建立超級使用者**

# 課本第四章資料結構

mynewsite(django-admin startproject mynewsite)
|----db.sqlite3
|----manage.py
|----mynewsite
|----|----setting.py
|----|----url.py
|----|----wsgi.py
|----mysite(進到專案之後下python manage.py startapp mysite)
     |----admin.py
     |----apps.py
     |----migrations
     |----models.py
     |----test.py
     |----views.py
     |----static(自己建立的資料夾)(下指令mkdir)
     |----templates(自己建立的資料夾)(下指令mkdir)
# 常見遇到cmd指令

rmdir /s (資料夾名稱)：刪除用不到的資料夾

del (資料夾/檔案名稱)：刪除資料夾內所有檔案或指定檔案名稱

應用（App）與專案（Project）的區別

Django Project（專案）：整個 Django 的網站，包含設定 (settings.py)、URL 路由 (urls.py)、資料庫設定等。

Django App（應用）：專案內的一個功能模組，例如「用戶管理」、「博客」、「購物車」等，App 可以被重複使用。