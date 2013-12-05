itc_python
==========

iTunes Connect Transporter python script 
Screenshots updater
===================

These scripts do what...

Dependencies
------------

screenshot_updater.py usese lxml library (link). To install it I suggest you create
a virtualenv:

Install steps...

pip install lxml

Note: that libxml and libxslt is required to install lxml


Usage
-----

Create a new version on iTunes Conect
//app_sku = application name on itunes connect
1) ./itc.sh fetch username password app_sku
2) Putting screenshots in app_sku.itmsp package, with the right names. See 'Screenshot names' section
3) ./itc.sh update username password app_sku newversion
4) Wait between 15 and 30 minutes until the screenshots will be available on iTunes

Screenshot names
----------------

1) Open app_sku.itmsp package.
2) copy paste all screenshots with the following names
   for ipad : ipad1, ipad2, ipad3, ipad4, ipad5
   for iphone4 : iphone4_1, iphone4_2, iphone4_3, iphone4_4, iphone4_5
   for iphone5 : iphone5_1, iphone5_2, iphone5_3, iphone5_4, iphone5_5
3) Make sure all the screenshots are in PNG format
