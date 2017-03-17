# Get Started with Smv Tutorial

After going through the [SmvTraining](https://github.com/TresAmigosSD/SmvTraining), there are a few more steps so that you can start this tutorial.

## 1. Prerequisites
**Step 1.1.** Git clone this project to your local environment:   
  `git clone https://github.com/DataSenseAnalytics/SmvTutorialBasics`

**Step 1.2**. Make sure Smv is successfully installed, if not please refer to the [installation guide](smv_install_sample_app.md#smv-installation).

**Step 1.3.** Install Jupyter  
1) If users are using SMV with docker, there is **no need to install** Jupyter in a specific docker container as it is already installed.  
2) If users have installed SMV and would like to use SMV locally without docker, users can continue on the below steps to set up Jupyter.  
- Please refer to [this guide](http://jupyter.org/install.html) to install Jupyter. After installation, type `jupyter --version` in terminal to validate the installation.
- Make sure `smv-jupyter` is in system PATH:   
  - Open ~/.bashrc:  `vi ~/.bashrc`
  - Add `export PATH=$PATH:SMV_HOME/tools` in the file (*note:* SMV_HOME is where SMV is installed), save and exit. Source the file `source ~/.bashrc`
- Copy required kernel json file and jupyter configuration:  
  <pre>
  cp SMV_HOME/docker/smv/kernel.json /usr/local/share/jupyter/kernels/smv-pyshell/kernel.json
  cp SMV_HOME/docker/smv/.jupyter/jupyter_notebook_config.py ~/.jupyter/
  </pre>

## 2. Launch Jupyter Notebook
**Step 2.1.** Go to the root directory of the sample project created in [SmvTraining](https://github.com/TresAmigosSD/SmvTraining), and make sure the project has already been built with `mvn package` or `sbt assembly`. Users using latest SMV with python interface may skip the building step, please kindly check the latest project.   

**Step 2.2.** Check if there is a directory "notebooks" existing under the root directory. Currently by customized configuration, "notebooks" will be the working directory and all notebooks will be stored in this directory.

**Step 2.3.** Type command `smv-jupyter` at **the root directory of a project** to start jupyter. Open a browser and type: `localhost:8888` in the address bar to access Jupyter web application. Please kindly note that users who are using virtual box or remote linux environment but would like to use Jupyter locally may need to bind the remote port to local environment.   

Now users are able to use smv functions, native pyspark and python functions to process and analyze data in an interactive environment.

## 3. Create Notebooks
**Step 3.1.** Click any existing notebook or click "New" at the top right corner to create a new notebook

**Step 3.2.** Write your first line in the notebook  
```python
print("hello world")
```

Now you are all set! :wink:
