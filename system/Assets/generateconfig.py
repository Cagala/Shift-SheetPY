import configparser

def createConfig(path=str):
    config_file = configparser.ConfigParser()

    config_file.add_section("Credentials")
    config_file.set("Credentials", "CredsPath", path+r"\Assets\Config\creds.json")

    config_file.add_section("Sheet")
    config_file.set("Sheet", "SheetName", "SheetPy")

    config_file.add_section("SheetRangeRow")
    config_file.set("SheetRangeRow", "From", "17")
    config_file.set("SheetRangeRow", "To", "99")

    config_file.add_section("SheetRangeCol")
    config_file.set("SheetRangeCol", "From", "2")
    config_file.set("SheetRangeCol", "To", "7")

    config_file.add_section("CellGroup")
    config_file.set("CellGroup", "GOMEZ", "G")
    config_file.set("CellGroup", "LOPEZ", "B")

    config_file.add_section("PointCellGroup")
    config_file.set("PointCellGroup", "LOPEZ", "B")

    with open(path+r"\Assets\Config\sheet_config.ini", "w") as configObj:
        config_file.write(configObj)
        configObj.flush()
        configObj.close()