#!/bin/sh

echo "Reboot needed to apply changes"

printf "Do you want to reboot now? (y/n): "
read -r choice
case "$choice" in
yes | Yes | y | Y)
	echo "Rebooting now..."
	sudo systemctl reboot
	;;
no | No | n | N)
	echo "Reboot canceled."
	;;
*)
	echo "Invalid input. Please enter yes or no."
	;;
esac
