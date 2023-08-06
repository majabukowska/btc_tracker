# Bitcoin Tracker

This repository contains a simple Python application for tracking the current price of Bitcoin using an API.

## Files

### `bitcoin_tracker.py`

This file contains the main code for the Bitcoin tracking application. It imports modules and functions from other files and creates a graphical user interface (GUI) window to display the current Bitcoin price.

### `common.py`

This file defines a common variable `btc_api` which holds the API URL for retrieving Bitcoin price data.

### `verify_data.py`

This file provides a function `is_btc_api_available(api)` to verify the availability of the Bitcoin price API by sending a request and checking the response status.

## How to Use

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine using the following command:
`git clone https://github.com/your-username/bitcoin-tracker.git`
3. Navigate to the cloned repository's directory: `cd bitcoin-tracker`
4. Install required dependencies: `pip install requests`
5. Run the Bitcoin tracking application: `python bitcoin_tracker.py`


The application will open a GUI window displaying the current price of Bitcoin in various currencies. The data is retrieved from the API specified in `common.py`. The window also shows the time at which the data was last updated.

