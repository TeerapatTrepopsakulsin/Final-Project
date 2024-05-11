# Road incident deaths

## Description
The GUI application created using Tkinter and Python to allows a user to visualise, analyse, and interact with global road incident deaths data to obtain useful knowledge or insights.
The application contains 3 pages, a Storytelling page, a DataExploration page, and a Dataset page.

The data on the Storytelling page will be displayed as descriptive statistics, graphs, and charts, with little interactivity. On the DataExploration page, the user can fully alter the view and interact with graphs to gain their interest information (age, type, year, etc.), which will be displayed differently depending on the filtered parameters after a graph is generated. Lastly, the Dataset page displays the dataset used for calculating and generating the graph for this project. (Road_incident_deaths.csv [Check out my data processing](https://github.com/TeerapatTrepopsakulsin/Year1-Project/wiki/Data-Processing)).

## Application UI (MS Windows)
|Page| Application UI  |
|--------|--------------------|
|Storytelling|![Storytelling](https://github.com/TeerapatTrepopsakulsin/Year1-Project/blob/main/screenshots/data/Storytelling.png)|
|DataExploration|![DataExploration](https://github.com/TeerapatTrepopsakulsin/Year1-Project/blob/main/screenshots/DataExploration.png)|
|Dataset|![Dataset page](https://github.com/TeerapatTrepopsakulsin/Year1-Project/blob/main/screenshots/Dataset.png)|

## Python files
|File| Usage |
|--------|--------------------|
|graph_ui.py|Main UI of the application.|
|pages.py|Page module which contains the frame of all 3 pages.|
|sub_component.py|Components which are used by some pages.|
|controller.py|Controller module which connects the generators to the UI.|
|graph_generator.py|Classes for generating graphs.|
|entity.py|Contains an Enum class of entity lists.|
|main.py|Main block for running the application.|

## Installing the Application
See [How to Install](https://github.com/TeerapatTrepopsakulsin/Year1-Project/wiki/Installation) in the project wiki.

## Running the Application
1. Activate the Virtual Environment
   
   MS Windows: 
     ```
     .\env\Scripts\activate
     ```
   Unix or MacOS:
     ```
     . env/bin/activate
     ```
2. Run the command
   ```
   python main.py
   ```
3. Deactivate the Virtual Environment
   ```
   deactivate
   ```
## Project Documents
[Project Proposal](https://docs.google.com/document/d/16FDrOhwlrF2d_EaP7QpTq1581u-YMD_n5A2Fp7wgljw/edit?usp=sharing)

[Development Plan](https://github.com/TeerapatTrepopsakulsin/Year1-Project/wiki/Development-Plan)

[UML Diagram](https://github.com/TeerapatTrepopsakulsin/Year1-Project/wiki/UML-Diagram)

[Data Processing](https://github.com/TeerapatTrepopsakulsin/Year1-Project/wiki/Data-Processing)

## Source of Data
The datasets used in this project are from [Our World in Data](https://ourworldindata.org/) and [World Health Organization](https://www.who.int//)

1. [Death rate from road injuries, 1990 to 2019](https://ourworldindata.org/grapher/death-rates-road-incidents?tab=table)
2. [Deaths from road incidents, by type, 1990 to 2019](https://ourworldindata.org/grapher/road-deaths-by-type)
3. [Deaths from road incidents, by age, 1990 to 2019](https://ourworldindata.org/grapher/road-incident-deaths-by-age)
4. [Deaths from road injuries, 1990 to 2019](https://ourworldindata.org/grapher/number-of-deaths-from-road-injuries?tab=table)
5. [Population](https://ourworldindata.org/grapher/population?tab=table)
6. [Maximum speed limits by country](https://apps.who.int/gho/data/node.main.A1007?lang=en)
7. [Seat-belt law by country](https://apps.who.int/gho/data/node.main.A1003?lang=en)
