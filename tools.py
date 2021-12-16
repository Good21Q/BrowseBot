import os

def remove_html(to_clean):
    count = 0
    html_cache = ''
    result = ''
    is_style = False
    for a in to_clean:
        if a == '<' or a == '>':
            count += 1
            if a == '>':
                if 'style' in html_cache:
                    is_style = not is_style
                html_cache = ''
            continue
        if (count%2 == 0 or count == 0) and not is_style:
            result += a
        else:
            html_cache += a
    return result

def read_inner_body(html):
    result = ''
    count = 0
    html_cache = ''
    body_read = False
    for a in html:
        if a == '<' or a == '>':
            count += 1
            continue
        if count == 1 or count%2 == 1:
            html_cache += a
        else:
            if html_cache == 'body':
                body_read = True
                html_cache = ''
            elif html_cache == '/body':
                body_read = False
                break
            elif len(html_cache) != 0:
                html_cache = ''
        if body_read and count%2==0:
            result += a
    return result

def copy_file(root_path, target_path):
    with open(root_path, 'rb') as f:
        read_bytes = f.read()
    with open(target_path, 'wb') as f:
        f.write(read_bytes)

def is_auto(user):
    path = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    path += r'\BBot.lnk'
    if os.path.exists(path):
        return True
    return False

def set_auto(user):
    path = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    copy_file('./BBot.lnk', path + '\\BBot.lnk')
    print('Succefully set auto-start')

            
