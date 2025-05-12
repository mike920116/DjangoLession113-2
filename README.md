# DjangoLession113-2
二技一年級下學期資料庫管理系統實作，Django的實作課程

# 啟動伺服器

```powershell
python manage.py runserver
```
接著用瀏覽器訪問 `http://127.0.0.1:8000`

# 從建立到進入虛擬環境

1.  **確認 Python 版本：**
    ```powershell
    python -V
    ```

2.  **建立虛擬環境：**
    (將 `<your_venv_name>` 替換為您的虛擬環境名稱，例如 `myenv`)
    ```powershell
    python -m venv <your_venv_name>
    ```

3.  **進入虛擬環境 (PowerShell)：**
    (將 `<your_venv_name>` 替換為您剛才建立的虛擬環境名稱)
    ```powershell
    .\\<your_venv_name>\\Scripts\\Activate.ps1
    ```
    *如果遇到執行原則 (Execution Policy) 問題，您可能需要先以系統管理員身分開啟 PowerShell 並執行 `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` 或 `Set-ExecutionPolicy RemoteSigned -Scope Process`，然後再嘗試啟動虛擬環境。*
    *若使用 CMD，請執行 `<your_venv_name>\\Scripts\\activate.bat`*

# 建立 Django 專案與應用程式

1.  **安裝 Django (指定版本 4.2)：**
    (請確保您已在虛擬環境中)
    ```powershell
    python -m pip install Django==4.2
    ```

2.  **建立 Django 專案：**
    (將 `<your_project_name>` 替換為您的專案名稱，例如 `myproject` 或 `mblog`)
    ```powershell
    django-admin startproject <your_project_name>
    ```

3.  **進入專案目錄：**
    (將 `<your_project_name>` 替換為您的專案名稱)
    ```powershell
    cd <your_project_name>
    ```

4.  **建立 Django 應用程式 (App)：**
    (將 `<your_app_name>` 替換為您的應用程式名稱，例如 `mysite`)
    ```powershell
    python manage.py startapp <your_app_name>
    ```

5.  **產生資料庫遷移檔案：**
    (這會根據您在 `models.py` 中的定義產生遷移檔案)
    ```powershell
    python manage.py makemigrations
    ```

6.  **執行資料庫遷移：**
    (這會將變更應用到資料庫)
    ```powershell
    python manage.py migrate
    ```

7.  **顯示遷移狀態 (可選)：**
    ```powershell
    python manage.py showmigrations
    ```

# 專案建立流程概覽 (另一種操作順序參考)

1.  **選擇或建立專案的根目錄：**
    (例如，您想在 `D:\\my_django_projects` 下建立新專案)
    ```powershell
    # 移至您選擇的基礎目錄
    cd <your_chosen_base_directory> # 例如: cd D:\\my_django_projects
    ```
    ```powershell
    # 建立專案資料夾
    mkdir <your_project_folder_name> # 例如: mkdir my_new_django_site
    ```
    ```powershell
    # 進入專案資料夾
    cd <your_project_folder_name> # 例如: cd my_new_django_site
    ```
    *注意：建議不要在虛擬環境的目錄內建立 Django 專案。*

2.  **(若尚未完成) 建立並進入虛擬環境，並安裝 Django：**
    (參考上一節「從建立到進入虛擬環境」及「安裝 Django」的指令)
    ```powershell
    # python -m venv <your_venv_name>
    # .\\<your_venv_name>\\Scripts\\Activate.ps1
    # python -m pip install Django==4.2
    ```

3.  **建立 Django 專案：**
    (將 `<your_project_name>` 替換為您的專案名稱。此名稱將是專案配置目錄和管理命令的基礎。)
    ```powershell
    django-admin startproject <your_project_name> .
    ```
    *注意：命令結尾的 `.` 表示在當前目錄 (`<your_project_folder_name>`) 下建立專案檔案，而不是再新增一層與 `<your_project_name>` 同名的子目錄。如果省略 `.`，則會在 `<your_project_folder_name>` 下建立一個名為 `<your_project_name>` 的子目錄，並將專案檔案放在其中。*

4.  **建立超級使用者 (用於後台管理)：**
    ```powershell
    python manage.py createsuperuser
    ```
    (依照提示設定使用者名稱、電子郵件和密碼)

# 常見 PowerShell 指令 (用於檔案/資料夾操作)

*   **刪除資料夾及其內容 (遞迴)：**
    (將 `<folder_name>` 替換為要刪除的資料夾名稱)
    ```powershell
    Remove-Item -Recurse -Force <folder_name>
    ```
    *`rmdir /s <folder_name>` 是 CMD 中的等效指令。*

*   **刪除檔案：**
    (將 `<file_name>` 替換為要刪除的檔案名稱)
    ```powershell
    Remove-Item -Force <file_name>
    ```
    *`del <file_name>` 是 CMD 中的等效指令。*

*   **刪除資料夾內所有檔案 (不含子資料夾中的檔案)：**
    (將 `<folder_name>` 替換為目標資料夾名稱)
    ```powershell
    Remove-Item -Force <folder_name>\\*
    ```

# 應用（App）與專案（Project）的區別

Django Project（專案）：整個 Django 的網站，包含設定 (settings.py)、URL 路由 (urls.py)、資料庫設定等。

Django App（應用）：專案內的一個功能模組，例如「用戶管理」、「博客」、「購物車」等，App 可以被重複使用。

# 專案與應用程式的典型目錄結構範例

假設我們的專案名稱是 `myproject`，應用程式名稱是 `myapp`。

1.  **建立專案 (例如 `myproject`)：**
    ```powershell
    django-admin startproject myproject
    ```
    ```powershell
    cd myproject
    ```

2.  **建立應用程式 (例如 `myapp`)：**
    (在專案目錄內執行)
    ```powershell
    python manage.py startapp myapp
    ```

3.  **在應用程式 `myapp` 目錄內建立 `static` 和 `templates` 資料夾：**
    (這些資料夾通常建立在每個 app 內部，或者在專案層級集中管理)
    ```powershell
    cd myapp
    mkdir static
    mkdir templates
    cd .. # 回到專案根目錄 (myproject)
    ```
    *或者，您也可以在專案根目錄 (`myproject`) 為整個專案建立共用的 `static` 和 `templates` 資料夾，這是另一種常見模式。*

**預期產生的結構 (以 `myproject` 和 `myapp` 為例)：**
```plaintext
myproject/
|----manage.py             # Django 管理腳本
|----myproject/            # Django 專案配置目錄
|    |----settings.py
|    |----urls.py
|    |----wsgi.py
|    |----asgi.py           # Django 3.0+
|    |----__init__.py
|----myapp/                # Django 應用程式 (App)
|    |----migrations/
|    |----static/           # (自行建立 for myapp)
|    |----templates/        # (自行建立 for myapp)
|    |----__init__.py
|    |----admin.py
|    |----apps.py
|    |----models.py
|    |----tests.py
|    |----views.py
|----db.sqlite3            # (執行 python manage.py migrate 後產生)
```
*注意：`static` 和 `templates` 的確切位置和組織方式可能因專案配置和個人偏好而異。上述是在 app 內建立的範例。*

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
