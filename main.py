from PIL import Image, ImageDraw, ImageFont #Модуль ImageDraw -> отрисовка, # ImageFont -> для параметра шрифта и отрисовки текста.
bgcolor=Image.new('RGB', (1000, 1000), (96, 141, 209)) #Фон для заднего фона
draw = ImageDraw.Draw(bgcolor)
Font = ImageFont.truetype('11874.ttf', size=32) # Параметры шрифта для отрисовки текста
draw.text((350, 20), 'Отрисовка фигур с помощью PIL(Pillow)', font=Font, fill='black') # Отрисовка текста
draw.ellipse((1, 1, 300, 300), fill='red', outline=(0, 0, 0), width=2) #отрисовка эллипса x0, y0 -> от края окна; x1, y1 -> размеры самого эллипса
draw.rectangle((20,310,450,550), fill = 'yellow', outline=(0,0,0), width=2) # отрисовка прямогульника
#bgcolor.save('draw-ellipse-rectangle-line.jpg', quality=95) # создание картинки с нарисованными фигурами
bgcolor.show()
