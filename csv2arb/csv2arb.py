import glob
import csv

##
## read .csv
##

try:
    csv_name = glob.glob('*.csv')[0]

except:
    exit('No .csv exists')

with open(csv_name,'r') as csv_file:
    csv_content = [row for row in csv.reader(csv_file)]


##
## save as .arb
##

for country_index in range(len(csv_content[0])):
    if csv_content[0][country_index] == "" : continue

    with open(f"app_{ csv_content[0][country_index] }.arb",'w') as arb_file:
        arb_file.write("{\n")
        arb_file.write(f"   \"@@locale\": \"{csv_content[0][country_index]}\",\n")
        arb_file.write("\n")

        for value_index in range(len(csv_content)):
            if value_index == 0: continue
            if value_index != len(csv_content)-1:
                arb_file.write(f"   \"{csv_content[value_index][0]}\": \"{csv_content[value_index][country_index]}\",\n")
            else:
                arb_file.write(f"   \"{csv_content[value_index][0]}\": \"{csv_content[value_index][country_index]}\"\n")

        arb_file.write("}\n")
