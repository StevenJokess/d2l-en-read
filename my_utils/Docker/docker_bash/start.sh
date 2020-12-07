

###
 # @version:
 # @Author:  StevenJokess https://github.com/StevenJokess
 # @Date: 2020-12-07 21:22:44
 # @LastEditors:  StevenJokess https://github.com/StevenJokess
 # @LastEditTime: 2020-12-07 21:22:53
 # @Description:
 # @TODO::
 # @Reference:https://github.com/cedrickchee/dockerfile-fastai/blob/master/docker_base/start.sh
###
#!/bin/bash
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

set -e

# Exec the specified command or fall back on bash
if [ $# -eq 0 ]; then
    cmd=bash
else
    cmd=$*
fi

run-hooks () {
    # Source scripts or run executable files in a directory
    if [[ ! -d "$1" ]] ; then
	return
    fi
    echo "$0: running hooks in $1"
    for f in "$1"/*; do
	case "$f" in
	    *.sh)
		echo "$0: running $f"
		source "$f"
		;;
	    *)
		if [[ -x "$f" ]] ; then
		    echo "$0: running $f"
		    "$f"
		else
		    echo "$0: ignoring $f"
		fi
		;;
	esac
    echo "$0: done running hooks in $1"
    done
}

run-hooks /usr/local/bin/start-notebook.d
