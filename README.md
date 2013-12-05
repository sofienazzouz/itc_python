itc_python
==========

iTunes Connect Transporter python script 
Screenshots updater
===================

Dependencies
------------

screenshot_updater.py usese lxml library [Here](http://lxml.de/index.html#download)
. To install it I suggest you create
a virtualenv:

Install steps...

pip install lxml

Note: that libxml and libxslt is required to install lxml


Usage
-----

Create a new version on iTunes Conect <br/>
//app_sku = application name on itunes connect <br/>
1. ./itc.sh fetch username password app_sku <br/>
2. Putting screenshots in app_sku.itmsp package, with the right names. See 'Screenshot names' section <br/>
3. ./itc.sh update username password app_sku newversion <br/>
4. Wait between 15 and 30 minutes until the screenshots will be available on iTunes <br/>

Screenshot names
----------------

1. Open app_sku.itmsp package. <br/>
2. copy paste all screenshots with the following names <br/>
   for ipad : ipad1, ipad2, ipad3, ipad4, ipad5 <br/>
   for iphone4 : iphone4_1, iphone4_2, iphone4_3, iphone4_4, iphone4_5 <br/>
   for iphone5 : iphone5_1, iphone5_2, iphone5_3, iphone5_4, iphone5_5 <br/>
3. Make sure all the screenshots are in PNG format
