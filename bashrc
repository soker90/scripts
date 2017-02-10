#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return


# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias updatemirror='sudo reflector --sort rate -l 5 --save /etc/pacman.d/mirrorlist && yaourt -Syyu --aur --devel'
alias xampp='sudo /opt/lampp/manager-linux-x64.run'
alias vista='redshift -l 38.984829:-3.927378 &'
PS1='[\u@\h \W]\$ '
export PATH=$PATH:/opt/android-sdk/platform-tools/
export ANDROID_HOME=/opt/android-sdk
export JAVA_HOME=/usr/lib/jvm/java-8-jdk/

alias infoxfs='xfs_db -c frag -r /dev/sdb6'
alias defragxfs='xfs_fsr /dev/sdb6'
