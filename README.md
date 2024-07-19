# fastapi-jinja2-study

## 概要

FastAPIとJinja2を用いたSSRの勉強用プロジェクト

## 注意書き

- このREADMEはMacで実行することを想定して書いています。
- パッケージマネージャーにはpoetryを使用しています。

## 環境構築

### 統合開発環境

VS Codeをダウンロードしてインストールする。
VS Codeは[こちら](https://code.visualstudio.com/download)からダウンロードできます。

### 補助プログラム

#### `poetry install`でインストールされるもの

次の二つはdev dependancyとしてpyproject.tomlにあるため、`poetry install`コマンドでインストールする。

- pylint = "^3.2.5"
- pre-commit = "^3.7.1"
- black = "^24.4.2"
- pytest = "^8.2.2"
- faker = "^26.0.0"
- mypy = "^1.10.1"

##### Pylintの設定

VSCodeでLintが働くように設定する。

設定ファイルは[こちら](.eslintrc.json)


##### BlackFormatterの設定

設定ファイルは[こちら](pyproject.toml)

pyproject.tomlの[tool.black]のセクションを参照のこと

#### Pre Commit

Pre Commitは`brew`でインストールする。

```shell:terminal
brew install pre-commit
```

Pre Commitの設定ファイルは`git add`することで有効となる。

```shell:terminal
git add .pre-commit-config.yaml
```


設定ファイルは[こちら](.pre-commit-config.yaml)

### ライブラリ

次のコマンドでインストールする。

```shell:terminal
poetry install
```

#### 特質すべきもの

- fastapi
  - このリポジトリで勉強に使うライブラリ
- Jinja2
  - SSRをするためのテンプレートエンジン

## 使い方

以下のコマンドをTerminalで実行する。

```shell:terminal
poetry run uvicorn fastapi_jinja2_study.app:app --reload
```

## 参考情報


以上
