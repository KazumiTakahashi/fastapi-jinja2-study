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

- aaaa
- aaaa
- aaaa

##### Pylintの設定

VSCodeでLintが働くように設定する。

設定ファイルは[こちら](.eslintrc.json)


##### BlackFormatterの設定

設定ファイルは[こちら](.eslintrc.json)

#### Pre Commit

Pre Commitは`brew`でインストールする。

```shell:terminal
brew install pre-commit
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

## 使い方

以下のコマンドをTerminalで実行する。

```shell:terminal
aaaaa
```

## 参考情報


以上
