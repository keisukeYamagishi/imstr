# imstr

### OverView

[![](https://img.shields.io/badge/language-Python-ff69b4.svg)](https://www.python.org/doc/)
[![](https://img.shields.io/apm/l/vim-mode.svg)](https://github.com/keisukeYamagishi/ImageToStr/blob/master/LICENSE)
[![](https://img.shields.io/badge/Twitter-O--Liker%20Error-blue.svg)](https://twitter.com/O_Linker_Error)

Convert take in photos into character strings and display at character strings.

## Supported python2.7

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
$ brew install python
$ cd /usr/local/bin
$ ln -s /usr/local/bin/python2.7 python
$ ls -l /usr/local/bin/python -> python2.7
```

```
$ brew tap homebrew/science
```

install opencv

```
$ brew install opencv
```

```
$ pip install numpy
```

When the following log is output

```
$ ./imstr 
RuntimeError: module compiled against API version 0xb but this version of numpy is 0x9
Traceback (most recent call last):
  File "./imstr", line 4, in <module>
    from Imgmain import Imgmain
  File "/Users/keisukeyamagishi/Code/git/imstr/Imgmain.py", line 1, in <module>
    from ImageConversion import ImageConversion
  File "/Users/keisukeyamagishi/Code/git/imstr/ImageConversion.py", line 3, in <module>
    import cv2
ImportError: numpy.core.multiarray failed to import
```

Please use the following

```
$ sudo pip install numpy --upgrade --ignore-installed
```

# Use it

```
$ ./imstr
Use it this
	imstr [ /home/shichimi/conversion.png ]
options
	-n html_name
	-v [ Disply this version ]
	-o Not Display output path
Supported image format
	png, jpeg, jpg, jpe
```
## version

```
$ ./imstr -v
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

![](https://github.com/keisukeYamagishi/imstr/blob/master/Resource/Result.png)



[http://shichimitoucarashi.com/imstr/](http://shichimitoucarashi.com/imstr/)
