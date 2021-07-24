# README

## リッチメニューの作成

これ
![リッチメニュー](./imgs/rich-menu.png)

### 手順

1. [LINE Official Account Manager](https://manager.line.biz/)へアクセスし、開発中のアカウントを選択

1. ホームタブの左のメニューから `リッチメニュー`を選択する

1. `作成`をおす

1. 手順に沿ってリッチメニューを作成する

## Webhook のイベントオブジェクト

使用する場合は lower_case で！！
`replyToken` -> `reply_token`

```
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "0f3779fba3b349968c5d07db31eab56f",
      "type": "message",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "message": {
        "id": "325708",
        "type": "text",
        "text": "Hello, world"
      }
    },
    {
      "replyToken": "8cf9239d56244f4197887e939187e19e",
      "type": "follow",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      }
    }
  ]
}
```
