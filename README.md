# pronuncy
English Pronunciation App

#### Dependencies:

> `tkinter` for GUI with `python 3.6`.

> `pygame` for sound playback.

> `cx_freeze` to build executable.

> Pronunciation Audio Files are from Wikimedia Commons under Creative Commons 2.0 and can be downloaded from `http://packs.shtooka.net/eng-wcp-us/mp3/` using a scraper or download .tar from `http://download.shtooka.net/eng-wcp-us_flac.tar` and manually convert .flac to .mp3 . Copy all .mp3 files in `assets/eng-wcp-us/` directory.


#### Building an Executable via `cx_freeze`:

> Edit the `setup.py` file. Replace `<path/to/your/python/>` with the actual path of your python installation directory. e.g. `c:/python36-32`.

> Open this project's directory in cmd and type `python setup.py build` to build the executable. (Works only on Windows).


#### Testing:

> Built and tested on Windows. Works with issues on Linux.


#### Credits:

> Wikimedia Commons for Pronunciation Files (Creative Commons 2.0).
