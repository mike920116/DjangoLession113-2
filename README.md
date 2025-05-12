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

# 建立三套組1.django版本2.專案3.python app
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

# 常見遇到cmd指令

rmdir /s (資料夾名稱)：刪除用不到的資料夾

del (資料夾/檔案名稱)：刪除資料夾內所有檔案或指定檔案名稱

應用（App）與專案（Project）的區別

Django Project（專案）：整個 Django 的網站，包含設定 (settings.py)、URL 路由 (urls.py)、資料庫設定等。

Django App（應用）：專案內的一個功能模組，例如「用戶管理」、「博客」、「購物車」等，App 可以被重複使用。

# 課本第四章資料結構 (mynewsite底下四個資料)

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


# Django 留言板與 BMI 計算專案 (dj4ch08)

這是一個使用 Django 框架建置的專案，主要功能包含一個留言板系統以及一個 BMI 計算器。

## 功能特色

*   **留言板系統:**
    *   使用者可以張貼包含心情、暱稱、內容的留言。
    *   留言需要設定刪除密碼。
    *   留言列表顯示。
    *   可透過密碼刪除自己的留言。
    *   整合 Google reCAPTCHA 以防止機器人。
*   **BMI 計算器:**
    *   使用者可以輸入姓名、身高、體重。
    *   系統會計算並顯示 BMI 值。
    *   BMI 資料儲存於 MongoDB。
*   **聯絡表單:**
    *   使用者可以透過表單發送郵件給網站管理員。
*   **後台管理:**
    *   整合 Django Admin，方便管理留言與心情等資料。

## 技術棧

*   **後端:** Python, Django
*   **資料庫:** SQLite (預設), MongoDB (用於 BMI 功能)
*   **前端:** HTML, CSS (透過 Django 模板)
*   **其他:** django-simple-captcha (用於驗證碼)

## 使用前準備

1.  **Python:** 請確保已安裝 Python 3.10 或以上版本。
2.  **pip:** Python 套件安裝工具。
3.  **Docker & Docker Compose:** (若要使用 BMI 計算功能，需啟動 MongoDB)
    *   安裝 [Docker Desktop](https://www.docker.com/products/docker-desktop/)。

## 安裝與設定

1.  **複製專案 (或下載原始碼):**
    ```bash
    # 若使用 git
    # git clone <repository_url>
    # cd dj4ch08
    ```

2.  **進入專案目錄:**
    ```powershell
    cd d:\DjangoLession113-2\20250512myproject第八章\dj4ch08
    ```

3.  **安裝 Python 依賴套件:**
    ```powershell
    python -m pip install -r requirements.txt
    ```

4.  **設定環境變數 (在 `dj4ch08/settings.py`):**
    *   **電子郵件設定 (用於聯絡表單):**
        ```python
        EMAIL_HOST_USER = "youremail@gmail.com"  # 您的 Gmail 信箱
        EMAIL_HOST_PASSWORD = "your_gmail_app_password" # 您的 Gmail 應用程式密碼
        ```
        *注意: Gmail 可能需要設定「應用程式密碼」而非直接使用登入密碼。*
    *   **Google reCAPTCHA 金鑰:**
        ```python
        GOOGLE_RECAPTCHA_SECRET_KEY = 'YOUR_GOOGLE_RECAPTCHA_SECRET_KEY' # 您的 reCAPTCHA Secret Key
        ```
        *請至 [Google reCAPTCHA](https://www.google.com/recaptcha/admin/create) 申請您網站的金鑰。*

5.  **啟動 MongoDB (若要使用 BMI 功能):**
    *   在專案根目錄下的 `mongo-db` 資料夾中，開啟終端機並執行：
        ```powershell
        cd mongo-db
        docker-compose up -d
        cd ..
        ```
    *   這會使用 `docker-compose.yml` 檔案啟動 MongoDB 和 Mongo Express (網頁管理介面，可於 `http://localhost:8081` 訪問)。
    *   MongoDB 連線資訊 (預設):
        *   主機: `localhost`
        *   連接埠: `27017`
        *   使用者名稱 (ME_CONFIG_MONGODB_ADMINUSERNAME): `root`
        *   密碼 (ME_CONFIG_MONGODB_ADMINPASSWORD): `example`

6.  **執行資料庫遷移 (Migrations):**
    *   這會建立 Django 所需的資料庫表結構 (預設使用 SQLite)。
    ```powershell
    python manage.py migrate
    ```

7.  **建立超級使用者 (Superuser) (可選，用於後台管理):**
    ```powershell
    python manage.py createsuperuser
    ```
    依照提示設定使用者名稱、電子郵件和密碼。

## 執行應用程式

1.  **啟動 Django 開發伺服器:**
    ```powershell
    python manage.py runserver
    ```

2.  **開啟瀏覽器並訪問:**
    *   首頁: `http://127.0.0.1:8000/`
    *   後台管理: `http://127.0.0.1:8000/admin/` (需使用超級使用者帳號登入)
    *   留言列表: `http://127.0.0.1:8000/list/`
    *   BMI 計算: `http://127.0.0.1:8000/bmi/`

## 專案結構概覽

```
dj4ch08/                  # 專案根目錄
├── dj4ch08/              # Django 專案設定目錄
│   ├── settings.py       # 專案設定檔
│   ├── urls.py           # 專案主路由設定
│   └── ...
├── mysite/               # Django 應用程式 (主要邏輯)
│   ├── models.py         # 資料庫模型定義
│   ├── views.py          # 視圖函式 (處理請求與回應)
│   ├── forms.py          # 表單定義
│   ├── admin.py          # 後台管理設定
│   ├── urls.py           # (若有) 應用程式路由設定
│   └── ...
├── templates/            # HTML 模板檔案
├── static/               # 靜態檔案 (CSS, JavaScript, 圖片)
├── media/                # 使用者上傳的媒體檔案
├── mongo-db/             # MongoDB 相關設定與工具
│   ├── docker-compose.yml # Docker Compose 設定檔
│   └── ...
├── manage.py             # Django 管理腳本
├── requirements.txt      # Python 依賴套件列表
├── db.sqlite3            # SQLite 資料庫檔案 (預設)
└── README.md             # 本檔案
```

## MongoDB 工具

在 `mongo-db/` 資料夾中包含以下 Python 腳本，可用於直接操作 MongoDB 資料庫 (需先安裝 `pymongo` 並確保 MongoDB 服務正在運行)：

*   `deldata.py`: 刪除資料。
*   `insertdata.py`: 插入範例資料。
*   `listdata.py`: 列出資料。
*   `listdb.py`: 列出所有資料庫。

---
