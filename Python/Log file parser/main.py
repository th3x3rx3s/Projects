import os
main_path=os.getcwd()
os.chdir('logs')
exist=False
for x in os.listdir():
    if os.path.exists(fr"{main_path}\reports\{x}_report.csv"):
        exist=True
    with open(x, "r") as f, open(fr"{main_path}\reports\{x}_report.csv", "a") as csv:
        if exist == False:
            csv.write("Date;Time;Error code;Error message\n")
        else:
            csv.write("\n")
        for y in f:
            try:   
                date,error_code,error_message=y.strip().split(",")
                date_date,date_time=date.split(" ")
                csv.write(f"{date_date};{date_time};{error_code[-3:]};{error_message}\n")
            except ValueError as e:
                print(f"Unexpected error while processing line: {y.strip()},{e}")