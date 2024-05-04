# Wallpaper Downloader

This Python script allows you to download wallpapers from the website [WallpaperFlare](https://www.wallpaperflare.com/) based on a specified keyword. The script utilizes asynchronous programming techniques with the `asyncio` and `aiohttp` libraries to achieve faster download speeds.

## Features

- **Asynchronous Downloading**: The script leverages asynchronous programming to download multiple wallpapers concurrently, resulting in faster download times.
- **Keyword Search**: You can search for wallpapers based on a specific keyword or phrase.
- **Customizable Download Quantity**: You can choose to download a specific number of wallpapers or fetch as many as possible.
- **Organized Output**: Downloaded wallpapers are saved in a directory named after the search keyword for better organization.
- **Error Logging**: Errors and exceptions encountered during the download process are logged to a file named `scrape.log` for debugging purposes.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.7 or higher
- `aiohttp`
- `requests`
- `beautifulsoup4`

If you don't have these dependencies installed, the script will attempt to install them automatically using `pip`.

## Usage

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script with the following command:

```
python Wallpaper_Downloader.py
```

4. When prompted, enter the keyword or phrase you want to search for wallpapers.
5. If you want to limit the number of wallpapers to download, enter the desired quantity. Otherwise, enter `n` to download as many wallpapers as possible.
6. The script will start downloading the wallpapers and display the progress in the terminal.
7. Once the download is complete, you can find the downloaded wallpapers in the `Images/<keyword>` directory within the project folder.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

This script utilizes the following open-source libraries:

- [aiohttp](https://docs.aiohttp.org/en/stable/) - Asynchronous HTTP client/server for Python
- [requests](https://requests.readthedocs.io/en/latest/) - Python HTTP library for making HTTP requests
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python library for parsing HTML and XML documents

Special thanks to the developers and contributors of these libraries.

