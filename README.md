# ImageToStr

### OverView

[![](https://img.shields.io/badge/language-Python-ff69b4.svg)](https://www.python.org/doc/)
[![](https://img.shields.io/apm/l/vim-mode.svg)](https://github.com/keisukeYamagishi/ImageToStr/blob/master/LICENSE)
[![](https://img.shields.io/badge/Twitter-O--Liker%20Error-blue.svg)](https://twitter.com/O_Linker_Error)

Convert take in photos into character strings and display at character strings.

## Supported python2.7

## git clone

***Via SSH***: For those who plan on regularly making direct commits, cloning over SSH may provide a better experience (which requires uploading SSH keys to GitHub):

```
mkdir gitrepo

cd gitrepo

git cloen git@github.com:keisukeYamagishi/ImageToStr.git

```

***Via https***: For those checking out sources as read-only, HTTPS works best:

```
mkdir gitrepo

cd gitrepo

git clone https://github.com/keisukeYamagishi/ImageToStr.git

```

### use for mac

if there is not homebrew install homebrew  

show homebrew info at https://brew.sh/index_ja.html

open terminal.app

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
tap homebrew/science

```
 brew tap homebrew/science
```

install opencv

```
brew install opencv
```

```
pip install numpy
```

When the following log is output

->> ./imstr 
RuntimeError: module compiled against API version 0xb but this version of numpy is 0x9
Traceback (most recent call last):
  File "./imstr", line 4, in <module>
    from Imgmain import Imgmain
  File "/Users/keisukeyamagishi/Code/git/imstr/Imgmain.py", line 1, in <module>
    from ImageConversion import ImageConversion
  File "/Users/keisukeyamagishi/Code/git/imstr/ImageConversion.py", line 3, in <module>
    import cv2
ImportError: numpy.core.multiarray failed to import

run this

```
sudo pip install numpy --upgrade --ignore-installed
```

# Use it

```
->> ./ImgConver
Use it this
	ImgConver image path [ /home/shichimi/conversion.png ]
	ImgConver -v [ Disply this version ]
Supported image format
	png, jpeg, jpg, jpe

```
## Run

```
->> ./ImgConver -v
ImgConver version: 2.0.1
```

***create html***

```
->> ./ImgConver nakamoto.jpeg
Complete
```

When executed, it is written in index.html.
Here is the file at run time

![](https://github.com/keisukeYamagishi/imstr/blob/master/bigbear.jpg)

create html

![](https://github.com/keisukeYamagishi/imstr/blob/master/Result.png)



[http://shichimitoucarashi.com/ImageToStr/](http://shichimitoucarashi.com/ImageToStr/)
