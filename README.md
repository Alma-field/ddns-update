# Hololive Notice
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
| HOSTS | 更新対象のホスト名<br>(セミコロン区切り) |
| DOMAIN | ドメイン名 |

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
HOSTS=セミコロン区切りの更新対象ホスト名
DOMAIN=ドメイン名
```
4. `python main.py  [--service <サービス名>]`を実行してください。

### 実行時パラメータ
| パラメータ名 | 説明 |
| :--: | -- |
| **\<service\>** | サービス名 |
| onamaecom | お名前ドットコム |

 - **太字**の場合は必須パラメータです。<br>
 - 例：`python main.py --service onamaecom`
