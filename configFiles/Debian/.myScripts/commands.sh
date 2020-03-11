#!/bin/bash
# prints the input

function loban() {
  # lolcat banner: display a stylish message!
  echo -e '\n'
  figlet -w 166 -f Bloody $1 | lolcat
  #figlet -w 160 -c -f Bloody $1 | lolcat
}

function xloban() {
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  echo;
  figlet -c -w 166 -f 3d $1 | lolcat
  echo;
}

function pskill() {
  sudo ps aux | fzy | awk '{ print $2 }' | xargs kill
}

#----1---------2---------3---------4---------5---------6---------7---------8---------9--------10
