import os
import pandas as pd
from parsel import Selector
folder_name='D:\html_files'
for file_name in os.listdir(folder_name):
        print('file name------>',file_name)
        file_path=os.path.join(folder_name,file_name)
        print('file_path-------->',file_path)
        
        with open(file_path,'r',encoding='utf-8-sig')as file:
            html_data=file.read()
        response=Selector(text=html_data)
        item={}
        car_details=response.xpath('//div[@class="sl-heading-link"]')
        for car_detail in car_details:
            item['file_path']=file_path
            list_of_car_names=car_detail.xpath('.//div[@class="sl-heading-model-wrapper"]/h3/text()').get('')
            list_of_car_prices=car_detail.xpath('.//h4[@class="sl-heading-prices sl-price"]/text()').get()
            item['car_name']=list_of_car_names[5:]
            item['year']=list_of_car_names.split()[0]
            item['price']=list_of_car_prices.replace('$','')
            item['currency_symbol']=list_of_car_prices[0]
            
            df = pd.DataFrame([item])
            if os.path.exists("html_parsing_output.csv"):
                df.to_csv('html_parsing_output.csv',mode='a',index=False,header=False)
            else:
                df.to_csv('html_parsing_output.csv',mode='a',index=False)
