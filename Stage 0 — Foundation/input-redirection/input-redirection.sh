cat << 'EOF' > show-info.sh
cat -e << 'END'
echo The current directory is: $PWD
echo The default paths are: $PATH
echo The current user is: $USERNAME
END
EOF