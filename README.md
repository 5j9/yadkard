# Citer

A citation generator tool for Wikipedia. Currently accessible from:\
http://citer.toolforge.org/ (the English version)\
http://yadfa.toolforge.org/ (the Persian version)

## What does it do?

Citer is especially useful for generating citations from Google Books URLs, DOIs (Any Digital object Identifiers) and ISBNs (International Standard Book Numbers).
Additionally, URLs of many major news websites are supported, including:

* The New York Times
* BBC
* Daily Mail
* Daily Mirror
* The Daily Telegraph
* The Huffington Post
* The Washington Post
* The Boston Globe
* Bloomberg Businessweek
* Financial Times
* The Times of India

Special support for the URLs of the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine) is also implemented.

Some other tested and supported Persian web-sites:
* http://www.noormags.ir (نورمگز)
* http://www.noorlib.ir (کتابخانه دیجیتال نور)
* http://www.ketab.ir (خانه كتاب)
* http://socialhistory.ihcs.ac.ir/ (تحقیقات تاریخ اجتماعی)


## Installation

To run Citer on your local computer:

1. Install Python 3.7+
2. Clone the project
3. Install the dependencies using `pip install --user -r requirements.txt`
4. Copy `config.py.example` to `config.py` (You might want to get an NCBI API key and add it to the config file if you're going to use its services)
5. Run `python3 app.py`

If you see html output to your console, this probably means you have
flup installed. You'll need to uninstall it for Citer to run.

If there are no warnings or error messages (and no html is displayed), the main page will be accessible from:\
    http://localhost:5000/

If you experience any problems or have questions, please open a ticket on this repo.

## Language Setting
The default language is English and can be changed to Persian using the setting in the config.py file.
