#!/usr/bin/env bash
# Prepare my webservers (web-01 & web-02)

# uncomment for easy debugging
# set -x

# colors
blue='\e[1;34m'
green='\e[1;32m'
reset='\033[0m'

echo -e "${blue}Updating and doing some minor checks...${reset}\n"

# install nginx if not present
if [ ! -x /usr/sbin/nginx ]; then
	sudo apt-get update -y -qq && \
	     sudo apt-get install -y nginx
fi

echo -e "\n${blue}Setting up some minor stuff.${reset}\n"

# Create directories...
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/

# create index.html for test directory
echo "<h1>Welcome<\h1>" | sudo dd status=none of=/data/web_static/releases/test/index.html

# create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# give user ownership to directory
sudo chown -R ubuntu:ubuntu /data/

# backup default server config file
sudo cp /etc/nginx/sites-enabled/default nginx-sites-enabled_default.backup

# Set-up domain.tech/hbnb_static to redirect
# to the content of /data/web_static/current
sudo sed -i '44i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html index.htm;\n\t}\n' /etc/nginx/sites-available/default

# restart Nginx after updating the configuration
sudo service nginx stop
sudo service nginx start

echo -e "${green}Completed${reset}"
exit 0
