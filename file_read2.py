with open("C:\Daniel\Supporting_files\larg_sample_html_file_download_for_testing.html",'r') as file:
    file_val=file.readlines()
for col in file_val:
    if 'Row' in col:
        print(col[1:6])
   