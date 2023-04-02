import pandas as pd

def read_excel_file(readFile):
    data = {}
    data_xls = pd.io.excel.ExcelFile(readFile)
    try:
        for sheet_name in data_xls.sheet_names:
            output = pd.read_excel(readFile, engine='openpyxl', sheet_name=sheet_name)
            if(output.size > 0):
                data[sheet_name] = output
            print(sheet_name + " read end, total of " + str(output.shape[0]) + " 行 " + str(output.shape[1]) + " 列.")
    except Exception as e:
        print(e)
    finally:
        print(str(readFile) + "read end!")
    return data

def write_excel_file(data, writeFile):
    isSuccess = True
    try:
        writer = pd.ExcelWriter(writeFile)
        for sheet_name in data:
            df = pd.DataFrame(data[sheet_name])
            df.to_excel(excel_writer=writer, sheet_name=sheet_name)
    except Exception as e:
        print(e)
        isSuccess = False
    finally:
        writer.save()
        writer.close()
        print(str(writeFile) + "write end!" + str(isSuccess))
    return isSuccess

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(description="excel_utils.py usage help document")
    # 添加不带默认值的可解析参数
    parser.add_argument("-r", "--readFile", help="read excel file")  # 注意： -h、--help为内置参数，不可用
    ARGS = parser.parse_args()  # 获取命令行参数
    print('ARGS is :', ARGS)

    if(ARGS.readFile):
        data = read_excel_file(ARGS.readFile)
        for row_num in range(0, len(data)):
            res = data["Sheet1"].iloc[row_num]
            print("res is " + str(res))