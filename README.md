# imstr

### OverView

[![](https://img.shields.io/badge/lang-python3-red)](https://www.python.org/doc/)
[![](https://img.shields.io/apm/l/vim-mode.svg)](https://github.com/keisukeYamagishi/ImageToStr/blob/master/LICENSE)

Convert take in photos into character strings and display at character strings.

## Supported python3.7.4

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
$ ./imstr
Use it this
Usage: xsort [-option] [<path>]
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

![](https://github.com/keisukeYamagishi/imstr/blob/master/Resource/bigbear.jpg)

create html

[Demo page](https://sevens-api.herokuapp.com/bigbear.html)

![](https://github.com/keisukeYamagishi/imstr/blob/master/Resource/Result.png)
