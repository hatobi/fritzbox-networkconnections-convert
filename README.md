# fritzbox-networkconnections-convert
convert Fritz!Box' network connections list into a csv

There is no simple way to export all network connections from an AVM Fritz!Box. Backups only contain active devices and the web interface does not offer an export.

This python script takes the site's HTML and converts it into a CSV-file.

## Steps

1. Open Fritz!Box' network connections tab
2. Inspect the site's HTML, find class  ```flexTable netOverviewTable zebra```
3. Copy everything inside of div with class  ```flexTable netOverviewTable zebra```
4. Create a new HTML-file with the copied contents
5. Run conversion-script on that file
