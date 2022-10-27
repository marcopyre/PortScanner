install:
	@echo 'Building for Linux... '
	pacman -S rustscan
	mkdir /usr/share/PortScanner/
	cp main.py /usr/share/PortScanner/PortScanner
	echo 'python /usr/share/PortScanner/PortScanner' > /usr/local/bin/portscanner
	chmod +x /usr/local/bin/portscanner
