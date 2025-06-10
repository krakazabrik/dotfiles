import os

# install all pacman packages
os.system('sudo pacman -S --needed git kitty base-devel alacritty wayland waybar chromium neofetch tty-clock flatpak hyprland zsh')

# install aur package manager
os.system('git clone https://aur.archlinux.org/yay.git')
os.system('cd yay')
os.system('makepkg -si')

# install aur packages 

os.system('cd')
os.system('yay -S vscodium github-desktop spotify discord')

# install flatpak packages

os.system('flatpak install flathub com.valvesoftware.Steam')

# install oh my zsh

os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
