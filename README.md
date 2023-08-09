# MIP Common Data Elements Metadata Schema Tool (`mip_schema`)

![Latest GitHub Release](https://img.shields.io/github/v/release/HBPMedical/mip_schema) ![Latest GitHub Release Date](https://img.shields.io/github/release-date/HBPMedical/mip_schema) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8056344.svg)](https://doi.org/10.5281/zenodo.8056344)

Open-source Python package to manipulate Common Data Elements Metadata Schema for the Medical Informatics Platform (MIP).

## How to install?

### For the user

1. Create your installation directory, go to this directory, and create a new virtual Python 3.9 environment:

```bash
$ mkdir -p "/installation/directory"
$ cd "/prefered/directory"
$ virtualenv venv -p python3.9
```

2. Activate the environment and install the package, at a specific version, directly from GitHub with Pip:

```bash
$ source ./venv/bin/activate
(venv) $ pip install git+https://github.com/HBPMedical/mip_schema.git@0.0.4
```

### For the developer

1. Clone the Git repository in your prefered directory:

```bash
$ cd "/prefered/directory"
$ git clone git@github.com:HBPMedical/mip_schema.git
```

2. Go to the cloned repository and create a new virtual Python 3.9 environment:

```bash
$ cd mip_schema
$ virtualenv venv -p python3.9
```

3. Activate the environment and install the package with Pip:

```bash
$ source ./venv/bin/activate
(venv) $ pip install -e .
```

## Available command-line tools

### `mip_schema_update`

Script to update the CDES JSON/EXCEL file pair to make this process more reproducible. 

**Usage**

In a terminal, you can run it with the folllowing command:
```
$ mip_schema_update \
    --cdes_json_file "/path/to/CDEsMetadata.json" \
    --cdes_excel_file "/path/to/myCDEs.xlxs" \
    --command "remove_dashes_and_underscores" \
    --output_suffix "updated" \
    --log_file "/path/to/CDEs_update.log" 
```
**Note:** You can use the option `-h`to show more help about command usage.

Available commands:

- `remove_dashes_and_underscores`: Remove dashes and underscores.


### `mip_schema_convert_from_json`

Script to convert the CDES in JSON format back to the EXCEL format ingested by the Data Catatog.

**Usage**

In a terminal, you can run it with the folllowing command:
```
$ mip_schema_convert_from_json \
    --json "/path/to/CDEsMetadata.json" \
    --excel "/path/to/myOutputCDEs.xlxs" \
```
**Note:** You can also use the option `-h`to show more help about command usage.

## Funding

This project received funding from the European Union's H2020 Framework Programme for Research and Innovation under the Specific Grant Agreement No. 945539 (Human Brain Project SGA3, as part the Medical Informatics Platform (MIP)).
