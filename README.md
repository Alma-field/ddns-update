# DDNS Update
![license](https://img.shields.io/badge/license-MIT-blue.svg)
[![GitHub issues open](https://img.shields.io/github/issues/Alma-field/ddns-update.svg?maxAge=2592000)](https://github.com/Alma-field/ddns-update/issues?q=is%3Aopen+is%3Aissue)
[![GitHub issues close](https://img.shields.io/github/issues-closed-raw/Alma-field/ddns-update.svg?maxAge=2592000)](https://github.com/Alma-field/ddns-update/issues?q=is%3Aclose+is%3Aissue)

DDNSのIPアドレスを更新します。


## 目次
 - [使用方法](#使用方法)
   - [ローカルでテストを行う場合](#ローカルでテストを行う場合)
 - [実行時パラメータ](#実行時パラメータ)

## 使用方法

### 必要なもの

| 項目 | 説明 |
| ---- | ----------- |
| USER_ID | 各種サービスのID |
| PASSWORD | 各種サービスのパスワード |
| DOMAINS | 更新対象のドメイン名<br>(スラッシュ区切り) |

#### ローカルでテストを行う場合
1. このリポジトリをローカル環境に複製してください。
```shell
git clone https://github.com/Alma-field/ddns-update
```
2. `pip install -r requirements.txt`を実行しライブラリをダウンロードします。
3. `main.py`と同階層に`.env`ファイルを`.env.sample`(または下記例)を参考に作成してください。<br>例：
```
USER_ID=各種サービスのユーザーID
PASSWORD=パスワード
DOMAINS=スラッシュ区切りの更新対象ドメイン名
```
4. `python main.py`を実行してください。(お名前ドットコムの場合)

### 実行時パラメータ
| パラメータ名 | 値 | 説明 |
| :-: | :-: | - |
| **-s/--service** | | **DDNSサービス名** |
| | **onamaecom** | お名前ドットコム |
| **-dns/--dns** | | **DNSサーバー** |
| | **google** | dns.google(8.8.8.8) |
| **-ip/--ipaddress** |  | **更新用IPアドレス**<br>`[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}` |
| **-f/--force** | | 強制更新 |

 - 値欄が**太字**の場合はデフォルト値です。
 - 例：`python main.py --service onamaecom`
