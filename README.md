# TaskNest

ユーザーがタスクを作成・管理できるWebアプリケーションです。  
フレームワークを使用したWebアプリ開発、および環境構築からデプロイまでの一連の流れを理解するために作成しました。  

## デモ

[TaskNestを試す](https://tasknest-r6c6.onrender.com)

## 機能

- ユーザー認証
  - 新規登録
  - ログイン
  - ログアウト

- タスクのCRUD操作
  - 作成（Create）
  - 読み取り（Read）
  - 更新（Update）
  - 削除（Delete）

- タスクの表示機能
  - 並び替え
  - 絞込み
  - 検索

## 使用技術  

- フロントエンド
  - HTML

- バックエンド
  - Python
  - Django

- データベース
  - SQLite3

- デプロイ
  - Render

- バージョン管理
  - Git / GitHub

- その他
  - VSCode
  - ChatGPT / Gemini

## 学んだこと

- Webアプリ開発の全体像
  - 環境構築、機能開発、デプロイという一連のサイクルを経験し、Webアプリがどのように動いているのかを体系的に理解できました。

- HTMLの基礎
  - 基本的な記述方法や構造を意識したマークアップの重要性を学びました。

- ディレクトリ構成と設計の重要性
  - Django特有のディレクトリ構造や、MTV (Model-Template-View) の理解を深めました。  
  特に、フレームワークが参照するファイルのパスと、それに基づいた適切な配置の重要性を学びました。

- GitとGitHubのワークフロー
  - `git status`, `git add`, `git commit`, `git push` といった基本コマンドの意味と、バージョン管理の基本的な流れを実践的に習得しました。

## 環境構築とセットアップ

このアプリケーションをローカル環境で動かすには、以下の手順を実行してください。

1. リポジトリのクローン

    ```bash
    git clone https://github.com/ochate/tasknest.git
    cd tasknest
    ```

2. 仮想環境の作成と有効化

    ```bash
    python -m venv venv

    # Windows
    .\venv\Scripts\activate.ps1

    # mac/Linux
    source venv/bin/active
    ```

3. 依存関係のインストール

    ```bash
    pip install -r requirements.txt
    ```

4. データベースのマイグレーション

    ```bash
    python manage.py migrate
    ```

5. 開発サーバーの起動

   ```bash
   python manage.py
   ```

ブラウザで `http://127.0.0.1:8000/` にアクセスすると、アプリケーションが表示されます。
