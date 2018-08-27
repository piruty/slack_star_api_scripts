# Star Operator on Slack

----

## Description

Python scripts to get / add / remove star items on slack.

## Dependency

* Python3
* requests

## Setup

### 1. Install modules

```bash
pip install -r requirements.txt
```

### 2. Get slack api token

Visit [here](https://api.slack.com), and create your slack api app.  
Then, copy your app's api token.

### 3. Add api token as env variable

```bash
echo "export SLACK_API_TOKEN=your_api_token_here"
```

## Usage

### Get starred items

```bash
python get_starred_items.py
```

### Add star to items

```bash
python add_star.py channel_id timestamp
```

### remove star from items

```bash
python remove_star.py channel_id timestamp
```

## Licence

MIT

## Author

[piruty](https://piruty.com)

## References

* [Slack API | Slack](https://api.slack.com)
* [stars.list method | Slack](https://api.slack.com/methods/stars.list)
* [stars.add method | Slack](https://api.slack.com/methods/stars.add)
* [stars.remove method | Slack](https://api.slack.com/methods/stars.remove)
