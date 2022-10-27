install:
	@echo 'Installing for Arch Linux... '
	pacman -S rustscan
	mkdir /usr/share/PortScanner/
	cp main.py /usr/share/PortScanner/PortScanner
	echo 'python /usr/share/PortScanner/PortScanner' > /usr/local/bin/portscanner
	chmod +x /usr/local/bin/portscanner

uninstall:
	@echo 'Removing app... '
	rm -r /usr/share/PortScanner/
	rm /usr/local/bin/portscanner
	pacman -R rustscan
