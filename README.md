# cryptocurrencyrc
![Cryptocurrencyrc Preview](https://raw.githubusercontent.com/x90-nop/cryptocurrencyrc/master/images/a2.png)
 Conky widget to keep you updated with Bitcoin,Ethereum,and Monero prices.Drop and appreciation percentages not fully implemented yet.
## Downloading and running
```
git clone https://github.com/x90-nop/cryptocurrencyrc
cd cryptocurrencyrc
conky -c conkyrc
```
## Adjusting widget position on screen
 Open the conkyrc file with your favorite text editor.
```
nano conkyrc
```
 First off,to adjust the general position change the "alignment" argument(first line)from `top_right` to `top_left`, `top_right`, `top_middle`, `bottom_left`, `bottom_right`, `bottom_middle`,`middle_left`, `middle_middle` or `middle_right`.Then adjust `gap_x X` and `gap_y Y` settings to your preference.
 You can also adjust the spacing between each object by changing the settings in the end of the file: `offset`,`voffset`,`alignr` and `-p x,y` for the images.
## Running on startup
```
#!/bin/bash
cd ~/path/to/rc/ && conky -c conkyrc
```
You can either configure your system to execute this script on startup or just add that line to your startup direcly.On Ubuntu-based systems you can usually do that on the "Startup Application Preferences" or "Applications" window.
## Price appreciation/drop not showing
```
rm /tmp/cryptorc
```
## License
This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details
