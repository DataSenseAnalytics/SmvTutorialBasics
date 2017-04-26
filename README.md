# Smv Tutorial

This is a tutorial for people to have an idea of how to conduct various data analyses using [SMV](https://github.com/TresAmigosSD/SMV) (Spark Modularized View) - a framework to use Spark to develop large scale data applications. The latest user guide can be found [here](https://github.com/TresAmigosSD/SMV/blob/master/docs/user/0_user_toc.md), Python API docs can be found [here](http://tresamigossd.github.io/SMV/pythondocs/1.5.2.7/index.html). After the tutorial, users are expected to be able to build a data analytics project with Smv framework.

The tutorial basics will mainly cover the following contents:

## I. Preliminaries
First things first. We need to make sure we have all necessary tools installed and the environment set up.
* [Installation and A Sample Project](./docs/smv_install_sample_app.md)
* [Get Started with the Tutorial](./docs/tutorial_get_started.md)


## II. A Taste of Smv for Data Analyses
Once we have the environment set up, we can start doing some cool things. As a data scientist or a business analyst who may be familiar with traditional analytic tools such as SQL or SAS, it is natural to ask how to process data and conduct analyses in Smv. We will leverage the employment data in the SmvTraining in the following examples. The sample file in the data directory was directly extracted from US employment data.   
```
$ wget http://www2.census.gov/econ2012/CB/sector00/CB1200CZ11.zip
$ unzip CB1200CZ11.zip
$ mv CB1200CZ11.dat CB1200CZ11.csv
```
*More info can be found on [US Census site](http://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=BP_2012_00CZ1&prodType=table)*  

Now we will show how convenient and efficient data analyses can be with Smv.

* [Profile Input Data](./MyApp_smv_example/notebooks/Profile_Input_Data.ipynb)  
* [Identify Insights from Data](./MyApp_smv_example/notebooks/Identify_Insights.ipynb)  
* [Advanced Analytics](./MyApp_smv_example/notebooks/Advanced_Analytics.ipynb)  
* [Quality Control](./MyApp_smv_example/notebooks/Quality_Control.ipynb)
* [Smv Exercise 1: Employment Data](./docs/exercise1.md)

## III. How to Create and Develop a Project
Now that you have seen how to conduct relatively ad-hoc analyses with SMV, it is time to see how a project is actually created and developed with SMV.

* [Initialize a Project](./docs/myapp_dev/myapp_init.md)
* [Prepare for Your Own Project](./docs/myapp_dev/myapp_prep.md)
* [Data and Project Development](./docs/myapp_dev/myapp_develop.md)
* [Smv Exercise 2: Create New Modules](./docs/exercise2.md)

## Remarks
Smv offers a the modularized computation framework, where the scalability and reusability of data, code is expected to finally scale the development team and reduce the development time of a complicated and large scale project. This tutorial is mainly to help users get familiar with how to build a project with Smv, and users are always encouraged to follow the latest development of [SMV project](https://github.com/TresAmigosSD/SMV) and check the corresponding API docs for detailed help.
