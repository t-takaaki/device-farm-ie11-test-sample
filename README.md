# Device Farm を使ってデスクトップブラウザ(IE11)でテストを実行するサンプルコード

[AWS Device Farm が Selenium を使用したデスクトップブラウザのテストを発表](https://aws.amazon.com/jp/about-aws/whats-new/2020/01/aws-device-farm-announces-desktop-browser-testing-using-selenium/)
> AWS Device Farm では、AWS クラウドでホストされている Chrome、Firefox、Internet Explorer ブラウザのさまざまなデスクトップバージョンに対してウェブアプリケーションをテストできるようになりました。
> 既存の Selenium テストで数行のコードを変更するだけで、Device Farm のフルマネージド型ブラウザグリッドで実行を開始できます。

激アツやん

QA - [よくある質問 - AWS Device Farm | AWS](https://aws.amazon.com/jp/device-farm/faqs/#Testing_on_desktop_browsers)
> Q. AWS Device Farm での Desktop Browser Testing とは何ですか?
> A. Device Farm を使用すると、AWS クラウドでホストされているさまざまなデスクトップブラウザとブラウザバージョンで Selenium テストを実行できます。Device Farm は、Selenium テストのクライアント側の実行モデルに従います。つまり、テストはお客様のローカルマシンで実行されますが、Selenium API を通じて AWS Device Farm でホストされているブラウザとやり取りします。

PythonSDKを使う

[Migrating to Device Farm Desktop Browser Testing from Local Selenium WebDrivers - Device Farm desktop browser testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/getting-started-local.html)


# GettingStarted
## 前提
- [こちら](https://docs.aws.amazon.com/devicefarm/latest/testgrid/getting-started-local.html)のドキュメントを参考に、以下設定済みとして進めます
  - DeviceFarmのproject ARN
  - AWS CLIのcredentials
- SeleniumをPythonで動かせるようになっていること

```
# project ARNの例
arn:aws:devicefarm:us-west-2:111122223333:testgrid-project:123e4567-e89b-12d3-a456-426655440000.

# credentialsの例
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

## やること
1. .envを作成し、環境変数に事前に作成したproject ARNを設定してください
```
$ cp .env.sample .env
$ vim .env
```

2. 依存ライブラリをインストールします
```
$ pip install -r requirements.txt
```

3. スクリーンショットの保存先ディレクトリを作成します
```
$ mkdir screenshots
```

これで準備完了です。

サンプルのテストコードは ``` test.py ``` です。
pytestを使用しています。テストを実行すると、SeleniumがDeviceFarm上のIE11
を動かし、テストコードを実行、その後スクリーンショットを保存します。
```
$ pytest test.py
$ open screenshots/test-hogehoge.png
```

# 所感
* テストはローカルで実行できる（おそらくCIツール上でも可能）
* 通常なら Selenium は WebDriver を使ってローカルのブラウザを立ち上げる
	* SeleniumはリモートのWebDriverクライアントを実行することができる
		* [リモートWebDriverクライアント :: Seleniumドキュメント](https://www.selenium.dev/documentation/ja/remote_webdriver/remote_webdriver_client/)
* 向き先をDeviceFarm上のブラウザに変えることで、任意の環境上でのテスト実行が可能になる
* サポート環境
	* ブラウザ
		* Chrome, FireFox, IE11 2020/05/06時点
		* [Supported Capabilities, Browsers, and Platforms in Device Farm Desktop Browser Testing - Device Farm desktop browser testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref-support.html#techref-support-browsers)
	* プラットフォーム
		* Windows 2020/05/06時点
		* [Supported Capabilities, Browsers, and Platforms in Device Farm Desktop Browser Testing - Device Farm desktop browser testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref-support.html#techref-support-platforms)
* 料金
	* デスクトップ版は無料枠ないっぽい
	* 0.005USD/インスタンス分
		* 1$ / 200分
		* 1テスト20〜30秒 → 400回で1ドルくらい？
	* [料金 - AWS Device Farm | AWS](https://aws.amazon.com/jp/device-farm/pricing/)
* ユースケース
	* 毎回テスト実行はコスパ見合わない
	* 例えば…master to production のリリース前に自動実行
		* 任意のページのスクショを取得
		* 全スクショを見て、承認すればマージできる…等
* 参考にしたリンク
	* [AWS Device Farm が Selenium を使用したデスクトップブラウザのテストを発表](https://aws.amazon.com/jp/about-aws/whats-new/2020/01/aws-device-farm-announces-desktop-browser-testing-using-selenium/)
	* https://docs.aws.amazon.com/devicefarm/latest/testgrid/what-is-testgrid.html#first-time-user
	* [Migrating to Device Farm Desktop Browser Testing from Local Selenium WebDrivers - Device Farm desktop browser testing](https://docs.aws.amazon.com/devicefarm/latest/testgrid/getting-started-local.html)
	* https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref-support.html
	* https://docs.aws.amazon.com/devicefarm/latest/testgrid/testing-frameworks-python.html
