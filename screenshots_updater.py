import os
import sys
import hashlib
from lxml import etree

def get_screenshots(source, size):
    """ prepare list files names sizes and md5 crypting"""
    listmd5 = []
    listsize = []

    if size == "iphone4":
        listfiles = ["iphone4_1.png","iphone4_2.png","iphone4_3.png","iphone4_4.png","iphone4_5.png"]
    elif size == "iphone5":
        listfiles = [ "iphone5_1.png", "iphone5_2.png", "iphone5_3.png", "iphone5_4.png","iphone5_5.png"]
    elif size == "ipad":
        listfiles = ["ipad1.png", "ipad2.png", "ipad3.png", "ipad4.png", "ipad5.png"]

    for i in listfiles:
        hhash = hashlib.md5(open(source+"/"+i).read()).hexdigest()
        listmd5.append(hhash)
        size = os.path.getsize(source+"/"+i)
        listsize.append(size)

    return (listfiles, listmd5, listsize)

def main(path, version_num):
    # Use the same namespace for all etree queries
    ns = {'ns':'http://apple.com/itunes/importer'}

    l_files_iphone4, l_hashs_iphone4, l_sizes_iphone4 = get_screenshots(path, "iphone4")
    l_files_iphone5, l_hashs_iphone5, l_sizes_iphone5 = get_screenshots(path, "iphone5")
    l_files_ipad, l_hashs_ipad, l_sizes_ipad = get_screenshots(path, "ipad")

    root = etree.parse(path + '/metadata.xml')
    versions = root.find(".//ns:software/ns:software_metadata/ns:versions", namespaces=ns)

    for v in versions.xpath(".//ns:version", namespaces=ns):

        version_attribute = v.attrib['string']
        if version_attribute != version_num:
            versions.remove(v)  #deleting all other versions

    for locale in root.findall(".//ns:software/ns:software_metadata/ns:versions/ns:version/ns:locales/ns:locale", namespaces=ns):
        screenshots = locale.find(".//ns:software_screenshots", namespaces=ns)
        # Counter is used  to count screenshots
        counter = 0

        for screenshot in screenshots.findall(".//ns:software_screenshot", namespaces=ns):
            #15 successive screenshot 5 for iphone4 5 for iphone5 5 for ipad
            if counter == 5: #counter should reset to 0 each time he finish screenshots of the mentionned device
                counter = 0
            file_name = screenshot.find(".//ns:file_name", namespaces=ns)
            checksum = screenshot.find(".//ns:checksum", namespaces=ns)
            size = screenshot.find(".//ns:size", namespaces=ns)

            if screenshot.get("display_target") == 'iOS-3.5-in':
                file_name.text = l_files_iphone4[counter]
                checksum.text = l_hashs_iphone4[counter]
                size.text = str(l_sizes_iphone4[counter])
            elif screenshot.get("display_target") == 'iOS-4-in':
                file_name.text = l_files_iphone5[counter]
                checksum.text = l_hashs_iphone5[counter]
                size.text = str(l_sizes_iphone5[counter])
            elif screenshot.get("display_target") == 'iOS-iPad':
                file_name.text = l_files_ipad[counter]
                checksum.text = l_hashs_ipad[counter]
                size.text = str(l_sizes_ipad[counter])
            counter = counter + 1
    output_file = open(path+ '/metadata.xml', 'w' )
    output_file.write(etree.tostring(root, xml_declaration=True, method='xml',
        encoding="UTF-8"))
    output_file.close()

if __name__ == "__main__":
    # name of the package, version number
    main(sys.argv[1] + '.itmsp', sys.argv[2])
