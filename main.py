link = "https://steamcommunity.com/sharedfiles/filedetails/?id="
var = input("All Mods: ")
from library import chrome
brow = chrome()
brow.get("https://google.com")
var = var.split(",")
for line in var:
    brow.execute_script("window.open(arguments[0])", link + line)