# Dashboard-SAGEP

## About the Project

This project consists of an automation for creating a dashboard developed in Power BI with the aim of analyzing the status of the protocols circulating within the Adjunct Secretary of People Management (SAGEP), a sector of the State Department of Education of Pará (SEDUC).

## Main Features

- **Process Inquiry:** The bot will enter the "Unit Input" folder and scan the "JUDICIAL PROCESS" folder, generating a spreadsheet for individual consultation of each protocol. From this spreadsheet, the bot will query each protocol number present in it, generating a new spreadsheet only with the information that will be used to create the dashboard.

  - **Spreadsheet Processing:** A script designed to process the spreadsheets generated in the process inquiry, editing them to return only the information that will be used in the final dashboard.
  
  - **Average Response Time:** Stacked bar chart calculating the average response time in days that each sector of SAGEP takes to process a protocol.
  
  - **Total SAGEP Response:** Stacked column chart returning the range of days within which a process is responded to within SAGEP, ranging from 0 to 5 days or more, displayed as a percentage.
  
  - **Oldest Process by Sector:** Stacked bar chart returning the process(es) that have been stalled the longest in each sector, along with the number of days it has been stalled since its last processing.
  
  - **Processes in Progress by Sector:** Stacked bar chart counting how many processes are still in progress in each sector of SAGEP.
  
  - **Critical Process Table:** A table with the protocol number, originating sector, destination sector, and the time it has been stalled. Criticality is defined by processes that have been without a response for more than 2 days.
  
  - **Translated Sector Filter:** A filter to show only the data from the selected sector(s).
  
  - **In Progress:** Card counting how many processes are still in progress at SAGEP.
  
  - **Archived:** Card counting how many processes are not found at SAGEP.
  
  - **Total:** Card counting how many processes are within the SAGEP process box.
  
## How to Use

1. **Installation:** First, make sure to install the following applications:
   - Power BI Desktop: [Download Link](https://www.microsoft.com/en-us/download/details.aspx?id=58494)
   - Anaconda: [Installation Guide](https://docs.anaconda.com/free/anaconda/install/index.html)
   - Visual Studio Code: [Setup Guide for Windows](https://code.visualstudio.com/docs/setup/windows)
2. **Creating Environment in Anaconda:**
   - 2.1 **Open Terminal or Anaconda Prompt:** Open the terminal or Anaconda Prompt on your operating system.
   - 2.2 **Navigate to the virtual environment directory:** Use the 'cd' command to navigate to the directory where the virtual environment is located. For example, if the virtual environment is in your "Downloads" folder, you would use the command:
   'cd Downloads/Consulta-PAE'
   - 2.3 **Creating the virtual environment:** Once in the correct directory, you can create the virtual environment using the 'conda env create' command, followed by the YAML file name. Assuming the file is Consulta-PAE.yml, the command would be:
   'conda env create -f Consulta-PAE.yml'
   - 2.4 Start the virtual environment.
3. Start the Automacao_SAGEP_Busca_Processos_Judiciais.py file, after it finishes its operation the others will start automatically, generating the necessary spreadsheets for the dashboard.
4. **Data:** Ensure that the data is in the correct format and location.
5. **Loading:** Open Power BI and load the `.pbix` file from this repository.
6. **Updating:** After the first use, update the dashboard by clicking on the "Refresh" option.

## Contributing

Would you like to contribute? Fantastic! Here are the steps:

1. **Fork** this repository.
2. Create a new **Branch** for your modifications.
3. Make your changes or additions.
4. Make a **Pull Request** so we can review.

## Contact

- Adriano Pinheiro - adriano.pinheiro@castanhal.ufpa.br
- João Gabriel - jgteixeiraramos@gmail.com

Acknowledgments:

- To all who contributed to this project.
- To the developers of libraries and tools used.
