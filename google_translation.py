## discussing about 3 python translating package
##
import pandas as pd
from google_trans_new import google_translator
from googletrans import Translator
import googletrans
from deep_translator import (GoogleTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeepL,
                             QCRI,
                             single_detection,
                             batch_detection)




# print(googletrans.LANGUAGES)



#let's create a pandas table

color_df = pd.DataFrame({
    "Color":["红",'绿','黄','白','黑']
})

#?print(color_df)

## Let's try deep_translator
deep_translator = GoogleTranslator(source='auto',target='en')
color_df['En_Color']=color_df['Color'].apply(lambda x: deep_translator.translate(x))

# print('color english translator:',color_df)

# Let's try with googletrans translating our column to spanish 
google_trans = Translator()
color_df['Sp_Color'] = color_df['Color'].apply(google_trans.translate,src='zh-TW', dest='es').apply(getattr,args=('text',))
print("color spainish translator:",color_df)

# Let's try with google_trans_new translating our column to french  
translator = google_translator()
color_df['Fr_Color'] = color_df['Color'].apply(translator.translate,lang_src='zh', lang_tgt='fr')#.apply(getattr,args=('text',))
print("color french translator:",color_df)

# translator = google_translator()  
# translate_text = translator.translate('สวัสดีจีน',lang_tgt='en') 