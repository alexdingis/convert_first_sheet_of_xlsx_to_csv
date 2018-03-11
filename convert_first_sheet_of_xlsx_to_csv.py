import os
import pandas as pd
import time
#
#
#
xlsx_dir   = r"C:\some\path\to\a\dir\full\of\xlsx"
#
csv_dir    = r"C:\some\path\to\an\output\dir"
#
#
#
def convert_first_sheet_of_xlsx_to_csv(input_xlsx_dir, output_csv_dir):
    #
    start_time = time.time()
    #
    try:
        #
        xlsx_file_paths = [os.path.join(input_xlsx_dir, x) for x in os.listdir(input_xlsx_dir) if x.endswith(".xlsx") == True]
        #
        for xlsx_file_path in xlsx_file_paths:
            #
            xlsx_name   = (xlsx_file_path.split('\\')[-1]).replace(".xlsx","")
            #
            csv_output  = os.path.join(output_csv_dir, xlsx_name + ".csv")
            #
            xl          = pd.ExcelFile(xlsx_file_path)
            #
            first_sheet = xl.sheet_names[0]
            #
            df          = xl.parse(first_sheet)
            #
            df.to_csv(csv_output, sep = ",", index = False)
            #
        #
    except Exception as e:
        #
        print e
        #
    #
    end_time = round(time.time() - start_time, 5)
    #
    print "Seconds elapsed: {0}".format(end_time)
    #
#
#
#
convert_first_sheet_of_xlsx_to_csv(xlsx_dir, csv_dir)
#
