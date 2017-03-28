# Prepare for Your Own Project
After you have successfully initialized a project and make sure the sample module can be run (which confirms your smv is correctly installed and configured), it is natural the next question would be how to make this become your own project.

## Customize the Initialized Project
Users can freely modify the project name, stage name and the name of the parent file for modules to customize the initialized project to their own projects.

### Change the names of directories
Users can change the name of the root directory to fit for their own projects. For example, when you initialized the project, you put it as "MyApp" temporarily and later on you decide to name your project as "MyProject". You may need to pay attention to the data directory (details to be discussed below) when you are modifying the name of the project.

As mentioned under `src/main/python` users can write core source scripts of a project, and to change the name of a stage, what users need to do are: 1) modify the directory name, for example change "stage1" to "etl_stage"; 2) modify the stage definition in app configuration (details to be discussed below).

### Change the names of files
To better organize the scripts, users could use multiple `.py` files to hold the modules. As in the example project, in the file `employment.py` there are 2 modules defined. When users are creating modules for own project, users can choose to change the name of this file (for example to `etl_fact_table.py`), or to create new `.py` files and remove this one.  

## Project Configuration
As mentioned in the [initialization section](myapp_init.md), under `conf/` directory there are 2 files to host app-level and user-level configurations.

### App-Level Configuration
The app-level configurations are those that are shared across all users of the app, for example app name and the stages in the app.

Users can edit the `smv-app-conf.props` file:  
```python
# application name
smv.appName = Test App

# stage definitions
smv.stages = stage1, stage2, ...
```   
Note that during the project development, users can always come back and add more stages in the definition.  

### User-Level Configuration
Configurations like data direcories may not necessarily be the same for all users, hence each user can specify in user-level configuration file `smv-user-conf.props`:  
```python
# when input and output directories share the same parent directory, users can just specify dataDir
smv.dataDir = file:///xxx/MyApp/data  

# when input and output directories do not share the same parent directory
smv.inputDir = file://xxx
smv.outputDir = file://xxx
```
Users can specify `file://` or `hdfs://` before the path depending on the location of the data. Note that if you have changed the root directory name of the project, please remember to modify the data directory accordingly.


## Prepare Input Data
To start developing your own project, the input data need to be prepared first.  

Currently SMV supports input data in csv format and hive table. We will take csv format as the starting point to build a project. For the usage of hive tables, please kindly refer to [this guide](https://github.com/TresAmigosSD/SMV/blob/master/docs/user/smv_input.md#hive-table-input).

For the tutorial purpose, assume we have another piece of employment data [CB1200CZ11_dummy.csv](../../dummy_data/CB1200CZ11_dummy.csv) and we would like to add this table and use it in the project.

### Prepare schema for csv files
Each csv file requires a [SmvSchema](http://tresamigossd.github.io/SMV/scaladocs/index.html#org.tresamigos.smv.SmvSchema) file which defines the column name and data types. The schema file should be of the same name with the dataset and `.schema` as the extension. A basic schema file contains column name and its corresponding data type, for example:  
<pre>...
ST: Integer
ZIPCODE: Integer
...</pre>  

Various [data types](https://github.com/TresAmigosSD/SMV/blob/master/docs/user/smv_input.md#supported-schema-types) are supported in the schema definition. There are mainly two ways to create the schema:  
1) Manually write the schema file in the required format  
2) Leverage the `discoverSchema` function. Enter the `smv-pyshell` or `smv-jupyter` environment, and use the following commands:  
<pre> >>> discoverSchema("data/input/xxx.csv")</pre>

By default `discoverSchema` will detect the data types of all the fields from the first 100000 records of the input file, with the assumption that the it is a csv file of default format (delimited by ",", with '\"' as quote character and with header). If users would like to use fewer or more records for schema detection, or the input file is not in default format (for example, the delimiter is "~"), users can specify the corresponding parameters with [`CsvAttributes`]()

An example of using `discoverSchema` with parameters to discover the schema of the dummy data is as below:
```python
>>> discoverSchema("../dummy_data/CB1200CZ11_dummy.csv", 100, ca = CsvAttributes(delimiter = '|', hasHeader = True))
```

A temporary schema file named `CB1200CZ11_dummy.schema.toBeReviewed` will be generated under the **project root directory** after running the command. Users can rename and use it as the schema if there is no error after reviewing; otherwise users can also easily modify data types and other attributes in the temporary schema file.

### Define input directory
As discussed before, users can either configure the specific location of the input data and schema, or put the input data and schema to the pre-defined input directory. For example we can copy `CB1200CZ11_dummy.csv` and `CB1200CZ11_dummy.schema` to `data/input/employment_dummy/`

Now you are ready to load new data and create new module upon them.
