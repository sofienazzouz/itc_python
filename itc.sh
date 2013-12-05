#!/bin/bash

USERNAME="$2"
PASSWORD="$3"
APP_SKU="$4"
APP_NAME=$APP_SKU'.itmsp'
APP_VERSION=$5

if [ "$1" = "fetch" ]; then # download package that contain metadata.xml
    /Applications/Xcode.app/Contents/Applications/Application\Loader.app/Contents/MacOS/itms/bin/iTMSTransporter -m lookupMetadata -u $USERNAME -p $PASSWORD -vendor_id $APP_SKU -destination .
    if [ "$?" = "0" ]; then
        echo "Success! Metadata downloaded."
    fi
else
    if [ "$1" = "update" ]; then #execute update script the verifie the new metadata.xml
        # update screeshots
        python screenshots_updater.py $APP_SKU $APP_VERSION
        /Applications/Xcode.app/Contents/Applications/Application\Loader.app/Contents/MacOS/itms/bin/iTMSTransporter -m verify -f $APP_NAME  -u $USERNAME -p $PASSWORD
        if [ "$?" = "0" ]; then #if verification success then upload the new metadata.xml
            /Applications/Xcode.app/Contents/Applications/Application\Loader.app/Contents/MacOS/itms/bin/iTMSTransporter -m upload -f $APP_NAME -u $USERNAME -p $PASSWORD
        else
            echo "ERROR: Invalid metadata!"
        fi
    else
        echo "Please choose an action: fetch or update"
        echo "Ex: ./itc.sh fetch [username] [password] [app_sku]"
        echo "Ex: ./itc.sh update [username] [password] [app_sku] [app_version]"
        echo "Note: Make sure [app_version] is editable in iTunes Connect"
    fi
fi

