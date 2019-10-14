import os
import sys

# 获取当前终端的宽度和高度
rows, columns = os.popen('stty size', 'r').read().split()

TERM_WIDTH = int(columns) # 宽度
TERM_HEIGHT = int(rows) # 高度


def blit(s, padding):
    sys.stdout.write(' ' * (padding + 2))
    l = padding + 2
    words = s.split(' ')
    for word in words[:-1]:
        if l + len(word) >= TERM_WIDTH - padding:
            sys.stdout.write('\n' + ' ' * padding)
            l = len(word) + 1 + padding
        else:
            l += len(word) + 1
        sys.stdout.write(word + ' ')
    sys.stdout.write(words[-1])

if __name__ == "__main__":
    s = ''' Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sagittis vitae et leo duis. Amet purus gravida quis blandit turpis cursus in hac. Non odio euismod lacinia at quis risus sed vulputate. Consequat nisl vel pretium lectus. Ut faucibus pulvinar elementum integer. Tincidunt lobortis feugiat vivamus at augue eget arcu dictum varius. A erat nam at lectus urna. Nisl vel pretium lectus quam id leo. Sit amet venenatis urna cursus eget nunc scelerisque. Nibh sed pulvinar proin gravida. Cras pulvinar mattis nunc sed blandit libero volutpat. Donec adipiscing tristique risus nec feugiat in fermentum posuere urna. Sed augue lacus viverra vitae congue eu consequat ac felis. Aliquet nec ullamcorper sit amet risus nullam eget. Nibh cras pulvinar mattis nunc sed blandit. Ut aliquam purus sit amet. Adipiscing elit ut aliquam purus. Mauris a diam maecenas sed.
Pellentesque sit amet porttitor eget dolor morbi non arcu. Faucibus in ornare quam viverra orci sagittis eu volutpat odio. Nascetur ridiculus mus mauris vitae ultricies. Feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper. Nullam vehicula ipsum a arcu cursus. Ultrices in iaculis nunc sed augue lacus viverra vitae. Nunc sed id semper risus in hendrerit gravida rutrum. Placerat in egestas erat imperdiet. Mi bibendum neque egestas congue quisque. In egestas erat imperdiet sed euismod nisi porta. Suspendisse interdum consectetur libero id faucibus. Vel elit scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. Tincidunt lobortis feugiat vivamus at. Enim tortor at auctor urna nunc. Purus viverra accumsan in nisl nisi scelerisque eu ultrices vitae. Orci dapibus ultrices in iaculis nunc sed augue. Purus ut faucibus pulvinar elementum integer enim neque volutpat. '''
    blit(s, 3)
