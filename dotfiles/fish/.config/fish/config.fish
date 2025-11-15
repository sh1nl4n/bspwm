if status is-interactive
	set -x JAVA_HOME /usr/lib/jvm/default-runtime/
    set -x PATH $JAVA_HOME/bin $PATH
end

alias spr="sudo pacman -Rns"
alias sps="sudo pacman -S"
alias spy="sudo pacman -Syu"
alias yy="yazi"
alias cat="bat --theme=base16"
alias ls='eza --icons=always --color=always'
alias ll='eza --icons=always --color=always -la'
alias la="eza --icons=always --color=always -a"
alias lg="lazygit"
