# Pocker <img src="img/logo_black.png" width="80"> 

> Python-based containers engine 


## Highlights

- Downloads ubuntu 16.04 using debootstrap to create a container
	- mkdir /ubuntu_xenial_1604
	- debootstrap --arch=amd64 xenial /ubuntu_xenial_1604 http://archive.ubuntu.com/ubuntu/	 

## Example Usage

```

./Pocker.py run /bin/bash

```

## Functionality: Currently Implemented

- `pocker run`

## Functionality: Not Yet Implemented

- pocker build †
- pocker pull
- pocker images
- pocker ps
- pocker run
- pocker exec
- pocker logs
- pocker commit
- pocker rm / docker rmi

## Disclaimer

Pocker is a third-party app and is not affiliated with Docker.

## Credits

- [Zakaria Benomar](https://github.com/zakaria-ben)
- [Gautham Santhosh](http://github.com/gauthamzz) 


## License

MIT

