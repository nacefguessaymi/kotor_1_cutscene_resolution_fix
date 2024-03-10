import shutil as sh


def initial(path):
    file = path + "\\swkotor.exe"
    return file

def backup_file(file):
    sh.copy2(file,exe_path +'\\swkotor_backup.exe')

def hex_resolution_code(height,width):
    height_hex_value = "0" + "{0:x}".format(height)
    width_hex_value = "0" + "{0:x}".format(width)
    exe_value_height = height_hex_value[2:4] + height_hex_value[0:2]
    exe_value_width = width_hex_value[2:4] + width_hex_value[0:2]
    return exe_value_height, exe_value_width


def find_and_replace(file, exe_height,exe_width):
    first_string = "00007515813dd8d17800" 
    second_string = "0000c7442410" 

    with open(file, 'rb') as f:
        exe_hex_code = f.read().hex()

    first_position = exe_hex_code.find(first_string)-4
    first_old_values = exe_hex_code[first_position:first_position+28]
    first_new_values = exe_height + first_string + exe_width

    second_position = exe_hex_code.find(second_string)-4
    second_old_values = exe_hex_code[second_position:second_position+20]
    second_new_values = exe_height + second_string + exe_width


    exe_hex_code = exe_hex_code.replace(first_old_values,first_new_values)
    exe_hex_code = exe_hex_code.replace(second_old_values,second_new_values)


    with open(file, 'wb') as f:
        f.write(bytes.fromhex(exe_hex_code))



if __name__ == '__main__':
    exe_path = input("Enter your swkotor.exe file path: ")
    user_height = int(input("Enter your height resolution in pixels (ex: 1920 for 1080p): "))
    user_width = int(input("Enter your width resolution in pixels (ex: 1080 for 1080p): "))
    [exe_height,exe_width] = hex_resolution_code(user_height,user_width)
    original = initial(exe_path)
    backup_file(original)
    find_and_replace(original,exe_height,exe_width)