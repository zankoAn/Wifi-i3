# Wifi-i3
This is a GUI app to connect Wifi in window manager i3 on linux And other places !!
<br />
<br />
<br />


![Wifi-i3](https://user-images.githubusercontent.com/45467643/122683043-252ecb00-d212-11eb-95dc-44bf90ac55e6.png)


<br />
<br />
### Requirements

> 
> - python >= 3.8
> - NetworkManager
> - nmcli
> - notify-send and dunstrc file

<br />
<br />
### Instalation

> - pip install -r requirements.txt
> - sudo pacman -S networkmanager
> - sudo pacman -S dunst
> - dunst --start -conf dunctrc

<br />
<br />
### i3 Config

If you are using i3 Window Manager, you can follow the instructions below.

Add the following line to the i3 config file

> exec --no-startup-id dunst -config ~/.i3/dunstrc

<br />
<br />
### i3blocks config
If you are using i3block, you can add the following lines to the i3blocks.conf

> ########################################
> 
> \#          Iface Config                \#
> 
> ########################################
> 
> [State]
> 
> full_text=" "
> 
> command=~/Wifi-i3/wifi.py
> 
> separator_block_width=0
> 
> border_top=0
> 
> border_left=0
> 
> border_right=0
> 
> border_bottom=3
> 
> border=#33bd96
> 
> color=#33bd96

<br />
<br />
<br />
### Note 

- _To use this tool you need to set the **wifi.py  PATH** inside the **i3blocks.conf**  (command=wifi.py) , you must also move the **dunstrc** file to **~/.i3/** (If your i3 config is here) and **chmod +x wifi.py**_

