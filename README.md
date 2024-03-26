# Daily Bible Verses 
<img src="docker-icon.png" alt="Bible Icon" width="100" />

This project is designed to provide daily Bible verses as norwegian audio tracks. You can choose between Bokmål and Nynorsk.

## Prerequisites

Docker

## Setup

### 1. Pull Docker Container
`docker pull vegardbeider/daily-bible-vers:latest`

### 2. Configure Docker Container

| Path           | Description   |
| -------------- | ------------- |
| `/app/output`  | This is the Docker path where the audio files will be stored. An external path should be mounted to this Docker path. If a custom path is needed, it can be defined using the `BV_PATH` environment variable. |

| Variable      | Description   | Default Value |
| ------------- | ------------- | ------------- |
| `BV_PATH`     | The path where the audio files will be stored. | `/app/output` |
| `BV_LANGUAGE` | The language of the audio tracks. Can be set to either `BM` or `NN`. | `BM` |

## Usage
The container uses crontab to run the script once a day at 05:00. The logs will print 'Success' or error messages after each run is completed. The Bible verse is saved to two files: one named ``latest.mp3`` and another with the date and language specified, e.g., ``010124_BM.mp3``. The ``latest.mp3`` can be used in automations to represent the latest Bible verse downloaded.

# Attribution
<a href="https://www.flaticon.com/free-icons/bible" title="bible icons">Bible icons created by Smashicons - Flaticon</a>