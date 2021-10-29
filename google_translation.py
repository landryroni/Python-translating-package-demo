## demo about 3 python translating package
# for jupyter notebook i will suggest to use 'deep_translator' as it doesn't have any error to deal with
# googletrans need version googletrans==4.0.0.-rc1 or googletrans==3.1.0a0 atleast

import pandas as pd
from pandas.plotting import table
import matplotlib.pyplot as plt
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




# print(googletrans.LANGUAGES), to check all available langguage
#deep_translator can be apply on full.txt file,



#let's create a pandas table

color_df = pd.DataFrame({
    "Zh-Color":["红",'绿','黄','白','黑']
})

#?print(color_df)

## Let's try deep_translator
deep_translator = GoogleTranslator(source='auto',target='en')
color_df['En_Color']=color_df['Zh-Color'].apply(lambda x: deep_translator.translate(x))

# Let's try with googletrans translating our column to spanish 
google_trans = Translator()
color_df['Sp_Color'] = color_df['Zh-Color'].apply(google_trans.translate,src='zh-TW', dest='es').apply(getattr,args=('text',))
print("color spainish translator:",color_df)

# Let's try with google_trans_new translating our column to french  
translator = google_translator()
color_df['Fr_Color'] = color_df['Zh-Color'].apply(translator.translate,lang_src='zh', lang_tgt='fr')

# print the final result with translated columns
print("color_df with translation(english,spanish and french) columns added french translator:",color_df)

# save our color_df as a
fig, ax = plt.subplots(figsize=(12, 2)) # set size frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis
ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
tabla = table(ax, color_df, loc='upper right', colWidths=[0.17]*len(color_df.columns))  # where df is your data frame
tabla.auto_set_font_size(False) # Activate set fontsize manually
tabla.set_fontsize(12) # if ++fontsize is necessary ++colWidths
tabla.scale(1.2, 1.2) # change size table
#save our color_df table as png
plt.savefig('color.png')

# googletrans you will in some cases encounter error such as :
# File "/Users/iuliiakrylova/miniconda3/lib/python3.9/json/decoder.py", line 340, in decode
#     raise JSONDecodeError("Extra data", s, end)
# json.decoder.JSONDecodeError: Extra data: line 1 column 296 (char 295)
# to solve this error (https://www.buzzphp.com/posts/python-google-trans-new-translate-raises-error-jsondecodeerror-extra-data):
# There is already an open git issue for this. The workaround for it is:
# Change line 151 in google_trans_new/google_trans_new.py which is: response = (decoded_line + ']') to response = decoded_line



# for more translating package you check these
#https://github.com/ssut/py-googletrans
#https://github.com/mouuff/mtranslate
#https://github.com/Animenosekai/translate
#https://github.com/ffreemt/google-stranslate