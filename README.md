# Smv Tutorial

This is a tutorial for people to have an idea of how to conduct various data analyses using [SMV](https://github.com/TresAmigosSD/SMV) (Spark Modularized View) - a framework to use Spark to develop large scale data applications. API docs can be found [here](http://tresamigossd.github.io/SMV/scaladocs/index.html#org.tresamigos.smv.package). After the tutorial, users are expected to be able to build a data analytics project with Smv framework.

The tutorial basics will mainly cover the following contents:

## I. Preliminaries
First things first. We need to make sure we have all necessary tools installed and the environment set up.
* [Installation and A Sample Project](./docs/smv_install_sample_app.md)
* [Get Started with the Tutorial](./docs/tutorial_get_started.md)


## II. A Taste of Smv for Data Analyses
Now we have the environment set up, we can start doing some cool things. As a data scientist or a business analyst who may be familiar with traditional analytic tools such as SQL or SAS, it is natural to ask how to process data and conduct analyses in Smv. Leveraging the [employment data](https://github.com/TresAmigosSD/SMV/blob/master/docs/user/getting_started.md#example-app-data-directory) in the SmvTraining, we will show how convenient and efficient data analyses can be with Smv.

* [Profile Input Data](./MyApp_smv_example/notebooks/Profile_Input_Data.ipynb)  
* [Identify Insights from Data](./MyApp_smv_example/notebooks/Identify_Insights.ipynb)  
* [Advanced Analytics](./MyApp_smv_example/notebooks/Advanced_Analytics.ipynb)  
* [Quality Control](./MyApp_smv_example/notebooks/Quality_Control.ipynb)
* [Smv Exercise 1: Employment Data](./docs/exercise1.md)


## Remarks
Smv offers a the modularized computation framework, where the scalability and reusability of data, code is expected to finally scale the development team and reduce the development time of a complicated and large scale project. This tutorial is mainly to help users get familiar with how to build a project with Smv, and users are always encouraged to follow the latest development of [SMV project](https://github.com/TresAmigosSD/SMV) and check the corresponding API docs for detailed help.
