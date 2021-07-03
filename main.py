from PIL import Image, ImageDraw
#Фон для заднего фона
bgcolor=Image.new('RGB', (1000, 1000), (96, 141, 209))
draw = ImageDraw.Draw(bgcolor)
draw.ellipse((1, 1, 300, 300), fill='black', outline=(0, 0, 0)) #отрисовка эллипса x0, y0 -> от края окна; x1, y1 -> размеры самого эллипса
#draw.rectangle((10,450,300,150), fill = 'pink', outline=(0,0,0))
#bgcolor.save('draw-ellipse-rectangle-line.jpg', quality=95)
bgcolor.show()
