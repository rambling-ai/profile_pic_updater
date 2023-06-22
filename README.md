# LinkedIn Profile Picture Updater

This simple Python project allows you to automatically update your LinkedIn profile picture daily with a different picture from a specified folder. You can use it to keep your LinkedIn profile fresh and engaging with minimal effort.

Warning: this tool is all in good fun and perfectly harmless, but use it at your own risk. Using automated tooling on LinkedIn could possibly get your account banned.

## Setup

1. Go to the project's GitHub repository at [https://github.com/rambling-ai/profile_pic_updater](https://github.com/rambling-ai/profile_pic_updater).

2. Click on the `Code` button and select `Download ZIP`.

3. Once the ZIP file is downloaded, extract it to a location of your choice.

4. Open Terminal.

5. Use the `cd` command to navigate to the extracted folder. For example, if the extracted folder is on your Desktop, you would type `cd ~/Desktop/profile_pic_updater-main` and press Enter.

6. Once you're inside the folder, install Playwright by typing `python3 -m pip install playwright` and then press Enter.

7. After the installation of Playwright is complete, type `playwright install` followed by Enter to download the required browser binaries.

8. Inside this folder you will find another folder called `pics_to_upload`. This is where you should place the pictures you want to use for your LinkedIn profile. Make sure these pictures are in either .jpg or .png format.

## Running the Scripts

### Manual Run

To run the scripts manually, follow these steps:

1. Open Terminal.

2. Navigate to the script folder as explained in the Setup section above.

3. Type `python3 daily_pic_update.py` and press Enter. This will run the script, which will update your LinkedIn profile picture with the first picture in the `pics_to_upload` folder.

### Automate the Runs

To automate this task, we will use a feature of macOS called "cron". Cron allows you to schedule tasks to run automatically at specific times. In this case, we will set it up to run `daily_pic_update.py` once a day.

1. Open Terminal.

2. Type `crontab -e` and hit Enter. This command opens your crontab file in an editor.

3. Add a new line that looks like this:

   `0 0 * * * /usr/local/bin/python3 /path/to/daily_pic_update.py`

   Make sure to replace `/path/to/` with the actual path to the `daily_pic_update.py` script. This line will run your script every day at midnight.

4. Save and exit the editor (press CTRL + X, then Y, then Enter).

5. You can check if your cron job has been added by typing `crontab -l` in Terminal.

## Troubleshooting

If you run into any issues while setting up or running the scripts, please check the following:

1. Make sure Python and Playwright are installed correctly. You can test your Python installation by typing `python3 --version` in Terminal. You can test your Playwright installation by typing `python3 -m playwright` in Terminal.

2. Make sure the `daily_pic_update.py` and `update_profile_pic.py` scripts are in the same folder and that you've correctly navigated to this folder in Terminal before trying to run them.

3. Make sure your `pics_to_upload` folder contains at least one .jpg or .png picture.

Enjoy your daily fresh LinkedIn profile pictures!
