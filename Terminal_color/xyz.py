from sys import stdout
put = stdout.write

print('\n' + "- " * 16 + "->", "Style")
for style in range(0, 8):
    print("\033[{};32m style-sample \033[0m {}".format(style, style))

print('\n' + "- " * 16 + "->", "Foreground")
for FG in range(30, 38):
    print("\033[0;{}m forground-sample \033[0m {}".format(FG, FG))

print('\n' + "- " * 16 + "->", "Background")
for style in range(40, 48):
    print("\033[0;38;{}m style-sample \033[0m  {}".format(style, style))

txt1 = '\n' + r'text = "'
txt2 = r'\033[X;Y;Zm'
txt3 = r' Some-Text-Here \033[0m"'
put("\033[0;32m{}\033[0m".format(txt1))
put("\033[0;31m{}\033[0m".format(txt2))
put("\033[0;32m{}\033[0m".format(txt3))
print("\nX --> Style")
print("Y --> Foreground")
print("Z --> Background\n")