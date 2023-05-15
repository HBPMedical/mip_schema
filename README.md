# MIP Common Data Elements Metadata Schema Tool (`mip_schema`)

Open-source Python package to manipulate Common Data Elements Metadata Schema for the Medical Informatics Platform (MIP).

## How to install?

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

### `mip_update_cdes_json`

Script to update the CDES JSON/EXCEL file pair to make this process more reproducible. 

**Usage**

In a terminal, you can run it with the folllowing command:
```
$ mip_update_cdes_json \
    --cdes_json_file "/path/to/CDEsMetadata.json" \
    --cdes_excel_file "/path/to/myCDEs.xlxs" \
    --command "remove_dashes_and_underscores" \
    --output_suffix "updated" \
    --log_file "/path/to/CDEs_update.log" 
```
**Note:** You can use the option `-h`to show more details about usage documentation.

Available commands:

- `remove_dashes_and_underscores`: Remove dashes and underscores.

