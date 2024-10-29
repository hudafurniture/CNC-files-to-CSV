import os
from pathlib import Path
import csv

def main():
    #script_directory = ""
    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_dir = script_directory+"/qr_csv"
    
    qrcode_set = set()
    for root, dirs, files in os.walk(script_directory):
        for f in files:
            if(f.endswith(".scx") or f.endswith(".SCX")):
                file_path = os.path.join(root, f)
                print(f)
                print(file_path)
                qrcode_set.add(os.path.splitext(f)[0])
        

    os.makedirs(output_dir, exist_ok=True)
    csv_file_name = 'output_csv_QRcodes_'
    
    '''
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for code in qrcode_set:
            writer.writerow([code])    
    
    txt_file = os.path.join(output_dir, csv_file_name+'.txt')
    with open(txt_file, 'w') as file:
        for code in qrcode_set:
            file.write(code + '\n')     
            
             '''
             
    lines_per_file = 2000
    file_counter = 1
    line_counter = 0

    txt_file = os.path.join(output_dir, f"{csv_file_name}_{file_counter}.txt")
    file = open(txt_file, 'w')

    for code in qrcode_set:
        file.write(f"{code}\n")
        line_counter += 1
        
        if line_counter == lines_per_file:
            file.close() 
            file_counter += 1 
            txt_file = os.path.join(output_dir, f"{csv_file_name}_{file_counter}.txt")
            file = open(txt_file, 'w')  
            line_counter = 0  

    file.close()        
                                
    
    print(str(len(qrcode_set)) + " different barcodes were found!")         
    input("Press enter to exit;")
            

    
    
    
    
    
  
  
    
if __name__ == "__main__":
    main()
