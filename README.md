# fritzbox-networkconnections-convert
There is no simple way to export all network connections from an AVM Fritz!Box as the web interface does not offer an export. You could use the backup-file but it only contains devices connected via cable (LAN) and none of the wireless devices.

This script helps to convert Fritz!Box' network connections list into a CSV-file. In order to use it, you need to manually copy some of the site's HTML-code and run a python-script on your local machine.

## Requirements
- python
- csv-library
- BeautifulSoup-library

## Steps

1. Open Fritz!Box' network connections tab
2. Inspect the site's HTML, find class  ```flexTable netOverviewTable zebra```
3. Copy everything inside of div with class  ```flexTable netOverviewTable zebra```
4. Create a new HTML-file with the copied contents
5. Run conversion-script on that file
