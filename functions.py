from streamlit.components.v1 import html
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import io
import pandas as pd
def click_element(element):
    open_script = f"<script type = 'text/javascript'>window.parent.document.querySelector('[id^=tabs-bui][id$=-{element}]').click();</script>"
    html(open_script, width=0, height=0)


sample = {'Body Type': 2,
 'Sex': 0,
 'How Often Shower': 1,
 'Social Activity': 2,
 'Monthly Grocery Bill': 230,
 'Frequency of Traveling by Air': 2,
 'Vehicle Monthly Distance Km': 210,
 'Waste Bag Size': 2,
 'Waste Bag Weekly Count': 4,
 'How Long TV PC Daily Hour': 7,
 'How Many New Clothes Monthly': 26,
 'How Long Internet Daily Hour': 1,
 'Energy efficiency': 0,
 'Do You Recyle_Paper': 0,
 'Do You Recyle_Plastic': 0,
 'Do You Recyle_Glass': 0,
 'Do You Recyle_Metal': 1,
 'Cooking_with_stove': 1,
 'Cooking_with_oven': 1,
 'Cooking_with_microwave': 0,
 'Cooking_with_grill': 0,
 'Cooking_with_airfryer': 1,
 'Diet_omnivore': 0,
 'Diet_pescatarian': 1,
 'Diet_vegan': 0,
 'Diet_vegetarian': 0,
 'Heating Energy Source_coal': 1,
 'Heating Energy Source_electricity': 0,
 'Heating Energy Source_natural gas': 0,
 'Heating Energy Source_wood': 0,
 'Transport_private': 0,
 'Transport_public': 1,
 'Transport_walk/bicycle': 0,
 'Vehicle Type_None': 1,
 'Vehicle Type_diesel': 0,
 'Vehicle Type_electric': 0,
 'Vehicle Type_hybrid': 0,
 'Vehicle Type_lpg': 0,
 'Vehicle Type_petrol': 0}

def input_preprocessing(data):
    data["Body Type"] = data["Body Type"].map({'Underweight':0, 'Normal':1, 'Overweight':2, 'Obese':3})
    data["Sex"] = data["Sex"].map({'Female':0, 'Male':1})
    data = pd.get_dummies(data, columns=["Diet","Heating Energy Source","Transport","Vehicle Type"], dtype=int)
    data["How Often Shower"] = data["How Often Shower"].map({'Less frequently':0, 'Daily':1, "Twice a day":2, "More frequently":3})
    data["Social Activity"] = data["Social Activity"].map({'Never':0, 'Sometimes':1, "Often":2})
    data["Frequency of Traveling by Air"] = data["Frequency of Traveling by Air"].map({'Never':0, 'Rarely':1, "Frequently":2, "Very Frequently":3})
    data["Waste Bag Size"] = data["Waste Bag Size"].map({'Small':0, 'Medium':1, "Large":2,  "Extra large":3})
    data["Energy efficiency"] = data["Energy efficiency"].map({'No':0, 'Sometimes':1, "Yes":2})
    return data
def hesapla(model,ss, sample_df):
    copy_df = sample_df.copy()
    travels = copy_df[["Frequency of Traveling by Air",
                         "Vehicle Monthly Distance Km",
                         'Transport_Private',
                          'Transport_Public',
                          'Transport_Walk',
                          'Transport_Bicycle',
                          'Vehicle Type_None',
                          'Vehicle Type_Diesel',
                          'Vehicle Type_Electric',
                          'Vehicle Type_Hybrid',
                          'Vehicle Type_Liquified Petroleum Gas',
                          'Vehicle Type_Petrol']]
    copy_df[list(set(copy_df.columns) - set(travels.columns))] = 0
    travel = np.exp(model.predict(ss.transform(copy_df)))

    copy_df = sample_df.copy()
    energys = copy_df[[ 'Heating Energy Source_coal','How Often Shower', 'How Long TV PC Daily Hour',
                         'Heating Energy Source_Electricity','How Long Internet Daily Hour',
                         'Heating Energy Source_Natural gas',
                         'Cooking_with_Stove',
                          'Cooking_with_Oven',
                          'Cooking_with_Microwave',
                          'Cooking_with_Grill',
                          'Cooking_with_Airfryer',
                         'Heating Energy Source_Wood','Energy efficiency']]
    copy_df[list(set(copy_df.columns) - set(energys.columns))] = 0
    energy = np.exp(model.predict(ss.transform(copy_df)))

    copy_df = sample_df.copy()
    wastes = copy_df[[  'Do You Recyle_Paper','How Many New Clothes Monthly',
                         'Waste Bag Size',
                         'Waste Bag Weekly Count',
                         'Do You Recyle_Plastic',
                         'Do You Recyle_Glass',
                         'Do You Recyle_Metal',
                         'Social Activity',]]
    copy_df[list(set(copy_df.columns) - set(wastes.columns))] = 0
    waste = np.exp(model.predict(ss.transform(copy_df)))

    copy_df = sample_df.copy()
    diets = copy_df[[ 'Diet_Omnivore',
                     'Diet_Pescatarian',
                     'Diet_Vegan',
                     'Diet_Vegetarian', 'Monthly Grocery Bill','Transport_Private',
                     'Transport_Public',
                     'Transport_Walk','Transport_Bicycle',
                      'Heating Energy Source_Coal',
                      'Heating Energy Source_Electricity',
                      'Heating Energy Source_Natural gas',
                      'Heating Energy Source_Wood',
                      ]]
    copy_df[list(set(copy_df.columns) - set(diets.columns))] = 0
    diet = np.exp(model.predict(ss.transform(copy_df)))
    hesap = {"Travel": travel[0], "Energy": energy[0], "Waste": waste[0], "Diet": diet[0]}

    return hesap


def chart(model, scaler,sample_df, prediction):
    p = hesapla(model, scaler,sample_df)
    bbox_props = dict(boxstyle="round", facecolor="white", edgecolor="white", alpha=0.7)

    plt.figure(figsize=(10, 10))
    patches, texts = plt.pie(x=p.values(),
                             labels=p.keys(),
                             explode=[0.03] * 4,
                             labeldistance=0.75,
                             colors=["#29ad9f", "#1dc8b8", "#99d9d9", "#b4e3dd" ], shadow=True,
                             textprops={'fontsize': 20, 'weight': 'bold', "color": "#000000ad"})
    for text in texts:
        text.set_horizontalalignment('center')

    data = io.BytesIO()
    plt.savefig(data, transparent=True)

    background = Image.open("./media/default.png")
    draw = ImageDraw.Draw(background)
    font1 = ImageFont.truetype(font="./style/ArchivoBlack-Regular.ttf", size=50)
    font = ImageFont.truetype(font="./style/arialuni.ttf", size=50)
    draw.text(xy=(320, 50), text=f"  How big is your\nCarbon Footprint?", font=font1, fill="#039e8e", stroke_width=1, stroke_fill="#039e8e")
    draw.text(xy=(370, 250), text=f"Monthly Emission \n\n   {prediction:.0f} kgCO₂e", font=font, fill="#039e8e", stroke_width=1, stroke_fill="#039e8e")
    data_back = io.BytesIO()
    background.save(data_back, "PNG")
    background = Image.open(data_back).convert('RGBA')
    piechart = Image.open(data)
    ayak = Image.open("./media/ayak.png").resize((370, 370))
    bg_width, bg_height = piechart.size
    ov_width, ov_height = ayak.size
    x = (bg_width - ov_width) // 2
    y = (bg_height - ov_height) // 2
    piechart.paste(ayak, (x, y), ayak.convert('RGBA'))
    background.paste(piechart, (40, 200), piechart.convert('RGBA'))
    data2 = io.BytesIO()
    background.save(data2, "PNG")
    background = Image.open(data2).resize((700, 700))
    data3 = io.BytesIO()
    background.save(data3, "PNG")
    return data3
