from PIL import Image

def watermark(im, mark, position):
    layer = Image.new("RGBA", im.size, (0,0,0,0))
    layer.paste(mark, position)
    return Image.composite(layer, im, layer)


im = Image.open("Day2Resource\\img\\clungup.jpg")
mark = Image.open("Day2Resource\\watermark.png")
mark = mark.resize((100,100))

out = watermark(im, mark, (0,50))
out.show()
