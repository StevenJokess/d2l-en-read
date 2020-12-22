

###
 # @version:
 # @Author:  StevenJokess https://github.com/StevenJokess
 # @Date: 2020-12-22 13:51:10
 # @LastEditors:  StevenJokess https://github.com/StevenJokess
 # @LastEditTime: 2020-12-22 13:51:11
 # @Description:
 # @TODO::
 # @Reference:https://github.com/d2l-ai/d2l-en/blob/master/static/build_html.sh
###
#!/bin/bash

set -e

rm -rf _build/rst _build/html
d2lbook build rst --tab all
cp static/frontpage/frontpage.html _build/rst_all/
d2lbook build html --tab all
cp -r static/frontpage/_images/* _build/html/_images/

for fn in `find _build/html/_images/ -iname '*.svg' `; do
    if [[ $fn == *'qr_'* ]] ; then # || [[ $fn == *'output_'* ]]
        continue
    fi
    # rsvg-convert installed on ubuntu changes unit from px to pt, so evening no
    # change of the size makes the svg larger...
    rsvg-convert -z 1 -f svg -o tmp.svg $fn
    mv tmp.svg $fn
done
