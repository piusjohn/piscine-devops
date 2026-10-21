cat << 'EOF' > show-info.sh
#!bin/bash
cat -e << END
The current directory is: $PWD
The default paths are: $PATH
The current user is: $USERNAME
END
EOF