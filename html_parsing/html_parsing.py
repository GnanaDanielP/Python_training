import os
import pandas as pd
from parsel import Selector
folder_name='D:/html_files'

for file_name in os.listdir(folder_name):
        print('file name------>',file_name)
        file_path=os.path.join(folder_name,file_name)
        print('file_path-------->',file_path)
        with open(file_path,'r',encoding='utf-8-sig')as file:
            html_data=file.read()
        response=Selector(text=html_data)
        item={}
        item['file_path']=os.getcwd()+"/"+file_path
        item['list_of_car_names']=response.xpath('//div[@class="sl-heading-model-wrapper"]/h3/text()').getall()
        item['list_of_car_prices']=response.xpath('//h4[@class="sl-heading-prices sl-price"]/text()').getall()
        print(item)
        data_frame=pd.DataFrame(item)
        
        if os.path.exists("html_parsing_output.csv"):
            data_frame.to_csv('html_parsing_output.csv',mode='a',index=False,header=False)
        else:
            data_frame.to_csv('html_parsing_output.csv',mode='a',index=False)