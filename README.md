# TwitchCon Attendees List

List all TwitchCon attendees in a PDF using Typst, Pillow and a Twitch endpoint.

The [TwitchCon Who's Coming](https://www.twitchcon.com/rotterdam-2025/whos-coming/) page only shows random streamers on each page load. I wanted a way to see the full list.

Requires Python 3.12 with some dependencies and the Inter font. Customization options (like changing the font) can be found in `main.py` and `main.typ`.

## How to run
1. Install dependencies
    ```sh
    uv sync
    ```

2. Run project
    ```sh
    uv run main.py
    ```