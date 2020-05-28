# Turnip Price Tracker
> A Discord bot for TheLeague4.0 that tracks members' Animal Crossing: New Horizons Turnip prices

The chatbot lives persistently on a networked Raspberry Pi 3 B+, and takes in user-submitted Turnip prices on a day-to-day basis. These prices are compared user to user, and the top price can be called so any member can see the best place to visit if they'd like to sell their Turnips for profit.  

The bot also has other miscellaneous Discord functionality, which can be triggered by users with the !command, and are all visible to you in the /cogs directory of this repo. 

## Installation

Required Dependences [Linux]:

Python 3.6+
```sh
$ sudo apt-get install python3.6
```

Discord.py:
```sh
python3 -m pip install -U discord.py
```

## Usage example

Submitting a Turnip Price:
```sh
!turnips <price>
```

Checking Turnip Prices:
```sh
!turnips
```

## Release History

* May 11, 2020
  * Implemented !rollNdN to roll a dice
  * Implemented a formatted embed for the !turnips price return
  * Implemented !quickpoll 

* April 22, 2020
  * Implemented Cogs
  * Fixed the Clear function (for real this time)
  * Fixed the Choose command

* April 19, 2020
  * Fixed the calculation for Sundays, buy days now seek out the lowest price
  * Somehow broke the Clear function again. Must investigate...
 

* April 13, 2020
  * Fixed timekeeping to reflect the Noon price reset
  * Fixed the Clear function thanks to some community help

* April 9, 2020
   * Added Issue Tracking to the repo
   * Added Sponsorship links to the top-bar

* April 8, 2020
    * Work in progress
    * Tracks basic Turnip Sale prices daily
    * No Sunday support for buying Turnips

## Meta

James D. – [@TuckingFypos](https://twitter.com/tuckingfypos)

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y81LHJL)


## Contributing

1. Fork it (<https://github.com/tuckingfypos/turnip-price-tracker/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
