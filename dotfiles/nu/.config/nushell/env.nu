def yy [msg?: string] {
  if $msg == null {
    yazi
  } else {
    yazi $msg
  }
}

def c [] {
  clear
}

def la [msg?: string] {
  if $msg == null {
    ls -a
  } else {
    ls -a $msg
  }
}

def sps [msg: string] {
  sudo pacman -S $msg
}

def spr [msg: string] {
  sudo pacman -Rns $msg
}

def spy [] {
  sudo pacman -Suuy
}

def lg [] {
  lazygit
}
