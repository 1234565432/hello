import media
import fresh_tomatoes
toy = media.Movie('toy',
                  'aiqiyi',
                  'a toy come to life'
                 'http://pic61.nipic.com/file/20150309/4614066_191939440318_2.jpg',
                 'http://www.iqiyi.com/')
avatar = media.Movie('avatar',
                     'avatar',
                     'ailient story'
                    'http://epaper.hf365.com/dtb/res/1/1541/2017-09/28/A08/res04_attpic_brief.jpg',
                    'http://my.tv.sohu.com/us/1853171/5092831.shtml')
movie = [toy, avatar]
fresh_tomatoes.open_movies_page(movie)
