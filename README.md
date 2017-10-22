# cryptocurrencyrc
![CryptocurrencyrcPreview](https://raw.githubusercontent.com/x90-nop/cryptocurrencyrc/master/images/a2.png)
 Conky widget to keep you updated with Bitcoin,Ethereum,and Monero prices(currencies can be changed and added,as described bellow). If you enjoy the widget please contribute! Pull requests are appreciated,as are donations of ANY amount. My Bitcoin address: `1Q9MxXPcLJ654u1o6F7YRxBB3HnMRZvRBf`  
 Fiat currency conversion script by alexprengere: https://github.com/alexprengere/currencyconverter
## Downloading and running
 Dependencies:
* Conky
* python

 Clone our repository:
```
git clone https://github.com/x90-nop/cryptocurrencyrc
```
 Running the widget:
```
cd cryptocurrencyrc
conky -c conkyrc
```

## Changing currencies
 You can easily change one of the three currencies available:
 * Download the currency's logo to the `images` folder
 * Change the respective `color` and `image` lines in the `conkyrc` file
 * Change the currency name after `voffset` and in the `exec` variable
 To add a new currency,create a new `color` line,copy and paste one of the lines bellow `TEXT` and do the same procedure.

## Fiat currency conversion
 Default currency is USD. To convert the currency add the `--convert-to` argument to the `exec` variables in the conkyrc. Then change the `$$` just before `exec` to match your new currency(`$$`=`$` to conky):
```
$$${exec python scripts/crypto.py -c bitcoin}
```
 to
```
R$$${exec python scripts/crypto.py -c bitcoin --convert-to BRL}
```
 If the conversion values are outdated replace `eurofxref-hist.csv`(scripts folder): https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip
## Running on startup
 Save the following script and configure your system to execute it on startup.On Ubuntu-based systems you can usually do that on the "Startup Application Preferences" or "Applications" window.
```
#!/bin/bash
cd ~/path/to/rc/ && conky -c conkyrc
```
## Adjusting widget position on screen
 Open the conkyrc file with your favorite text editor.
```
nano conkyrc
```
 First off,to adjust the general position change the alignment from `top_right` to `top_left`, `top_right`, `top_middle`, `bottom_left`, `bottom_right`, `bottom_middle`,`middle_left`, `middle_middle` or `middle_right`.Then adjust `gap_x X` and `gap_y Y` settings to your preference.
 You can also adjust the spacing between each object by changing the settings in the end of the file: `offset`,`voffset`,`alignr` and `-p x,y` for the images.

## License
 This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.
