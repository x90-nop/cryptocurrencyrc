# cryptocurrencyrc
![Cryptocurrencyrc Preview](https://raw.githubusercontent.com/x90-nop/cryptocurrencyrc/master/images/a2.png)
 Conky widget to keep you updated with Bitcoin,Ethereum,and Monero prices(currencies can be changed as described bellow).Drop and appreciation percentages/graphics and  are under development.
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
 First off,to adjust the general position change the alignment from `top_right` to `top_left`, `top_right`, `top_middle`, `bottom_left`, `bottom_right`, `bottom_middle`,`middle_left`, `middle_middle` or `middle_right`.Then adjust `gap_x X` and `gap_y Y` settings to your preference.
 You can also adjust the spacing between each object by changing the settings in the end of the file: `offset`,`voffset`,`alignr` and `-p x,y` for the images.
## Changing currencies
  You can easily change one of the three currencies available. To add a new currency to the list,create a new `color` line,copy and paste one of the lines bellow `TEXT` and do the same procedure:
 * Download the currency's logo to the `images` folder
 * Change the respective `color` and `image` lines in the `conkyrc` file
 * Change the currency name after `voffset` and in the `exec` variable
## Running on startup
 You can either configure your system to execute the following script on startup or just add the second line to your distro's startup direcly.On Ubuntu-based systems you can usually do that on the "Startup Application Preferences" or "Applications" window.
```
#!/bin/bash
cd ~/path/to/rc/ && conky -c conkyrc
```
## License
 This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details
