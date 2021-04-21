import os

from PIL import Image


def render_transparency(file_name, new_path):
    new_data = []
    image = Image.open(file_name)
    image = image.convert('RGBA', colors=255)
    data = image.getdata()

    for item in data:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    image.putdata(new_data)

    image.save(new_path, 'PNG')


def set_images():
    for file_name in os.listdir(os.getcwd()):
        src = file_name.strip('.bmp')
        new_path = "export/" + src + '.png'
        render_transparency(file_name, new_path)


def main():
    if not os.path.isdir("export/"):
        os.mkdir("export/")

    set_images()


if __name__ == '__main__':
    main()
