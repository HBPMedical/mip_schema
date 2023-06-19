"""Standalone script for converting a CDEs Metadata Schema of the Medical Informatics Platform (MIP) from JSON format back to EXCEL format."""

import sys
import json
import argparse
import pandas as pd


JSON_EXCEL_FIELDS_MAP = {
    "label": "name",
    "code": "code",
    "type": "type",
    "enumerations": "values",
    "units": "units",
    "description": "description",
}

EXCEL_JSON_FIELDS_MAP = {
    "csvFile": "csvFile",
    "name": "label",
    "code": "code",
    "type": "type",
    "values": "enumerations",
    "units": "units",
    "description": "description",
    "canBeNull": "canBeNull",
    "comments": "comments",
    "conceptPath": "conceptPath",
    "methodology": "methodology",
}


def create_parser():
    """Create argument parser of the script.

    Returns
    -------
    p : argparse.ArgumentParser
        Parser of the script.
    """
    parser = argparse.ArgumentParser(
        description="Convert MIP CDE Metadata Schema from JSON format (.json) to EXCEL format (.xls)"
    )
    parser.add_argument("--json", type=str, required=True, help="json file path")
    parser.add_argument("--excel", type=str, required=True, help="excel file path")
    return parser


def recursive_parse_json(json_data: dict, concept_path=[]):
    """Parse MIP CDEs Metadata Schema json data to a list of dict items to create a dataframe.

    Parameters
    ----------
    json_data : dict
        MIP CDEs Metadata Schema json data.

    concept_path : list
        List of concept path.

    Returns
    -------
    data : list
        List of parsed data.
    """
    data = []
    if isinstance(json_data, dict):
        for attribute, value in json_data.items():
            # handle variables at this hierarchical level
            if attribute == "variables":
                for variable in value:
                    data_row = []
                    for key in EXCEL_JSON_FIELDS_MAP.keys():
                        json_key = EXCEL_JSON_FIELDS_MAP[key]
                        if json_key in variable.keys():
                            if isinstance(variable[json_key], list):
                                dict_strings = [
                                    f'"{elem["code"]}":"{elem["label"]}"'
                                    for elem in variable[json_key]
                                ]
                                dict_string = "{" + ",".join(dict_strings) + "}"
                                data_row.append(dict_string)
                            else:  # str
                                data_row.append(variable[json_key])
                        elif json_key == "conceptPath":
                            concept_path_copy = concept_path.copy()
                            if len(concept_path_copy) == 0:
                                concept_path_copy.append(json_data["code"])
                            else:
                                concept_path_copy.append(json_data["label"])
                            concept_path_copy.append(variable["code"])
                            concept_path_str = "/".join(concept_path_copy)
                            data_row.append(concept_path_str)
                        else:
                            data_row.append("")
                    data.append(data_row)

            if attribute == "groups":
                concept_path_copy = concept_path.copy()
                if len(concept_path_copy) == 0:
                    concept_path_copy.append(json_data["code"])
                else:
                    concept_path_copy.append(json_data["label"])
                data += recursive_parse_json(value, concept_path=concept_path_copy)
    else:
        for item in json_data:
            concept_path_copy = concept_path.copy()
            data += recursive_parse_json(item, concept_path=concept_path_copy)
    return data


def main():
    """Main script function.

    Returns
    -------
    exit_code : {0, 1}
        Exit code (0: success / 1: error)
    """
    # Create the parser and parse the arguments
    parser = create_parser()
    args = parser.parse_args()

    # Check if the json schema file exists
    with open(args.json, "r") as f:
        cdes_data = json.load(f)

    # Parse the json data to a list of dict items with
    # "csvFile", "name", "code", "type", "values", "units",
    # "description", "canBeNull", "comments", "conceptPath",
    # and "methodology keys that can be used to create a pandas
    # dataframe
    result = recursive_parse_json(cdes_data)

    # Create a pandas dataframe from the list of dict items
    df = pd.DataFrame(result, columns=EXCEL_JSON_FIELDS_MAP.keys())
    print(df)

    # Write the pandas dataframe to an excel file
    df.to_excel(args.excel, engine="openpyxl", index=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
