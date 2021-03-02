# WebScrapping
This application opens this [laptop selling url](https://www.flipkart.com/computers/monitors/pr?sid=6bo%2C9no&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_0a4329f6-060a-460c-aff5-e710c5660a0e_1_372UD5BXDFYS_MC.ECL5SFI77NSY&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Electronics%7EComputer%2BPeripherals%7EMonitors_ECL5SFI77NSY&cid=ECL5SFI77NSY&sort=popularity) and scraps the item name, rating, and price for each laptop on the first page and saves them to a cvs file.  The basic source code for this project was found [here](https://www.edureka.co/blog/web-scraping-with-python/).

# Running
All dependencies were managed with pipenv. To install them, run ```pipenv install``` while in the folder containing this code. If that is done, run ```pipenv shell``` to enter the virtual env that holds all dependencies. This will download any of these dependencies that are not present on the current machine, but only for this shell/virtual environment.
