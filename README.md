# imstr

### OverView

[![](https://img.shields.io/badge/lang-python3-red)](https://www.python.org/doc/)
[![](https://img.shields.io/apm/l/vim-mode.svg)](https://github.com/keisukeYamagishi/ImageToStr/blob/master/LICENSE)

Convert take in photos into character strings and display at character strings.

## Supported python3.*

## git clone

***Via SSH***: For those who plan on regularly making direct commits, cloning over SSH may provide a better experience (which requires uploading SSH keys to GitHub):

```
$ mkdir gitrepo

$ cd gitrepo

$ git@github.com:keisukeYamagishi/imstr.git
```

***Via https***: For those checking out sources as read-only, HTTPS works best:

```
$ mkdir gitrepo

$ cd gitrepo

$ git clone https://ithub.com:keisukeYamagishi/imstr.git
```

### use for mac

if there is not homebrew install homebrew  

show homebrew info at https://brew.sh/index_ja.html

open terminal.app

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

set up python for mac

```
$ brew install python3
```

```
$ pip3 install numpy
```

```
$ brew install opencv3
```

# Use it

```
$ python3 ./imstr
Use it this
	imstr path option 
options
	-n html_name
	-v [ Disply this version ]
	-o Not Display output path
Supported image format
	png, jpeg, jpg, jpe
```
## version

```
$ ./bin/imstr -v
imstr version: 2.0.1
```

***create html***

```
$ ./imstr bigbear.jpg 
create path: => /Users/keisukeyamagishi/Code/git/imstr/index.html
Complete
🍺 
```

## Example html

When executed, it is written in index.html.
Here is the file at run time

<img width="542" alt="Screen Shot 2022-03-25 at 18 47 07" src="https://user-images.githubusercontent.com/5553852/160096881-5c616c23-c791-4d9d-9717-afc6ca0d8f3a.png">

create html

[Demo page](https://shichimitoucarashi.com/imstr)
