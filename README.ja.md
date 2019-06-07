
# Git autopep8

![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg "Python 3.6")
![MIT License](https://img.shields.io/badge/License-MIT-green.svg "MIT License")

\| 日本語 \| [English](README.md) \| 

Git autopep8 はリポジトリに追加・更新されたソースファイルに、 **PEP8**コーディング規約を適用するコマンドを追加します。
Git と Python で物を書くとき `git commit` のついでに、自動でコーディング規約を適用できたら便利そうだったこと。
`pre-commit` に複雑なコードを書かず、ひとつのコマンドで済ませることができたら便利そうだったので書きました。

## インストール

Git autopep8 は `setup.py` が同梱されていますので下記のコマンドからインストールできます。

```shell
$ python setup.py install
```

## 使い方

Git autopep8 導入すると、`git-autopep8` グローバルコマンドがインストールされます。
このコマンドは `git add` された `.py` 拡張子のファイルに **PEP8**コーディング規約を適用します。
元のファイルは上書きされます。
`git commit` 時に自動でこのコマンドを実行したい場合には、`.git/hook/pre-commit` にこのコマンドを登録してください。

```shell
$ git-autopep8 # 追加の引数は autopep8 に受け渡されます。
```

## ライセンス 

Git autopep8は [MIT License](LICENSE.txt) で公開されています。  
Git autopep8は [autopep8](https://github.com/hhatto/autopep8) を使用しています。こちらは [MIT License](license/LICENSE_AUTOPEP8.txt) で公開されています。詳細は [license/LICENSE_AUTOPEP8.txt](license/LICENSE_AUTOPEP8.txt) と [license/AUTHORS.rst](license/AUTHORS.rst) を参照ください。
