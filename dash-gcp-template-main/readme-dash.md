# Steps to follow

1. Open Google Cloud Shell

	In your home directory create a virtual environment using the command below

	`python3 -m venv myenv`

2. Activate the environment:

	`source myenv/bin/activate`

3. You can download the files in this repository using the download button given on the project homepage: https://gitlab.com/mobibootcamp/dash-gcp-template 
In the home directory of your google cloud shell, make a folder called 'dash-gcp-template' and upload the extracted files from the zip file into 'dash-gcp-template'. You will find the upload button in the top navigation bar of the Google Cloud shell terminal in the 'more' icon.

Alternative; You can also clone your repository from the home directory, using git, with the command given below:

`git clone https://gitlab.com/mobibootcamp/dash-gcp-template.git`

This will create a directory 'dash-gcp-template' and will download all the files from the git repository

4. Cd to home directory and run the below command

	`pip install -r ./dash-gcp-template/requirements.txt`

5. After all the packages are downloaded, cd to 'dash-gcp-template' folder start the app using the command below:

	`python3 main.py`

After the above step, you can see your app running at port 8080 by clicking on Web Preview icon on the cloud console. To stop this app, go to your google cloud shell terminal and press Crtl+C. This will shutdown your Dash app on your cloud shell

6. To deploy to GCP, select the project to which you want to deploy through the dropdown box in the Google cloud shell terminal and then run the below command:

	`gcloud app deploy`

Once deployed your project URL is displayed which you can invoke to see your application on GCP. You can now send this link to anyone who wishes to see your project

The above steps are high level. You may have to follow the GCP prompts for login, enabling certain API permissions for the project etc..

A few more things to note:
1. If you installed any new libraries using pip, be sure to add that library in requirements.txt file.
2. For datafiles, upload the files into your project folder and use relative paths to access your files. e.g., if you created a folder called 'data' in your project root and uploaded your 'my-data.csv' file into this folder, then you can create a dataframe using `df = pd.read_csv('data/my-data.csv')`
3. Dash works well with plotly-express library only. Seaborn and Matplotlib figures need some extra steps 
before they can be displayed on Dash. Refer eg3-matplotlib-image.py file to see an example.
 So I would highly encourage you to only use Plotly-express module for this assignment
4. There are a few more example files in this repository; example of callback function, etc.. You can run each one individually for e.g, running `python 'eg3-matplotlib-image.py` runs only this file. You can delete all these example files as required.
5. You can edit your project files using the 'Open Editor' button on the top navigation bar of your google cloud shell terminal

# Selenimum references
* https://selenium-python.readthedocs.io/installation.html
* https://selenium-python.readthedocs.io/waits.html - refer how to wait for the element to load
