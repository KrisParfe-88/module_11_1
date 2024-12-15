# Проведем небольшой анализ с помощью библиотеки Pandas
import pandas as pd

df = pd.read_csv('popul.csv', sep=';')
print(df.head(), '\n')
print(df.info(), '\n')
for i in ['all', 'city', 'village']:
    df[i] = df[i].replace(regex={',': '.'})
    df[i] = df[i].astype('float')
print(df.info(), '\n')
print(df.sample(), '\n')
all_max = df['all'].max()
all_min = df['all'].min()
df['city_%'] = round(df['city'] / df['all'], 1)
df['village_%'] = round(df['village'] / df['all'], 1)
print(df.sample(), '\n')
df_max = df.query('all == @all_max').reset_index(drop=True)
df_min = df.query('all == @all_min').reset_index(drop=True)
print(df_max, '\n')
print(df_min, '\n')
print(f'В таблице приведены данные о численности населения в РФ с {df['year'].min()} по {df['year'].max()} годы. '
      f'Наибольшая численность в анализируемом периоде была в {df_max['year'][0]} и {df_max['year'][1]} годах '
      f'и составила {df_max['all'][0]} млн человек. '
      f'Наименьшая численность - в {df_min['year'][0]} году ({df_min['all'][0]} млн человек)')

# Нарисуем график с помощью библиотеки matplotlib
import matplotlib.pyplot as plt

x = df['year']
plt.figure(figsize=(10, 5), layout='constrained')
plt.grid(linestyle='--', alpha=0.5)
plt.plot(x, df['city'], label='Город')
plt.plot(x, df['village'], label='Село')
plt.xticks(range(df['year'].min(), df['year'].max() + 1, 1))
plt.xticks(rotation=90)
plt.xlabel('Год')
plt.ylabel('Численность населения')
plt.title("Динамика численности городского и сельского населения в РФ, млн человек")
plt.legend()
plt.show()

# Сделаем gif с помощью библиотеки PIL
from PIL import Image

im = Image.open("fox.jpg")
print(im.format, im.size, im.mode)

box = (0, 150, 564, 714)
im.crop(box).save("fox_crop.jpg")
fox = Image.open("fox_crop.jpg")
print(fox.format, fox.size, fox.mode)

fox.rotate(90).save('fox_crop_90.jpg')
fox.rotate(180).save('fox_crop_180.jpg')
fox.rotate(270).save('fox_crop_270.jpg')

image_filenames = [
    "fox_crop.jpg",
    "fox_crop_270.jpg",
    "fox_crop_180.jpg",
    "fox_crop_90.jpg",
]
images = [Image.open(filename) for filename in image_filenames]
images[0].save(
    "animated_fox.gif",
    save_all=True,
    append_images=images[1:],
    duration=500,
    loop=0,
)
